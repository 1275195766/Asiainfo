import json
import requests
def get_boundary(key_word,city):
    param={
        "query":key_word,
        "tag":"机场",
        "region":city,
        "output":"json",
        "coord_type":3,
        "page_size":1,
        "ak":"sEtYdhBIhgomgTGOkGOea2QOCd05uxr4"
    }
    api_url='http://api.map.baidu.com/place/v2/search?'
    header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63"}
    res=requests.get(url=api_url,params=param,headers=header)
    # print(res.text)
    try:
        # boundary_param={
        #
        # }
        uid=json.loads(res.text)['results'][0]['uid']
        boundary_url='https://map.baidu.com/?uid={0}&qt=detailConInfo&compat=1&auth=EabZWQe=FFYV@LCKKAwS020EvJzvGYGPuxHTTNxRVRRtfy9GUIsxAwwi04vy77u1GgvPUDZYOYIZuVt1cv3uVtGccZcuVtPWv3GuztQZ3wWvUvhgMZSguxzBEHLNRTVtcEWe1GD8zv7u@ZPuVteuxtf0wd0vyIUUOyS7CCuquTTGVFxcc@AZ'.format(uid)
        boundary_res=requests.get(url=boundary_url,headers=header)
        # print(boundary_res.text)
        # if 'ext' not in boundary_res.text:
        #     return 0
        original_crd=json.loads(boundary_res.text)['content']['ext']['detail_info']['guoke_geo']['geo']

        temp=original_crd.split('|')[2][2:-1].split(',')
        original_crd_list=[str(temp[i])+','+str(temp[i+1]) for i  in range(0,len(temp),2)]
        crd_res_list=[]
        for i in range(0,len(original_crd_list),50):
            s=';'.join(original_crd_list[i:i+50])

            conversion_url='http://api.map.baidu.com/geoconv/v1/?coords={0}&from=6&to=5&ak=LyIM4GPhDU9cMnA6G3sBW4GDrdMock64'.format(s)
            conversion_res=requests.get(conversion_url,headers=header)
            zb=json.loads(conversion_res.text)

            for i in zb['result']:
                crd_res_list.append(str(i['x'])+','+str(i['y']))
        boundary = '\n'.join(crd_res_list)
        print(city)
        print(boundary)

        return boundary
    except BaseException as e :
        print(e)
if __name__=='__main__':
    get_boundary('呼伦贝尔市满洲里市中俄边境旅游区','内蒙古自治区')
