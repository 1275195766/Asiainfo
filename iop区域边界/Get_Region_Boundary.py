# -*- coding:utf-8 -*-
import sys
import urllib.request
from urllib.parse import quote
import numpy as np
import json
from iop区域边界 import coditransfor
from iop区域边界 import bdrtransform
import pandas as pd
from pandas import Series, DataFrame
from multiprocessing.dummy import Pool as pl
import os

#搜素的城市名(全名)
def getlnglat(address):
    key = 'adddc47b9d4c6bb9f395bd316b07df9b'
    url = 'http://restapi.amap.com/v3/config/district?'
    uri = url + 'keywords=' + quote(address) + '&key=' + key + '&subdistrict=1' + '&extensions=all'

    # 访问链接后，api会回传给一个json格式的数据
    temp = urllib.request.urlopen(uri)

    temp = json.loads(temp.read())

    # polyline是坐标，name是区域的名字
    # city_code=temp["districts"][0]['citycode']
    Data = temp["districts"][0]['polyline']
    name = temp["districts"][0]['name']
    # polyline数据是一整个纯文本数据，不同的地理块按照|分，块里面的地理信息按照；分，横纵坐标按照，分，因此要对文本进行三次处理
    Data_Div1 = Data.split('|')  # 对结果进行第一次切割，按照|符号
    len_Div1 = len(Data_Div1)  # 求得第一次切割长度

    num = 0
    len_Div2 = 0  # 求得第二次切割长度，也即整个数据的总长度
    while num < len_Div1:
        len_Div2 += len(Data_Div1[num].split(';'))
        num += 1

    num = 0
    num_base = 0
    output = np.zeros((len_Div2, 5)).astype(np.float)  # 循环2次，分割；与，
    while num < len_Div1:
        temp = Data_Div1[num].split(';')
        len_temp = len(temp)
        num_temp = 0
        while num_temp < len_temp:
            output[num_temp + num_base, :2] = np.array(temp[num_temp].split(','))  # 得到横纵坐标
            output[num_temp + num_base, 2] = num_temp + 1  # 得到横纵坐标的连接顺序
            output[num_temp + num_base, 3] = num   # 得到块的序号
            num_temp += 1
        num_base += len_temp
        num += 1
    output = DataFrame(output, columns=['lng_gcj02', 'lat_gcj02', '连接顺序', '块', '名称'])
    output['名称'] = name
    output1=output.astype({"块":int},errors='raise')
    # output1.sort_values(by='块',ascending=False,inplace=True)
    output1.loc[output1['块']!=0,"标识"]='I'




    return output1

def getSubName(address):
    key = 'adddc47b9d4c6bb9f395bd316b07df9b'
    url = 'http://restapi.amap.com/v3/config/district?'
    uri = url + 'keywords=' + quote(address) + '&key=' + key + '&subdistrict=1' + '&extensions=all'
    temp = urllib.request.urlopen(uri)
    temp = json.loads(temp.read())
    list0 = temp['districts'][0]['districts']
    num_Qu = 0
    output = []
    while num_Qu < len(list0):
        output.append(list0[num_Qu]['adcode'])
        num_Qu += 1
    return output

def data_write(addr_name):
    num = 0
    # ad = getSubName(addr_name)  # 得到某市下属区域的城市代码
    add = getlnglat(addr_name)  # 得到某市整个的边界数据
    # while num < len(ad):
    #     add = pd.concat([add, getlnglat(ad[num].encode("utf-8"))])  # 得到某市下属的全部区域的边界数据
    #     num += 1
    #增加百度坐标
    add = add.astype(str)
    lng_list = list(add['lng_gcj02'])
    lat_list = list(add['lat_gcj02'])
    list_bd09_lon_lat = [[0] * 2 for i in range(len(lng_list))]
    _longitude_ct_bd09 = [[0] * 1 for i in range(len(lng_list))]
    _latitude_ct_bd09 = [[0] * 1 for i in range(len(lng_list))]
    for i in range(0, len(lng_list)):
        """
           GCJ02(火星坐标系)转BD-09(百度)
        """
        # print(i)
        list_bd09_lon_lat[i] = coditransfor.gcj02tobd09(float(lng_list[i]), float(lat_list[i]))
        _longitude_ct_bd09[i] = list_bd09_lon_lat[i][0]
        _latitude_ct_bd09[i] = list_bd09_lon_lat[i][1]
    add['lng_bd09'] = _longitude_ct_bd09
    add['lat_bd09'] = _latitude_ct_bd09
    add=add.reindex(columns=['lng_gcj02', 'lat_gcj02', 'lng_bd09','lat_bd09','连接顺序', '块', '标识','名称'])
    # print(add)
    # add=add.sort_values('块')
    add1=add.reindex(columns=[ 'lng_bd09','lat_bd09', '块', '标识'])
    # print(add1)
    # add1.sort_values(by=['块'], axis=0, ascending=True, inplace=True)

    # zb_temp=add1.to_string(header=0,index=0,na_rep='')
    # print(zb_temp)

    s=add1.to_string(header=0,index=0)
    print(s)
    add1.to_csv("temp.csv",columns=[ 'lng_bd09','lat_bd09', '块', '标识'],header=0,index=0, encoding="utf-8")


    zb_res=bdrtransform.boundary_transfor("temp.csv",addr_name)
    print("%s is finished!" %(addr_name))
    return zb_res



def start(addr_list):
    key = 'adddc47b9d4c6bb9f395bd316b07df9b'
    url = 'http://restapi.amap.com/v3/config/district?'
    # addr_list = ["杭州市"]
    # addr_list=["1833"]
    try:
        zb_res=data_write(addr_list)
        print(zb_res)
        # pool = pl(8)  # 初始化线程池
        # pool.map(data_write, addr_list)
        # pool.close()
        # pool.join()
    except UnboundLocalError as err:
        print("error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

if __name__ == '__main__':
    # key = 'adddc47b9d4c6bb9f395bd316b07df9b'
    # url = 'http://restapi.amap.com/v3/config/district?'
    # addr_list=["杭州市"]
    # #addr_list=["1833"]
    # try:
    #     pool = pl(8)  # 初始化线程池
    #     pool.map(data_write, addr_list)
    #     pool.close()
    #     pool.join()
    # except UnboundLocalError as err:
    #     print("error: {0}".format(err))
    # except:
    #     print("Unexpected error:", sys.exc_info()[0])
    #     raise
        # print(results)
    start("三沙市西沙群岛")
