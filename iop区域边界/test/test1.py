
for i in range(6,23):
    s = '202009'
    if i <10:
        s+='0'+str(i)
    else:
        s+=str(i)
    s1='hdfs dfs -mv /user/zh2_huawei_yybxyuser/other_data_obc/C_guoman/i_70011_{0}_32052_00_001.dat /user/zh2_huawei_yybxyuser/other_data_obc/D_32052_14day_manchu/i_70011_{0}_32052_00_001.dat'.format(s)
    print(s1)