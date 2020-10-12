import pandas as pd
import psycopg2

df=pd.read_excel(r'D:\文档\亚信实习\工作\iop\火车站\火车站上级行政区.xlsx')
# Index(['id', 'channel_name', '省', '站', 'province', 'city', 'area'], dtype='object')

conn = psycopg2.connect(database="yx_test", user="postgres", password="123456", host="121.89.179.247", port="5432")
null_list=[]
if conn is not None:
    # print(conn)
    print ("Opened database successfully")
    cur = conn.cursor()
    for i in df.loc[df['area'].isna()==False].values:
        # print(i)

        select_sql="select id,channel_name,telno,channel_subtype from channel_info where channel_name like '%{0}%{1}%';".format(i[5][:-1],i[6][:-1])
        print(select_sql)
        cur.execute(select_sql)
        rows = cur.fetchall()
        if rows == []:
            null_list.append(i[4:])
        else:
            df.loc[df.id==i[0],'parent_id']=rows[0][0]
    for n in null_list:
        print(n)
    df.to_excel(r'D:\文档\亚信实习\工作\iop\火车站\火车站上级行政区(parent_id).xlsx',index=None)
    print('完成')
        # pass


pass