import json
import requests
import urllib.parse
def get_boundary(key_word,city):
    # param={
    #     "query":key_word,
    #     "tag":tag,
    #     "region":city,
    #     "output":"json",
    #     "coord_type":3,
    #     "page_size":1,
    #     "ak":"sEtYdhBIhgomgTGOkGOea2QOCd05uxr4"
    # }

    # api_url='http://api.map.baidu.com/place/v2/search?'
    session=requests.session()
    gd_param={
         "keywords": key_word,
         "city": city,
         "output": "json",
         "offset": 1,
         "page": 1,
         "key": "f69a0c4146782da8ca2745bd4c8508e9",
         "extensions":"all"

    }
    gd_api='https://restapi.amap.com/v3/place/text?'
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63",


    }
    cookie='UM_distinctid=173a321ccf48a1-047f363d2825fe-5d371947-1fa400-173a321ccf58ee; _ga=GA1.2.1444731394.1596169768; cna=TakTF0Xf21wCAX1QpeDZEzJp; _uab_collina=159616976993440040198753; passport_login=MTI5NzQxODI2LGFtYXBfMTU1MjMyNzA5MjZCRVZFU296RDgsZmttNGJscHlvZXQyYXkyNmt3M2w2aWxodTZxNXFta3AsMTU5ODMyNDEzNSxZekE0WVdWaE1XRmtNbVV6T0RobE9XWTVObVEzTURkbU5Ua3dOelkzTWpBPQ%3D%3D; dev_help=aPgS5uF05LWSvyrEf4ZuUjY5ZTAzNTk5OGFlZTVmODczNzEyZTUwYTQ5MmVkYWZjNTFhODJiYjhmMjc0YjlhYWE3NzZiZWY0NTk2MzkzNGZuh7EC3B9cZ8JbqQK4HIrpYBCoZqDhQ%2BXJlX1KNjTyTLZu%2BSsWEUP2w9PyfX09tSdtmoad%2FBFwly2DMmXOxVnqFOTwjHMPEjy2vfHTZsEqYAN9TTkD1u3h%2FLf0PHyfdHrJMaO%2BVb%2BqlL0QpLyUgZbS; xlly_s=1; guid=ae82-3f0c-afee-c9bd; x-csrf-token=586d0e17c4dca839ed53479ae66a00bd; CNZZDATA1255626299=6242382-1596166942-https%253A%252F%252Fwww.google.com%252F%7C1598400486; tfstk=cC85BP0gd82W6poUzQGVLeEI_XWCauN1O06kN3w-uDg8fSYhHsV37O14ZH2dXXff.; l=eBjxM_YROxfXrp4wBO5ahurza77OwpRflhVzaNbMiInca6QAvU7TUNQ4NFzHBdtjgtffGFtPC8EqeRe2-C4dg1MOYg6ihf2XTxJ6-; isg=BOrqYCmiQeAvvc1qOjqO0yHeO1CMW261hBKzWnStKD3Ip4BhWOqTxR2RN9O7fOZN'
    cookie_dic={i.split('=')[0]:i.split('=')[-1] for i in cookie.split(';')}
    res=session.get(url=gd_api,params=gd_param,headers=header,cookies=cookie_dic)
    # referer_url='https://www.amap.com/search?query={0}&city={1}'.format(key_word,city)
    # referer_url=urllib.parse.quote('https://www.amap.com/search?query=定陵机场&city=110000')
    # print(res.text)
    pass
    # header['Referer']=referer_url
    uid=json.loads(res.text)['pois'][0]['id']
    boundary_url='https://www.amap.com/detail/get/detail?id={0}'.format(uid)
    boundary_res=session.get(url=boundary_url,headers=header)
    print(boundary_res.text)
    original_crd=json.loads(boundary_res.text)['data']['spec']['mining_shape']['shape']
    temp=original_crd.split('|')[2][2:-1].split(',')
    original_crd_list=original_crd.split(';')
    crd_res_list=[]
    for i in range(0,len(original_crd_list),50):
        s=';'.join(original_crd_list[i:i+50])

        conversion_url='http://api.map.baidu.com/geoconv/v1/?coords={0}&from=6&to=5&ak=LyIM4GPhDU9cMnA6G3sBW4GDrdMock64'.format(s)
        conversion_res=requests.get(conversion_url,headers=header)
        zb=json.loads(conversion_res.text)

        for i in zb['result']:
            crd_res_list.append(str(i['x'])+','+str(i['y']))
    boundary='\n'.join(crd_res_list)
    print(boundary)

    return boundary
if __name__=='__main__':
    # d={'北京市': ['北京首都国际机场', '北京大兴国际机场', '北京南苑机场(已关闭)', '北京海淀机场', '定陵机场', '北京首都国际机场3号航站楼C区', '北京八达岭机场', '北京平谷金海湖机场', '北京密云穆家峪机场', '北京首都国际机场3号航站楼D区', '北京首都国际机场3号航站楼E区']}
    # for i in d.keys():
    get_boundary('重庆黔江武陵山机场','重庆市')