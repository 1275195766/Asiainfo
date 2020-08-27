#coding:utf-8
import os
def boundary_transfor(temp_path,save_path):
    with open(temp_path,'r',encoding='utf-8') as f:
        lines=f.readlines()
    lng_lat_list=[]
    # lines=zb_temp.split('\n')
    for line in lines:

        line_list=line.split(',')
        if line_list[2]=='0':
            line_list[1]+='\n'
            lng_lat_list.append(line_list[:2])

        else:
            # line_list[3] += '\n'
            lng_lat_list.append(line_list)
    s=''
    for i in lng_lat_list:
        s+=','.join(i)

    res_path = os.path.join(os.getcwd(), 'result' )
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    res_path=os.path.join(res_path,'{0}.csv'.format(save_path))
    with open(res_path,'w') as f1:
        f1.write(s)
    return s

if __name__=="__main__":
    boundary_transfor()