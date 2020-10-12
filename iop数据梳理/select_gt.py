import psycopg2
with open(r'result/高铁channel_id.txt', 'r') as f:
    gt_id=f.readlines()

name=[]

conn = psycopg2.connect(database="yx_test", user="postgres", password="123456", host="121.89.179.247", port="5432")
if conn is not None:
    print(conn)
    print ("Opened database successfully")
    cur = conn.cursor()
    for gt in gt_id:

        select_sql="select id,channel_name,telno,channel_subtype from channel_info where id={0}".format(gt[:-1])
        # print(select_sql)
        cur.execute(select_sql)


        rows = cur.fetchall()
        print(rows[0][1])