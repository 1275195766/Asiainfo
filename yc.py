import pandas as pd

df=pd.read_table('yc1.txt',sep='|',header=None,names=['id','channel_name','channel_id','op_time','people_count','roamin_cnt','resident_cnt','visiting_cnt','iot_cnt'],converters={'op_time':str},engine='python',encoding='utf-8')

d_list=df.op_time.to_list()
d_list1=[]
for i in d_list:
    d_list1.append(i[:8])

df['new_op_time']=d_list1
month=[31,28,31,30,31,30,31,31,30,31,30,31]
new_op_time=[]
for i in range(1,13):
    for d in range(1,month[i-1]+1):

        m = '0' + str(i) if i<10 else str(i)
        d1='0'+str(d) if d<10 else str(d)
        new_op_time.append('2019'+m+d1)
        pass

# df['new_op_time1']=new_op_time

res=df.pivot_table(index='new_op_time',columns='channel_name',values='people_count',aggfunc='mean').reset_index()
res1=pd.DataFrame(new_op_time,columns=["new_op_time"])
res2=pd.merge(res,res1,how='outer',on='new_op_time')
res2=res2.reset_index()
print(res)

pass