#coding:utf-8
def flat(nums):
    res = []
    for i in nums:
        if isinstance(i, list):
            res.extend(flat(i))
        else:
            res.append(i)
    return res

import json
import re
import time
import pandas as pd


# channel_name = []
# area_info = []
# bank_name = []
# addr = []
# tel_no = []
# location =[]
# county = []
with open('res_json.json','r') as f:
    d=f.readlines()
    # print(len(d))



def re_():
    channel_name = []
    area_info = []
    bank_name = []
    addr = []
    tel_no = []
    location = []
    county = []
    start_time=time.time()
    # with open('res_json.json','r') as f:
    #     result=f.read()
    n=0
    for result in d:

        input_channel_name = re.compile('"name":"(.*?)"').findall(result)
        channel_name.append(input_channel_name)
        n += len(input_channel_name)

        input_lnglat = re.compile('"location":"(.*?)"').findall(result)
        location.append(input_lnglat)

        input_tel = re.compile('"tel":"(.*?)"').findall(result)
        tel_no.append(input_tel)

        input_addr = re.compile('"address":"(.*?)"').findall(result)
        addr.append(input_addr)

        input_county = re.compile('"adname":"(.*?)"').findall(result)
        county.append(input_county)

        input_bankname=re.compile('"type":"(.*?)"').findall(result)
        bank_name.append(channel_name)
        end_time=time.time()
    print(end_time-start_time)

    print(n)
    channel_name = flat(channel_name)
    tel_no = flat(tel_no)
    addr = flat(addr)
    county = flat(county)
    location = flat(location)
    bank_name = flat(bank_name)
    wangdian = pd.DataFrame([channel_name, addr, tel_no, county, location, bank_name]).T
    wangdian.columns = (["网点名称", "地址", "电话", "区县", "经纬度", "银行名称"])
    wangdian = wangdian.drop_duplicates()
    # wangdian1=wangdian.loc[wangdian['电话']==None]
    # wangdian

    # print("city:{}".format(city))
    wangdian.to_csv("{}.csv".format("re_"), header=True, sep='|', encoding="ANSI")
    # channel_name.clear()
    # area_info.clear()
    # bank_name.clear()
    # addr.clear()
    # tel_no.clear()
    # location.clear()
    # county.clear()


def json_():
    channel_name = []
    area_info = []
    bank_name = []
    addr = []
    tel_no = []
    location = []
    county = []
    start_time = time.time()
    # with open('res_json.json', 'r') as f:
    #     res = f.read()
    channel_name1=[]
    n=0
    for res in d:
        # print(res)
        # result = json.loads(res)
    #     n += 1

        result=json.loads(res)

        for p in result["pois"]:
            try:
                input_channel_name=p["name"]
                channel_name.append(input_channel_name)

                input_lnglat = p["location"]
                location.append(input_lnglat)

                input_tel = p["tel"]
                tel_no.append(input_tel)

                input_addr = p["address"]
                addr.append(input_addr)

                input_county = p["adname"]
                county.append(input_county)

                input_bankname = p["type"]
                bank_name.append(input_bankname)

            except BaseException as e:
                input_channel_name = ''
                channel_name.append(input_channel_name)
                print(e)

        channel_name1.append(channel_name)
        print(n)

    end_time = time.time()
    print(end_time - start_time)
    print(len(channel_name))
    print('------------------------------------------')
    wangdian = pd.DataFrame([channel_name, addr, tel_no, county, location, bank_name]).T
    wangdian.columns = (["网点名称", "地址", "电话", "区县", "经纬度", "银行名称"])
    wangdian = wangdian.drop_duplicates()
    # wangdian1=wangdian.loc[wangdian['电话']==None]
    # wangdian

    # print("city:{}".format(city))
    wangdian.to_csv("{}.csv".format("json_"), header=True, sep='|', encoding="ANSI")


# for i in range(10):
re_()

json_()