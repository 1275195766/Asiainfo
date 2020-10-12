import requests

def Conversion(string):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63",
    }
    original_crd_list=string.split(';')
    crd_res_list=[]
    for i in range(0,len(original_crd_list),50):
        s=';'.join(original_crd_list[i:i+50])

        conversion_url='http://api.map.baidu.com/geoconv/v1/?coords={0}&from=3&to=5&ak=LyIM4GPhDU9cMnA6G3sBW4GDrdMock64'.format(s)
        conversion_res=requests.get(conversion_url,headers=header).json()
        # zb=json.loads(conversion_res.text)

        for i in conversion_res['result']:
            crd_res_list.append(str(i['x'])+','+str(i['y']))
    boundary='\n'.join(crd_res_list)
    print(boundary)


if __name__=="__main__":
    s="13069163.23,6347767.72"
    Conversion(s)