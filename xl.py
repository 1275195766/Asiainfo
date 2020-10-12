import pandas as pd

df=pd.read_excel(r'xl.xlsx',converters={'省级行政区':str,"channel_id":str,
                                        # "小学及以下":str,"初高中":str,"专本":str,"研究生及以上":str
                                        })
# df=df.applymap(lambda x :'%.2f%%'  %  (x*100))
pv='北京市,天津市,河北省,山西省,内蒙古自治区,辽宁省,吉林省,黑龙江省,上海市,江苏省,浙江省,安徽省,福建省,江西省,山东省,河南省,湖北省,湖南省,广东省,广西壮族自治区,海南省,重庆市,四川省,贵州省,云南省,西藏自治区,陕西省,甘肃省,青海省,宁夏回族自治区,新疆维吾尔自治区'.split(',')
i=0
for p in pv:
    s=p
    print(p)
    ch=df.loc[df.省级行政区==p,'channel_id'][i]
    print(ch)
    # xl=df.loc[df.省级行政区==p,'小学及以下'][1]
    # print(type(xl))
    # xl=
    # print('{0:0.2%}'.format(df.loc[df.省级行政区==p,'小学及以下'][1]))
    s+=','+str(ch)+',学历,'+'小学及以下'+','+'{0:0.2%}'.format(df.loc[df.省级行政区==p,'小学及以下'][i])+'\n'+p
    s+=','+str(ch)+',学历,'+'初高中'+','+'{0:0.2%}'.format(df.loc[df.省级行政区==p,'初高中'][i])+'\n'+p
    s+=','+str(ch)+',学历,'+'专本'+','+'{0:0.2%}'.format(df.loc[df.省级行政区==p,'专本'][i])+'\n'+p
    s+=','+str(ch)+',学历,'+'研究生及以上'+','+'{0:0.2%}'.format(df.loc[df.省级行政区==p,'研究生及以上'][i])+'\n'



    with open(r'xl.txt','a') as f :
        f.write(s)
    # s=''
    i+=1
pass
