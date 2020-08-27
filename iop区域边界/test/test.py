#coding:utf8
import json
import requests
# citys="北京市,天津市,上海市,重庆市,河北省,山西省,辽宁省,吉林省,黑龙江省,江苏省,浙江省,安徽省,福建省,江西省,山东省,河南省,湖北省,湖南省,广东省,海南省,四川省,贵州省,云南省,陕西省,甘肃省,青海省,内蒙古自治区,广西壮族自治区,西藏自治区,宁夏回族自治区,新疆维吾尔自治区".split(',')
# name_dic={}
# for city in citys:
#     param={
#         "query":'机场',
#         "tag":"机场",
#         "region":city,
#         "output":"json",
#         "coord_type":3,
#         "page_size":20,
#         "ak":"sEtYdhBIhgomgTGOkGOea2QOCd05uxr4"
#     }
#     api_url='http://api.map.baidu.com/place/v2/search?'
#     header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63"}
#     res=requests.get(url=api_url,params=param,headers=header)
#     dic=[]
#     for result in json.loads(res.text)['results']:
#         dic.append(result['name'])
#     name_dic[city]=dic
#     with open('name.txt','w') as f:
#         f.write(str(name_dic))
#     print(dic)
#     pass
#
#
#
dic={"天津市": ["天津滨海国际机场", "天津塘沽机场", "天津滨海窦庄通用机场", "天津滨海东方通用直升机场"], "上海市": ["上海浦东国际机场", "上海虹桥国际机场",  "崇明机场", "上海高东直升机场", "龙华机场", ], "重庆市": ["重庆江北国际机场", "万州五桥机场", "黔江武陵山机场", "重庆巫山机场", ], "河北省": ["石家庄正定国际机场"], "山西省": ["太原武宿国际机场"], "辽宁省": ["大连周水子国际机场"], "黑龙江省": ["哈尔滨太平国际机场"], "江苏省": ["南京禄口国际机场", "南京老山直升机场"], "安徽省": ["合肥新桥国际机场"], "福建省": ["厦门高崎国际机场"],"山东省": ["青岛流亭国际机场"], "河南省": ["郑州新郑国际机场"], "湖北省": ["武汉天河国际机场", "通用机场"], "湖南省": ["长沙黄花国际机场"], "广东省": ["深圳宝安国际机场", "深圳南头直升机场", "直升机场"], "海南省": ["海口美兰国际机场"], "四川省": ["成都双流国际机场"], "贵州省": ["贵阳龙洞堡国际机场"], "云南省": ["昆明长水国际机场"], "陕西省": ["西安咸阳国际机场"], "甘肃省": ["兰州中川国际机场"], "青海省": ["花土沟机场", "德令哈机场", "格尔木机场"], "西藏自治区": ["拉萨贡嘎国际机场"], "宁夏回族自治区": ["银川河东国际机场"], "新疆维吾尔自治区": ["乌鲁木齐地窝堡国际机场"]}
for d in dic.keys():
    print(dic[d])