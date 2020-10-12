import pandas as pd

df=pd.read_excel(r'D:\文档\亚信实习\5A景区数据@20200916(456).xlsx',sheet_name='202004')
l=[
465241708,
465241688,
465241668,
465241648,
465241628,
465241608,
465241588,
465241568,
465241548,
465241528,
465241508,
465241488,
465241468
]
# Index(['渠道ID', '景区名称', '用户数', '省内', '省外'], dtype='object')
# res=[]

for i in l:
    try:
        res=df.loc[df.渠道ID==i].values[0]

        # print(res)
        for j in res:
            print(j,end=' ')
            # print(j,end=' ')
            # print(j,end=' ')
            # print(j,end=' ')
            # print(j,end=' ')
        print()
    except BaseException as e :
        print(i)

pass
