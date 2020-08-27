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
        uid=json.loads(res.text)['results'][0]['uid']
        boundary_url='https://map.baidu.com/?uid={0}&ugc_type=3&ugc_ver=1&qt=detailConInfo&device_ratio=1&compat=1&t=1598253753780&auth=%40dDDT8gaM9K16734SbH%40VEG%3DM9233D5CuxHTRzHBNHBtzljPyBYYxy1uVt1GgvPUDZYOYIZuBtGfyMx7w4kkfkD%3DCPWv3GuzztQZ3wWvUvhgMZSguxzBEHLNRTVtlEeLZNz1%40Db17dDFC8zv7u%40ZPuVteuxxtoqFmqE25%3DZI5I3251swVVH3W2GllhIMX'.format(uid)
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
    get_boundary('上海金山水上机场','上海市')
