import random
import time

import requests
import json
import pandas as pd


def get_prov(key_word,region):
    param={
        "query":key_word,
        "tag":"火车站",
        "region":region,
        "output":"json",
        "coord_type":3,
        "page_size":1,
        "ak":"sEtYdhBIhgomgTGOkGOea2QOCd05uxr4"
    }
    api_url='http://api.map.baidu.com/place/v2/search?'
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63"}
    res=requests.get(url=api_url,params=param,headers=header)
    # print(res.text)
    try:
        prov_json=json.loads(res.text)
        prov=prov_json['results'][0]['province']
        city=prov_json['results'][0]['city']
        adname=prov_json['results'][0]['area']
    except BaseException as e:
        print('error')
        print(e)
        with open(r'D:\文档\亚信实习\工作\iop\火车站\stain.log', 'a+') as w:
            w.write(key_word)


    return prov,city,adname

def start():
    print('开始抓取。。。。')
    print('读取Excel生成Dateframe。。。。')
    df=pd.read_excel(r'D:\文档\亚信实习\工作\iop\火车站\拆分了火车站省和站名v1.xlsx',sheet_name='Sheet2')
    print('Success')
    stain_list=df.站.values
    prov_lsit=[]
    print('开始获取数据。。。。')
    for stain in stain_list:
        try:
            print(stain)
            region=df.loc[df.站==stain,'省'].to_list()
            # print(region)
            prov,city,adname=get_prov(stain,region[0])
            print("省：{0} 市：{1} 县：{2}".format(prov,city,adname))
            df.loc[df.站==stain,'province']=prov
            df.loc[df.站==stain,'city']=city
            df.loc[df.站==stain,'area']=adname
        except BaseException as e :
            print(e)
            with open(r'D:\文档\亚信实习\工作\iop\火车站\stain.log','a+') as w:
                w.write(stain+'\n')
        finally:
            # time.sleep(random.randint(1,3))
            time.sleep(0.3)
        pass
    # df1=pd.DataFrame(prov_lsit)
    print('数据获取完成，开始生成Excel。。。。')
    df.to_excel(r'D:\文档\亚信实习\工作\iop\火车站\火车站上级行政区.xlsx',index=None)
    print('生成成功，请到 D:\文档\亚信实习\工作\iop\火车站 目录下查看！！！')
    pass



if __name__=="__main__":
    # start()
    prov,city,adname=get_prov('博乐站','全国')
    print(prov,city,adname)



