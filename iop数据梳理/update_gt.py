import psycopg2

# with open(r'result/动车channel_id.txt', 'r') as f:
#     dc_id=f.readlines()
dc_id=[465296535,465296373,465296372,465296181,465296544,465296181,465296181,465296408,465296176,465296408,465296181,465296148,465296181,465296223,465296411]

id=[465296804,465298720,465298536,465298385,465299485,465298983,465298385,465299515,465296459,465297019,465296623,465296273,465297783	,465299406,465297002]



null_list=[]
gt_chnnel_id=[]
update_sql_list=[]
conn = psycopg2.connect(database="yx_test", user="postgres", password="123456", host="121.89.179.247", port="5432")
if conn is not None:
    print(conn)
    print ("Opened database successfully")
    cur = conn.cursor()
    for gt in range(len(dc_id)):
        # select_sql="select id,channel_name,parent_channel_id,channel_subtype from channel_info where id={0}".format(id[gt])
        update_sql="update channel_info set parent_channel_id={0} where id={1}".format(dc_id[gt],id[gt])
        # update_sql_list.append(update_sql+';')

        print(update_sql+';')

        # cur.execute(update_sql)
        #
        # select_sql="select id,channel_name,telno,channel_subtype from channel_info where id={0}".format(gt[:-1])
        # print(select_sql)
        # cur.execute(select_sql)
        #
        # rows = cur.fetchall()
        # print(rows[0][2])
        # if rows==[]:
        #     null_list.append(gt[:-1])
        #     # print(gt[:-1])
        # else:
        #     print(rows[0])
        #     gt_chnnel_id.append(rows[0][0])
            # print(rows)
        pass
    for i in update_sql_list:
        print(i)

    # print(null_list)

    # for g in gt_chnnel_id:
    #     print(g)