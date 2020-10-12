import time

import requests
import json
import pandas as pd
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re
from  iop区域边界 import iopboundary
errro_list=[]
area_dic={}
provid_dic={
"重庆市":"465296153",
"河北省":"465296178",
"山西省":"465296179",
"辽宁省":"465296172",
"吉林省":"465296164",
"黑龙江省":"465296156",
"江苏省":"465296176 ",
"浙江省":"465296171",
"安徽省":"465296169",
"福建省":"465296157",
"江西省":"465296161",
"山东省":"465296173",
"河南省":"465296150",
"湖北省":"465296165",
"湖南省":"465296152",
"广东省":"465296174",
"海南省":"465296151",
"四川省":"465296170",
"贵州省":"465296166",
"云南省":"465296159",
"陕西省":"465296162",
"甘肃省":"465296148",
"青海省":"465296154",
"台湾省":"465296155",
"内蒙古自治区":"465296177",
"广西省":"465296175",
"西藏自治区":"465296167",
"宁夏回族自治区":"465296160",
"新疆维吾尔自治区":"465296149"
}
base_path=r'F:\pythonPrj\Asiainfo\iop区域边界\重点城市园区范围'
gyyq_excel=pd.read_excel(r'D:\文档\亚信实习\工作\iop\工业园区基站圈选.xlsx')

file_list=os.listdir(base_path)

def get_prov(yq_name):
    url = 'https://restapi.amap.com/v3/place/text?'
    param = {
        'keywords': yq_name,
        'children': 0,
        'offset': 1,
        'page': 1,
        'extensions': 'base',
        'key':'f69a0c4146782da8ca2745bd4c8508e9'
    }
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
    prov_res=requests.get(url,params=param,headers=header)
    prov_json=json.loads(prov_res.text)
    prov=prov_json['pois'][0]['pname']
    return prov
    pass

def Drawborder(id,driver,boundary):

    # id = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]").text
    # boundary_url = "http://117.132.182.230:18080/iopbj/ImportAreaPolygon.jsp?id={0}".format(id)

    # addrs_list=self.shi+self.qu
    try:
        import_url="http://117.132.182.230:18080/iopbj/ImportAreaPolygon.jsp?id={0}".format(id)
        driver.get(import_url)
        time.sleep(1)
        # boundary=getpoiboundary.get_boundary(key_word, city)
        if boundary==0:
            exit()
        #输入坐标
        driver.find_element_by_xpath("//textarea[@id='regform3_cellData']").send_keys(boundary)
        time.sleep(0.2)
        Select(driver.find_element_by_xpath("//select[@name='importCoordinateType']")).select_by_visible_text('DB9')
        time.sleep(0.2)
        driver.find_element_by_xpath("//input[@id='regform3_0']").click()
        time.sleep(0.2)
        driver.switch_to.alert.accept()
        # time.sleep(3)
        # driver.execute_script("document.body.style.zoom='0.2'")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='regform1']/input[10]").click()
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(1)
    except BaseException as e :
        print(e)


def create_area(prov,area_name,s,driver):

    # 换成自己构造的字典
    # name_dic=Getairtportname.airport()

    try:

        # 进入新建界面
        driver.get(
            'http://117.132.182.230:18080/iopbj/toNewChannelInfo.action?countyName=-&queryTypeName=&querySubTypeName=')
        # 选择省
        Select(driver.find_element_by_xpath('//*[@id="regform_countyName"]')).select_by_visible_text(prov)
        time.sleep(0.3)
        # 选择地区子类型
        Select(driver.find_element_by_xpath('//*[@id="regform_channelSubtype"]')).select_by_visible_text('产业园区')
        time.sleep(0.3)
        # 输入地区名称
        driver.find_element_by_xpath('//*[@id="regform_channelName"]').send_keys(area_name)
        time.sleep(0.5)
        #输入cellID

        driver.find_element_by_xpath('//*[@id="regform_parentChannelId"]').send_keys(provid_dic[prov])
        # 新建
        driver.find_element_by_xpath('//*[@id="regform_0"]').click()
        time.sleep(3)  # driver.back()
        try:
            # 获取id
            boundary_url = driver.find_element_by_xpath(
                '//*[@id="regform"]/table/tbody/tr[9]/td[2]/a').get_attribute('href')
            id = re.search(r'.*channelId=(.*)', boundary_url).group(1)
            time.sleep(1)
            # driver.back()
            print('id:', id)
            area_dic[area_name]=id
            # 画边界
            Drawborder(id,driver,s)
        except BaseException as e:
            errro_list.append(area_name)
            print(e)
        pass
    except BaseException as e:
        print(e)

driver = webdriver.Firefox()
driver.set_window_size(950, 1030)
url = "http://117.132.182.230:18080/iopbj/"
driver.get(url)

driver.find_element_by_xpath("//input[@name='username']").send_keys('yujiang')
driver.find_element_by_xpath("//input[@name='pwd2']").send_keys('bajyie123!')
driver.find_element_by_xpath("//input[@type='image']").click()
yzm = input("请输入验证码：")

driver.find_element_by_xpath('//*[@id="regform"]/div[1]/p/input[1]').send_keys(yzm)
driver.find_element_by_xpath('//*[@id="regform"]/div[2]/input').click()
time.sleep(1)

for file in file_list:
    file_name=os.path.splitext(file)
    yq_name=gyyq_excel.loc[gyyq_excel['文件名称']==file_name[0],'园区名称'].to_list()[0]
    area_dic[yq_name]=''
    prov=get_prov(yq_name)
    path=os.path.join(base_path,file)

    with open(path,'r') as f:
        res=f.read()

    res_json=json.loads(res)
    n=0
    l=[]
    for feature in res_json['features']:
        for i in feature['geometry']['coordinates'][0]:
            i.append(n)
            # s=','.join(i)
            l.append(i)
        n+=1

    df=pd.DataFrame(l)
    s=df.to_string(header=None,index=None).replace('  ',',')




    create_area(prov,area_name=yq_name,s=s,driver=driver)

    # print(s)
    # df.to_csv(r'F:\pythonPrj\Asiainfo\iop区域边界\园区res\{0}'.format(file),header=None,index=None)
    pass
print(errro_list)
print(area_dic)