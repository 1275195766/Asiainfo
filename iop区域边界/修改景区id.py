import time

import requests
import json
# import pandas as pd
# import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re


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

provs=[

'江西省',
'山东省',
'河南省',
'湖北省',
'湖南省']
def get_prov(yq_name):
    url = 'https://restapi.amap.com/v3/place/text?'
    param = {
        'keywords': yq_name,
        'children': 2,
        'offset': 1,
        'page': 1,
        'extensions': 'base',
        'key':'f69a0c4146782da8ca2745bd4c8508e9'
    }
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"}
    prov_res=requests.get(url,params=param,headers=header)
    prov_json=json.loads(prov_res.text)
    prov=prov_json['pois'][0]['pname']
    city=prov_json['pois'][0]['cityname']
    adname=prov_json['pois'][0]['adname']

    return prov,city,adname

def search_aera(prov,area):
    Select(driver.find_element_by_xpath("//select[@id='regform_queryCountyName']")).select_by_visible_text(prov)
    Select(driver.find_element_by_xpath("//select[@id='regform_querySubTypeName']")).select_by_visible_text(area)
    driver.find_element_by_xpath("//input[@id='regform_queryByName']").clear()
    time.sleep(0.3)



for prov in provs:
    # 选择省份，行政区域
    search_aera(prov,'景区')
    driver.find_element_by_xpath("//input[@id='regform_0']").click()
    time.sleep(0.3)
    table=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table').text
    table_list=table.split('\n')
    add_names=[t.split(' ') for t in table_list]
    del add_names[0]
    for add_name in add_names:
        try:

            prov1,city,adname=get_prov(add_name[1])
            search_aera(prov,'行政区划')

            driver.find_element_by_xpath("//input[@id='regform_queryByName']").send_keys('{0}_{1}_{2}'.format(prov1, city, adname))
            driver.find_element_by_xpath("//input[@id='regform_0']").click()
            time.sleep(0.8)
            cell_id=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]').text
            search_aera(prov, '景区')
            time.sleep(1.5)
            driver.find_element_by_xpath("//input[@id='regform_queryByName']").send_keys(add_name[1])
            driver.find_element_by_xpath("//input[@id='regform_0']").click()
            time.sleep(0.3)
            xg_url=driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[9]/a[1]').get_attribute('href')
            driver.get(xg_url)
            time.sleep(0.3)
            driver.find_element_by_xpath('//*[@id="regform_parentChannelId"]').clear()
            driver.find_element_by_xpath('//*[@id="regform_parentChannelId"]').send_keys(cell_id)
            time.sleep(0.3)
            driver.find_element_by_xpath('//*[@id="regform_0"]').click()
            time.sleep(0.3)
            driver.get('http://117.132.182.230:18080/iopbj/ListChannelInfoAction.action')
        except BaseException as e:
            print(add_name[1])
            driver.get('http://117.132.182.230:18080/iopbj/ListChannelInfoAction.action')
    # print(table)
        pass
