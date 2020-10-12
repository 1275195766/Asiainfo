import time

import json
import urllib.parse
from selenium import webdriver
import re
import pandas as pd


city_code={
"120000":"天津市",
"120100":"天津市市辖区",
"120101":"和平区",
"120102":"河东区",
"120103":"河西区",
"120104":"南开区",
"120105":"河北区",
"120106":"红桥区",
"120110":"东丽区",
"120111":"西青区",
"120112":"津南区",
"120113":"北辰区",
"120114":"武清区",
"120115":"宝坻区",
"120116":"滨海新区",
"120117":"宁河区",
"120118":"静海区",
"120119":"蓟州区"
}






def get_prov(yq_name,driver,pd_list):

    # url = 'https://restapi.amap.com/v3/place/text?'
    driver.get('https://www.amap.com/')
    main_url = 'https://www.amap.com/service/poiInfo?'
    # param = {
    #     'keyword': yq_name,
    #     'types':'营业厅=0.589000;银行',
    #     'city':'120000',
    #     'citylimit':'true',
    #     # 'children': 4,
    #     'offset': 25,
    #     'page': 1,
    #     'output':'json',
    #     'extensions': 'all',
    #     'key':'f69a0c4146782da8ca2745bd4c8508e9'
    # }
    param={
        "query_type": "TQUERY",
        "pagesize": "20",
        "pagenum": 1,
        "qii": "true",
        "cluster_state": 5,
        "need_utd": "true",
        "utd_sceneid": 1000,
        "div": "PC1000",
        "addr_poi_merge": "true",
        "is_classify": "true",
        "zoom": "14.05",
        "classify_data": "query_type=TQUERY+reserved_keywords=true;category=1601",
        "user_loc": "117.256046,39.143066",
        "geoobj": "117.209519|39.133399|117.329159|39.154664",
        "city": 120000,
        "keywords": yq_name
    }
    url=main_url+urllib.parse.urlencode(param)
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}



    try:
        driver.get(url)
        res=driver.find_element_by_id('json').text
        res_json=json.loads(res)
        total=res_json['data']['total']
        for i in range(1,int(total)//20+1):

            param['pagenum']=i
            url = main_url + urllib.parse.urlencode(param)

            try:
                driver.get(url)
                res1 = driver.find_element_by_id('json').text
                # res_json1 = json.loads(res1)
                for poi in json.loads(res1)['data']['poi_list']:
                    row_list = []
                    print(yq_name, poi['name'],i)

                    r=re.search(r'(.*)\(.*',poi['name'])
                    bank_name= r.group(1) if r is not None else poi['name']
                    row_list.append(bank_name)
                    row_list.append(poi['name'])

                    row_list.append(poi['address'])
                    phone= poi['tel'] if poi['tel']!='' else ''
                    row_list.append(phone)
                    row_list.append(poi['longitude'])
                    row_list.append(poi['latitude'])
                    row_list.append(poi['cityname'])

                    row_list.append(city_code[poi['adcode']])

                    pd_list.append(row_list)
                    time.sleep(0.5)

                # print(pd_list)
                df = pd.DataFrame(pd_list)
                df.to_excel('天津银行信息未筛选v1.xlsx', header=['银行名称', '网点名称', '地址', '联系电话', '经度', '纬度', '地市名称', '区县名称'], index=None,engine='openpyxl')
                time.sleep(1)
            except BaseException as e1:
                with open(r'天津银行.log','a+') as f:
                    f.write(url)
                    f.write('\n')
                print('内层try')
                print(e1)
    except Exception as e :
        print('外层try')
        print(e)
    # res=driver.page_source
    pass


    



if __name__=="__main__":
    bank_list = ["工商银行",
                 "建设银行",
                 "招商银行",
                 "中国银行",
                 "农业银行",
                 "交通银行",
                 "广发银行",
                 "中信银行",
                 "光大银行",
                 "华夏银行",
                 "兴业银行",
                 "民生银行",
                 "邮政储蓄",
                 "北京银行",
                 "平安银行"]


    pd_list = []

    driver = webdriver.Firefox()
    driver.set_window_size(950, 1030)
    main_url = 'https://www.amap.com/'

    # for bank in bank_list:
    get_prov('银行',driver,pd_list)

    df = pd.DataFrame(pd_list)
    df.to_excel('天津银行信息.xlsx', header=['银行名称', '网点名称', '地址', '联系电话', '经度', '纬度', '地市名称', '区县名称'], index=None,
                engine='openpyxl')

    pass