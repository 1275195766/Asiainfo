import requests
import json

def airport():
    citys="北京市,天津市,上海市,重庆市,河北省,山西省,辽宁省,吉林省,黑龙江省,江苏省,浙江省,安徽省,福建省,江西省,山东省,河南省,湖北省,湖南省,广东省,海南省,四川省,贵州省,云南省,陕西省,甘肃省,青海省,内蒙古自治区,广西壮族自治区,西藏自治区,宁夏回族自治区,新疆维吾尔自治区".split(',')
    name_dic={}


    for city in citys:
        airport_name_list = []
        param={
            "keywords":"机场",
            "city":city,
            "output":"json",
            "offset":20,
            "page":1,
            "key":"f69a0c4146782da8ca2745bd4c8508e9",
            "extensions":"all"
        }
        name_dic[city]=''
        url="https://restapi.amap.com/v3/place/text?"
        try:
            header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63"}
            res=requests.get(url,params=param,headers=header)
            print(res.status_code)
            for airport in json.loads(res.text)['pois']:
                airport_name_list.append(airport['name'])
            name_dic[city]=airport_name_list
        except BaseException as e:
            print(e)
    return name_dic


