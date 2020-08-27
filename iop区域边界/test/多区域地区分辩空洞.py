# coding=utf-8

#获取修正的坐标表,分组的表（a,b）、（b,c）...,分组数
def getZbAndIndex_lis(inputpath):
    zb = open(inputpath,'r').read()
    zb_l = zb.split('\n')

    zb_index = [0,-1]
    n = 0
    for index,i in enumerate(zb_l):
        if len(i.split(",")) > 2:
            n += 1
            i_s=i.split(',')
            zb_l[index] = i_s[0]+','+i_s[1]
            zb_l.insert(index+n,i_s[2]+','+i_s[3])
            zb_index.insert(n,index)  #第一组的最后一个元素下标
    for aa in range(len(zb_l)):
        zb_l[aa] =  zb_l[aa].replace(' ','')

    return zb_l,zb_index,n+1  #坐标表,分组的表（a,b）、（b,c）...,分组数

# def getMaxMin(tmp):
#     #各个分块的经纬度的最大值和最小值，经度lon,纬度lat
#     max_min = {'len':[],
#                'max':{'lon':[],'lat':[]},
#                'min':{'lon':[],'lat':[]}
#                }
#
#     for t in tmp:
#         lon=[]
#         lat=[]
#         max_min['len'].append(len(t))
#         for t_1 in t:
#             t_s = t_1.split(",")
#             lon.append(t_s[0])
#             lat.append(t_s[1])
#         max_min['max']['lon'].append(max(lon))
#         max_min['max']['lat'].append(max(lat))
#         max_min['min']['lon'].append(min(lon))
#         max_min['min']['lat'].append(min(lat))
#     return max_min

def getFenkuai(shuju,index,n):
    num=0
    tmp = []
    while num < n:
        tmp.append(shuju[index[num]:index[num+1]])
        num += 1
    return tmp

def rayCasting(p, poly):
    px = p['x']
    py = p['y']
    flag = False

    i = 0
    l = len(poly)
    j = l - 1
    # for(i = 0, l = poly.length, j = l - 1; i < l; j = i, i++):
    while i < l:
        sx = poly[i]['x']
        sy = poly[i]['y']
        tx = poly[j]['x']
        ty = poly[j]['y']

        # 点与多边形顶点重合
        if (sx == px and sy == py) or (tx == px and ty == py):
            return 'on'

        # 点在边上
        # if (ty-py)/(tx-px) == (py-sy)/(px-sx):
        #     return 'on'


        # 判断线段两端点是否在射线两侧
        if (sy < py and ty >= py) or (sy >= py and ty < py):
            # 线段上与射线 Y 坐标相同的点的 X 坐标
            x = sx + (py - sy) * (tx - sx) / (ty - sy)   #(py-sy)/(ty-sy)  比例 算x
            # 点在多边形的边上
            if x == px:
                return 'on'
            # 射线穿过多边形的边界   如果在外面，不管怎么样都会是偶数；如果在里面，无论怎样都会是奇数，不会差那几个反方向的交点。
            if x > px:
                flag = not flag
        j = i
        i += 1

    # 射线穿过多边形边界的次数为奇数时点在多边形内
    return 'in' if flag else 'out'

# 得到点的坐标
def getpoint(lis):
    jihe = []
    for a in lis:
        jihe.append({'x': float(a.split(',')[0]), 'y': float(a.split(',')[1])})
    return jihe
    # i = 0
    # zhima = []
    # while i < len(a.split(',')[1::2]):
    #     zhima.append({'x': float(a.split(',')[::2][i]), 'y': float(a.split(',')[1::2][i])})
    #     i += 1
    # return zhima

# 点集与多边形顶点集进行运算
def get_p_poly_cnt(p_l,poly):
    cnt_in = 0
    cnt_on = 0
    cnt_out = 0
    for point in p_l:
        rs = rayCasting(point, poly)
        if rs == 'in':
            cnt_in += 1
        elif rs == 'on':
            cnt_on +=1
        else:
            cnt_out +=1
    return cnt_in,cnt_on,cnt_out


def get_kongdong(tmp):
    # tmp：[[],[],[]...]
    seq = tmp[:]
    length = len(seq)   #test : 3
    # i = j = 0
    # flag = 1
    # while i < length:
    #     j = 0
    #     while j < length - i:
    #         # 主体
    #
    #         j += 1
    #     if flag:
    #         break
    #     i += 1
    i_j = ''
    f = []
    for i in range(0,length):
        for j in range(i+1,length):

            i_j = ''
            # a作点的集，b作多边形
            p1_l = seq[i]
            poly1= seq[j]
            p_a = getpoint(p1_l)
            poly_a = getpoint(poly1)
            a_in,a_on,a_out = get_p_poly_cnt(p_a,poly_a)

            # b作点的集，a作多边形
            p2_l = seq[j]
            poly2 = seq[i]
            p_b = getpoint(p2_l)
            poly_b = getpoint(poly2)
            b_in, b_on, b_out = get_p_poly_cnt(p_b, poly_b)


            # a在b外，b不在a外（a包含b）
            if a_out>4 and b_in>3:
                if j not in f:
                    f.append(j)
                # print('a包含b')
            # b在a外，a不在b外（b包含a）
            elif b_out>4 and a_in >3 and i != 0:
                if i not in f:
                    f.append(i)
                # print('b包含a')
    return f



dq_l = open('C:/Users/b1683/Desktop/边界/多区域.txt','r').read()
dq_l = dq_l.split(' ')
for dq in dq_l:
    print('\n')
    print("开始："+dq)
    print("..................................................................")
    inputpath = "C:/Users/b1683/Desktop/边界/多区域/" + dq + ".txt"
    outpath = "C:/Users/b1683/Desktop/多区域修正/" + dq + ".txt"

    zb_l,zb_index,n = getZbAndIndex_lis(inputpath)
    #print(zb_l,zb_index,n)

    tmp = getFenkuai(zb_l,zb_index,n)
    # print(tmp)

    #max_min = getMaxMin(tmp)    #长度 max：lon\lat,min:lon\lat
    #print(max_min)

    kd = get_kongdong(tmp)  # 空洞地块的：[索引,索引,...]
    # print(kd)

    #拆分
    kuai = 0
    zbs = []
    for t in tmp:
        for t_1 in t:
            t_1= t_1+","+str(kuai)
            if kuai in kd:
                t_1 = t_1+",I"
            zbs.append(t_1)
        kuai +=1
    # if kd != []:
    #print(zbs)


    #写入文件
    open(outpath,'w').write('\n'.join(zbs))
    #print(zb_l)
    print("完成："+dq)

