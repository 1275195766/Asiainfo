# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:41:25 2020

@author: gaojiafeng
"""

import pandas as pd 
import os
import re
path="D:\文档\亚信实习\工作\国际漫游数据质量核查\国际漫游数据质量核查\\"
os.chdir(path) #路径需要根据自己的文件存放位置进行修改
day = "6月26日"


'''
两份编码表存在不完整的问题，合并两份数据使用
'''

tb_area_0 = pd.read_excel(path+"tbl_area.xlsx",converters={'id':str,"name":str}) #路径需要根据自己的文件存放位置进行修改
tb_area_0 = tb_area_0.loc[:, ['id', 'name']]

#对比两个码表，tbl_area主是是多了很多市辖区的数据，建议与逍遥线上所用编码保持一致
area_code = pd.read_excel(path+'area_code.xlsx', converters = {'countyID':str, 'cityId':str, 'prov':str})#路径需要根据自己的文件存放位置进行修改
area_code['provName'] = area_code.provName.apply(lambda x: re.sub("省|市|自治区|维吾尔|回族|壮族", "" ,x))
area_code['cityName'] = area_code.cityName.apply(lambda x:  re.sub('市', '', x) if x in ['上海市', '北京市', '天津市', '重庆市'] else x) 

tb_area_1 = pd.concat([area_code.loc[:, ['countyID', 'countyName']].rename(columns = {'countyID':'id', 'countyName':'name'}), area_code.loc[:, ['cityId', 'cityName']].rename(columns = {'cityId':'id', 'cityName':'name'}), area_code.loc[:, ['prov', 'provName']].rename(columns = {'prov':'id', 'provName':'name'})]).drop_duplicates()

tb_area = pd.merge(tb_area_1, tb_area_0, how = "outer", on = "id")
tb_area["name"] = tb_area.apply(lambda row: row["name_x"] if pd.notnull(row["name_x"]) else row["name_y"], axis = 1)
tb_area = tb_area.drop(['name_x', 'name_y'], axis = 1)

tb_city = pd.read_excel(path+"地市编码-漫入话单.xlsx", converters = {'id':str, 'name':str}) #路径需要根据自己的文件存放位置进行修改

tb_prov = pd.read_excel(path+"省份编码-漫入话单.xlsx", converters = {'id':str})#路径需要根据自己的文件存放位置进行修改
tb_prov['prov_name'] = tb_prov.prov_name.apply(lambda x: "内蒙古" if x == "内蒙" else x)


file_imsi =open(r"xinling_imsi_count.dat", encoding="utf-8")
data_imsi = pd.read_table(file_imsi,  sep = "|",header=None, names=['prov', '信令imsi数量'], converters = {"prov":str},engine='python')
result_xl = pd.merge(data_imsi, tb_area, how="left", left_on ="prov", right_on = "id").drop("id", axis = 1).drop("prov", axis = 1)


#话单imsi
data_src = pd.read_table("src_imsi_count.dat", sep = "|", header=None, names=['prov', '话单imsi数量'], converters = {'prov':str}, engine='python')
data_src['prov'] = data_src.prov.apply(lambda x:x.strip())
result_src = pd.merge(data_src, tb_prov, how="left", left_on="prov", right_on="id").drop(["id", "prov"], axis =1)

#信令话单交集的imsi个数
data_inner = pd.read_table("join_count.dat", sep = "|", header=None, names=['prov', '重叠imsi数量'], converters = {'prov':str}, engine='python')
result_inner = pd.merge(data_inner, tb_prov, how="left", left_on="prov", right_on="id").drop(["id", "prov"], axis =1)

data_out = pd.merge(result_xl, result_src, how="outer", left_on="name", right_on="prov_name")
data_out = pd.merge(data_out, result_inner, how="outer", on="prov_name")
data_out["provName"]=data_out.apply(lambda row: row["name"] if pd.notnull(row["name"]) else row["prov_name"], axis=1)
data_out.loc[:, ["provName", "信令imsi数量", "话单imsi数量", "重叠imsi数量"]].fillna(0).to_excel("国际漫游数据质量核查-逍遥"+day+".xlsx", index=False)


#话单找不到信令
data_diff = pd.read_table("src_detail_sample.dat", sep = "|", usecols=[0, 1, 2, 3, 4, 5, 6], header=None, names=['ph', 'imsi', 'country', 'countryNo', 'prov', 'cityId', 'startTime'], converters = {'ph':str,'imsi':str, 'country':str, 'countryNo':str,'prov':str, 'cityId':str,  'startTime':str}, engine='python')

data_diff['prov'] = data_diff.prov.apply(lambda x:x.strip())
data_diff['cityId'] = data_diff.cityId.apply(lambda x:x.strip() if pd.notnull(x) else x)

data_1 = pd.merge(data_diff, tb_prov, how="left", left_on="prov", right_on="id").drop(["prov", "id"], axis=1)
data2 =pd.merge(data_1, tb_city, how='left', left_on="cityId", right_on="id").drop(["cityId", "id"], axis=1)

data2.to_excel("话单里找不到信令的imsi示例"+day+".xlsx", index=False)

