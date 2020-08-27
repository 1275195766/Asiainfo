import requests
import json
import pandas as pd
import random
import time
import logging
LOG_FORMAT = "%(lineno)d - %(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='全国城市中心点-v1.log', level=logging.ERROR, format=LOG_FORMAT)

def get_json(query,region,df):
    header_list=[{"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"},
                 {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52"}
                 ]

    ak=['LyIM4GPhDU9cMnA6G3sBW4GDrdMock64','sEtYdhBIhgomgTGOkGOea2QOCd05uxr4']

    headers=random.choice(header_list)
    params = {
        'query': query,  # 检索关键字
        'region': region,  # 检索行政区划区域
        'output': 'json',  # 输出格式为json
        'scope': '2',  # 检索结果详细程度。取值为1 或空，则返回基本信息；取值为2，返回检索POI详细信息
        'page_size': 5,  # 单次召回POI数量，默认为10条记录，最大返回20条。
        'page_num': 0,  # 分页页码，默认为0,0代表第一页，1代表第二页，以此类推。
        'ak': random.choice(ak),
        'coord_type':'bd09ll',     #坐标类型
        # 'city_limit' :'true'
    }
    url="http://api.map.baidu.com/place/v2/search"

    res_page0=requests.get(url,params=params,headers=headers).text
    js_page0=json.loads(res_page0)
    data = []
    try:
        data.append(js_page0['results'][0]['province'])
        data.append(js_page0['results'][0]['city'])
        data.append(js_page0['results'][0]['area'])
        data.append(js_page0['results'][0]['name'])
        data.append(js_page0['results'][0]['location']['lat'])
        data.append(js_page0['results'][0]['location']['lng'])
        data.append(js_page0['results'][0]['address'])

        size = df.index.size
        df.loc[size] = data
    except BaseException as e:
        print(e,query)
        # error=e+'prov:'+query
        logging.error(query)
        # logging.error(query)
    time.sleep(random.randint(1,2))

    # time.sleep(random.randint(1,4))




if __name__=="__main__":

    data=pd.read_excel(r'D:\文档\亚信实习\工作\基站经纬度爬虫\全国行政区划码-v2.xlsx',header=0)
    pass

    print(data.columns)
    df = pd.DataFrame(columns=["province", "city", "area", "name", "lat", "lng", "address"])
    writer = pd.ExcelWriter(r'全国城市中心点-v4.xlsx')
    for prov in data['单位名称']:
        print(prov)
        query=prov.strip()+'政府'
        get_json(query,prov,df)
        df.to_excel(excel_writer=writer,sheet_name='Sheet1')
        writer.save()
    writer.close()
