import pandas as pd
import re

df=pd.read_excel(r'old.xlsx',header=0,converters={'CARD_NO':str,"D_NAME":str})
df.fillna(0,inplace=True)
# df1=pd.DataFrame([],columns=['sheng','shi''xian'])
sheng=[]
shi=[]
xian=[]
for name in df.D_NAME:
    # print(name)
    if name !=0:
        cp=re.compile(r'(.*省)(.*地区)(.*)|(.*省)(.*?市)(.*)')
        res = cp.search(name)
        res = list(res.groups())
        for i in range(3):
            res.remove(None)
        print(res)

        sheng.append(res[0])
        shi.append(res[1])
        xian.append(res[2])




print(sheng)
df1=pd.DataFrame([sheng,shi,xian]).T
pass
print(df.D_NAME)