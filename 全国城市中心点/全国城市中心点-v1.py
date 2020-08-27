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

    # ak=['LyIM4GPhDU9cMnA6G3sBW4GDrdMock64','sEtYdhBIhgomgTGOkGOea2QOCd05uxr4']

    headers=random.choice(header_list)
    params = {
        'query': query,  # 检索关键字
        'region': region,  # 检索行政区划区域
        'output': 'json',  # 输出格式为json
        'scope': '2',  # 检索结果详细程度。取值为1 或空，则返回基本信息；取值为2，返回检索POI详细信息
        'page_size': 5,  # 单次召回POI数量，默认为10条记录，最大返回20条。
        'page_num': 0,  # 分页页码，默认为0,0代表第一页，1代表第二页，以此类推。
        'ak': 'iHMauZIIRXPoHAaynTkb6P3xtH2i2Wld',
        'coord_type':'bd09',     #坐标类型
        # 'city_limit' :'true'
    }
    url="http://api.map.baidu.com/place/v2/search"
    print(params)
    res_page0=requests.get(url,params=params,headers=headers)
    print(res_page0.url)
    js_page0=json.loads(res_page0.text)
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

    # data=pd.read_excel(r'D:\文档\亚信实习\工作\基站经纬度爬虫\全国行政区划码-v2.xlsx',header=0)
    pass

    # print(data.columns)
    df = pd.DataFrame(columns=["province", "city", "area", "name", "lat", "lng", "address"])
    prov_dic = {
        "天津市": ["和平区"],
        "河北省": [
            '河北省',
            '井陉县',
            '正定县',
            '深泽县',
            '元氏县',
            '玉田县',
            '遵化市',
            '昌黎县',
            '丛台区',
            '桥东区',
            '平乡县',
            '清苑区',
            '涞水县',
            '蠡县',
            '雄县',
            '定州市',
            '高碑店市',
            '桥东区',
            '宣化区',
            '下花园区',
            '蔚县',
            '双桥区',
            '鹰手营子矿区',
            '沧州市',
            '青县',
            '东光县',
            '盐山县',
            '黄骅市',
            '三河市',
            '安平县',
            '景县'
        ],
        "山西省": [
            '山西省',
            '太原市',
            '云冈区',
            '广灵县',
            '城区',
            '矿区',
            '郊区',
            '平定县',
            '上党区',
            '城区',
            '昔阳县',
            '稷山县',
            '垣曲县',
            '河津市',
            '定襄县',
            '静乐县',
            '偏关县',
            '临汾市',
            '尧都区',
            '洪洞县',
            '古县',
            '乡宁县',
            '汾西县'
        ],
        "内蒙古自治区": [
            '内蒙古自治区',
            '回民区',
            '赤峰市',
            '宁城县',
            '敖汉旗',
            '科尔沁区',
            '鄂尔多斯市',
            '商都县'
        ],
        "辽宁省": [
            '辽宁省',
            '和平区'
        ],
        "吉林省": [
            '吉林省',
            '西安区'
        ],
        "黑龙江省": ['黑龙江省',
                 '郊区',
                 '西安区'
                 ],
        "上海市": ['上海市'],
        "江苏省": ['江苏省'],
        "浙江省": ['浙江省', '江北区'],
        "安徽省": ['安徽省', '郊区'],
        "福建省": ['福建省'],
        "江西省": ['江西省'],
        "山东省": ['山东省'],
        "河南省": ['河南省'],
        "湖北省": ['湖北省'],
        "湖南省": ['湖南省'],
        "广东省": ['广东省', '城区'],
        "广西壮族自治区": ['广西壮族自治区', '城中区'],
        "海南省": ['海南省', '三沙市'],
        "重庆市": ['江北区'],
        "四川省": ['四川省', '西区'],
        "贵州省": ['贵州省'],
        "云南省": ['云南省'],
        "西藏自治区": ['西藏自治区'],
        "陕西省": ['陕西省'],
        "甘肃省": ['甘肃省'],
        '青海省': ['青海省', '城中区'],
        "宁夏回族自治区": ['宁夏回族自治区'],
        '新疆维吾尔自治区': ['新疆维吾尔自治区', '新市区', '阿拉山口市', '胡杨河市'],

    }
    writer = pd.ExcelWriter(r'全国城市中心点-v3.xlsx')
    for prov in prov_dic:
        print(prov)
        for d in prov_dic[prov]:
            query=d.strip()+'政府'
            get_json(query,prov,df)
            df.to_excel(excel_writer=writer,sheet_name='Sheet1')
            writer.save()
    writer.close()
