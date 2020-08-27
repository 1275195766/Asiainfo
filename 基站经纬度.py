import requests
import pandas as pd
import json
df=pd.read_table('F:\pythonPrj\Asiainfo\新疆信令与基站中的数据差异量@20200801@乌市待修复基站v1.txt',sep='|',header=None,names=['lac_id','cell_id','cell_name','lng','lat'],engine='python',encoding='utf-8')
lac_dict=df.lac_id.to_dict()
ci_dict=df.cell_id.to_dict()

mcc=460
mnc=0
coord='bd09'
output='json'
new_lat_list=[]
new_lng_list=[]
new_addr_list=[]
for i in range(len(lac_dict)):
    url="http://api.cellocation.com:81/cell/?mcc={0}&mnc={1}&lac={2}&ci={3}&output={4}&coord={5}".format(mcc,mnc,lac_dict[i],ci_dict[i],output,coord)
    res=requests.get(url=url)
    print(res)
    js=json.loads(res.text)
    if js['errcode']==10001:
        new_lat=new_lng=new_addr=''
    elif js['errcode']==0:
        new_lat=js['lat']
        new_lng=js['lon']
        new_addr=js['address']
    new_lat_list.append(new_lat)
    new_lng_list.append(new_lng)
    new_addr_list.append(new_addr)

df['new_lat']=new_lat_list
df['new_lng']=new_lng_list
df['new_addr']=new_addr_list
df.to_excel(r'基站数据爬取.xlsx')

