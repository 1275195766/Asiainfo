import pandas as pd
import re


df=pd.read_excel(r'天津银行信息未筛选v1.xlsx')
df.drop_duplicates(subset='网点名称',inplace=True)

test=list(df.网点名称)
l=[]

for i in range(len(test)):
    r=re.search(r'(装修中)|(24小时)|(自助)|(停车场)|(ATM)',test[i])
    if r is None:
        l.append(test[i])
# test.remove('')
# test.sort(reverse = True)

df1=df[df.网点名称.isin(l)]

df1.to_excel(r'天津银行信息去重v2.xlsx', header=['银行名称', '网点名称', '地址', '联系电话', '经度', '纬度', '地市名称', '区县名称'], index=None,
                engine='openpyxl')
pass