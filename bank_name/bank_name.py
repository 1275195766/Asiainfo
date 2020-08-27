# coding: utf-8

# In[34]:


def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res

import requests
import re
from lxml import etree
import random
import re
from pandas import DataFrame
import pandas as pd
#定义爬取的对象
channel_name = []
area_info = []
bank_name = []
addr = []
tel_no = []
location =[]
county = []


city_name=[
"610200","610300","610400","610500","610600","610700","610800","610900","611000"
]

keyword=['银行']
for city in city_name:
  for kw in keyword:
      with open('res_json.json', 'a+') as f:
          for i in [1,2,3,4,5,6,7,8,9,10,11]:
            print(i)
            url="http://restapi.amap.com/v3/place/text?&keywords={}&city={}&offset=50&page={}&output=json&key=9e7db922b2fc634f3b272a2cd002274f&extensions=all".format(kw,city,i)
            print(url)
            head={
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                  "Accept-Encoding": "gzip, deflate",
                  "Accept-Language": "zh-CN,zh;q=0.9",
                  "Cache-Control":"max-age=0",
                  "Connection": "keep-alive",
                  "Cookie": "guid=1bb4-a836-96c4-2354; key=bfe31f4e0fb231d29e1d3ce951e2c780; cna=g+EXFAUw8HgCAX1Uu+iAN+qh; isg=BBsbId7sw7qurj9OszACg0rgqn-F8C_y1Y90WA1ZCZol7D3OlcHoQ8YlggpHTIfq",
                  "Host": "restapi.amap.com",
                  "Upgrade-Insecure-Requests": "1",
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
                  }
            res=requests.get(url,headers=head)
            res.encoding=res.apparent_encoding
            result=res.text



            input_channel_name = re.compile('"name":"(.*?)"').findall(result)
            channel_name.append(input_channel_name)

            input_lnglat = re.compile('"location":"(.*?)"').findall(result)
            location.append(input_lnglat)

            input_tel = re.compile('"tel":"(.*?)"').findall(result)
            tel_no.append(input_tel)

            input_addr = re.compile('"address":"(.*?)"').findall(result)
            addr.append(input_addr)

            input_county = re.compile('"adname":"(.*?)"').findall(result)
            county.append(input_county)

            input_bankname=re.compile('"type":"(.*?)"').findall(result)
            bank_name.append(input_bankname)

      channel_name = flat(channel_name)
      tel_no = flat(tel_no)
      addr = flat(addr)
      county = flat(county)
      location=flat(location)
      bank_name=flat(bank_name)
      wangdian = pd.DataFrame([channel_name,addr,tel_no,county,location,bank_name]).T
      wangdian.columns = (["网点名称","地址","电话","区县","经纬度","银行名称"])
      wangdian = wangdian.drop_duplicates()
      wangdian1=wangdian.loc[wangdian['电话']==None]
      wangdian       
      
      print("city:{}".format(city))
      wangdian.to_csv("{}.csv".format(city),header = True, sep='/',encoding = "ANSI")
      channel_name = []
      area_info = []
      bank_name = []
      addr = []
      tel_no = []
      location =[]
      county = []