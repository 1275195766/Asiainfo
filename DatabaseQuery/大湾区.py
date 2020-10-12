import psycopg2
import pandas as pd
conn = psycopg2.connect(database="yx_test", user="postgres", password="123456", host="121.89.179.247", port="5432")
prov_list=["广州","深圳","珠海","佛山","惠州","东莞","中山","江门","肇庆"]
null_list=[]
cz_chnnel_id=[]
def select(prov,subtype):
    sql = "select id,channel_name,channel_subtype from channel_info_clear where channel_name like '%{0}%' and channel_subtype='{1}';".format(prov,subtype)
    print(sql)
    cur.execute(sql)
    rows = cur.fetchall()
    if rows == []:
        null_list.append([prov,subtype])
        return rows

    else:
        return rows

if conn is not None:
    print ("Opened database successfully")
    cur = conn.cursor()
    for prov in prov_list:
        czrows=select(prov,'火车站')
        for row in czrows:
            cz_chnnel_id.append(row)
        jcrows=select(prov,'机场')
        for row in jcrows:
            cz_chnnel_id.append(row)
    print(null_list)
    df=pd.DataFrame(cz_chnnel_id,columns=['id','channel_name','channel_subtype'])
    df.to_excel(r'F:\pythonPrj\Asiainfo\DatabaseQuery\result\大湾区火车站机场id.xlsx',index=None)
    pass