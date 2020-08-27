import requests
import json
import pprint

ak = "iHMauZIIRXPoHAaynTkb6P3xtH2i2Wld"
address = '重庆市'

url = 'http://api.map.baidu.com/place/v2/search?query=公园&region={0}&output=json&ak={1}'.format(address,ak)
print(url)
res = requests.get(url)
json_data = json.loads(res.text)
pprint.pprint(json_data)
lat = json_data['results'][0]['location']['lat']
lng = json_data['results'][0]['location']['lng']
print(lat,lng)
pass
