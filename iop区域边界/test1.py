import json
import pandas as pd

with open(r'F:\pythonPrj\Asiainfo\iop区域边界\重点城市园区范围\117食品重庆涪陵工业园区.geojson', 'r') as f:
    res = f.read()

res_json = json.loads(res)
n = 0
l = []
for feature in res_json['features']:
    for i in feature['geometry']['coordinates'][0]:
        i.append(n)
        # s=','.join(i)
        l.append(i)
    n += 1

df = pd.DataFrame(l)
s = df.to_string(header=None, index=None).replace('  ', ',')
print(s)