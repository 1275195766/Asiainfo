# -*- coding: utf-8 -*-
import json
import requests
import math

key = 'sEtYdhBIhgomgTGOkGOea2QOCd05uxr4'  # 这里填写你的百度开放平台的key
x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 扁率

def geocode(address):
    #利用百度geocoding服务解析地址获取位置坐标
    #:param address:需要解析的地址
    #:return:
    geocoding = {'s': 'rsv3',
                 'key': key,
                 'city': '全国',
                 'address': address}
    res = requests.get(
        "http://restapi.amap.com/v3/geocode/geo", params=geocoding)
    if res.status_code == 200:
        json = res.json()
        status = json.get('status')
        count = json.get('count')
        if status == '1' and int(count) >= 1:
            geocodes = json.get('geocodes')[0]
            lng = float(geocodes.get('location').split(',')[0])
            lat = float(geocodes.get('location').split(',')[1])
            return [lng, lat]
        else:
            return None
    else:
        return None

def gcj02tobd09(lng, lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param lng:火星坐标经度
    :param lat:火星坐标纬度
    :return:
    """
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * x_pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * x_pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006




    # param={
    #     "coords":str(lng)+','+str(lat),
    #     "from":3,
    #     "to":5,
    #     "ak":"sEtYdhBIhgomgTGOkGOea2QOCd05uxr4"
    # }
    # header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
    # url='http://api.map.baidu.com/geoconv/v1/'
    # res=requests.get(url,params=param)
    # json_res=json.loads(res.text)
    # bd_lng=json_res["result"][0]['x']
    # bd_lat=json_res["result"][0]['y']



    return [bd_lng, bd_lat]


def bd09togcj02(bd_lon, bd_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bd_lat:百度坐标纬度
    :param bd_lon:百度坐标经度
    :return:转换后的坐标列表形式
    """
    x = bd_lon - 0.0065
    y = bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    gg_lng = z * math.cos(theta)
    gg_lat = z * math.sin(theta)
    return [gg_lng,gg_lat]


def wgs84togcj02(lng, lat):
    """
    WGS-84转GCJ-02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [mglng,mglat]


def gcj02towgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return lng, lat
    dlat = transformlat(lng - 105.0, lat - 35.0)
    dlng = transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = lat + dlat
    mglng = lng + dlng
    return [lng * 2 - mglng,lat * 2 - mglat]


def transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
        0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
        0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret


def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    if lng < 72.004 or lng > 137.8347:
        return True
    if lat < 0.8293 or lat > 55.8271:
        return True
    return False

'''
if __name__ == '__main__':
    lng = 128.543
    lat = 37.065
    result1 = gcj02tobd09(lng, lat)
    result2 = bd09togcj02(lng, lat)
    result3 = wgs84togcj02(lng, lat)
    result4 = gcj02towgs84(lng, lat)
    result5 = geocode('北京市朝阳区朝阳公园')
    print result1, result2, result3, result4, result5
'''
'''
BD09转gcj02
gcj02转wgs84
'''

#f=open(r"D:\PycharmProjects\\untitled\network_catch\a.txt",'r')
#print(f)
#lng=[]
#lat=[]
#for line in f.readlines():
#    #rint(line.strip)
#    lng.append(line.split(',',1)[0])
#    lat.append(line.split(',',1)[1])
#    #print(lng[0],lat[0])
#f.close
#
#list_lon_lat_gcj=[[0]*2 for i in range(0,len(lng))]
#_lon_gcj=[[0]*1 for i in range(0,len(lng))]
#_lat_gcj=[[0]*1 for i in range(0,len(lng))]
#list_lon_lat_wgs=[[0]*2 for i in range(0,len(lng))]
#_lon_wgs=[[0]*1 for i in range(0,len(lng))]
#_lat_wgs=[[0]*1 for i in range(0,len(lng))]
#for i in range(0,len(lng)):
#    list_lon_lat_gcj[i]=bd09togcj02(float(lng[i]),float(lat[i]))
#    _lon_gcj[i]=list_lon_lat_gcj[i][0]
#    _lat_gcj[i]=list_lon_lat_gcj[i][1]
#    list_lon_lat_wgs[i] = gcj02towgs84(float( _lon_gcj[i]), float(_lat_gcj[i]))
#    _lon_wgs[i] = list_lon_lat_wgs[i][0]
#    _lat_wgs[i] = list_lon_lat_wgs[i][1]
#    #print(list_lon_lat_wgs[i])
#    with open(r"D:\PycharmProjects\\untitled\network_catch\a2.txt",'at') as f:
#        f.write(str(list_lon_lat_gcj[i])+'\n')
#    with open(r"D:\PycharmProjects\\untitled\network_catch\a3.txt",'at') as f:
#        f.write(str(list_lon_lat_wgs[i])+'\n')


"""
gcj02转BD09
"""

#f=open(r"D:\PycharmProjects\\untitled\network_catch\a.txt",'r')
#print(f)
#lng=[]
#lat=[]
#for line in f.readlines():
#    #rint(line.strip)
#    lng.append(line.split(',',1)[0])
#    lat.append(line.split(',',1)[1])
#    #print(lng[0],lat[0])
#f.close
#list_lon_lat_bd=[[0]*2 for i in range(0,len(lng))]
#_lon_bd=[[0]*1 for i in range(0,len(lng))]
#_lat_bd=[[0]*1 for i in range(0,len(lng))]
#
#for i in range(0,len(lng)):
#    list_lon_lat_bd[i]=gcj02tobd09(float(lng[i]),float(lat[i]))
#    _lon_bd[i]=list_lon_lat_bd[i][0]
#    _lat_bd[i]=list_lon_lat_bd[i][1]
#    print(list_lon_lat_bd[i])
#    with open(r"D:\PycharmProjects\untitled\network_catch\a1.txt",'at') as f:
#        f.write(str(list_lon_lat_bd[i])+'\n')


#print(gcj02tobd09(104.056104,30.547307));
#print(bd09togcj02(104.05562271220187, 30.636738386146323))
#print(gcj02towgs84(104.049185,30.630456))
#103.951278,30.593061
#104.049185,30.630456

#104.05562271220187, 30.636738386146323
