#coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
driver=webdriver.Firefox()
city_list="650100,650200,650400,650500,652300,652700,652800,652900,653000,653100,653200,654000,654200,654300".split(',')
for city in city_list:
    url="http://ip.bczs.net/city/{0}".format(city)
    # url="http://ip.bczs.net/city/650100"
    driver.get(url)
    ip_str=driver.find_element_by_xpath("//*[@id='result']/div/table/tbody").text
    ip_str=ip_str.split('\n')
    print(ip_str)
    cidr_list=[]
    driver.get("https://www.sioe.cn/xinqing/CIDR.php")
    Select(driver.find_element_by_xpath('//*[@id="qh4"]')).select_by_visible_text('IP地址范围')
    for ip in ip_str:
        ip1=ip.split(' ')
        print(ip1)
        start_ip=ip1[0]
        end_ip=ip1[1]
        # driver.get("https://www.sioe.cn/xinqing/CIDR.php")
        # Select(driver.find_element_by_xpath('//*[@id="qh4"]')).select_by_visible_text('IP地址范围')
        driver.find_element_by_xpath('//*[@id="a14"]').clear()
        driver.find_element_by_xpath('//*[@id="a14"]').send_keys(start_ip)
        driver.find_element_by_xpath('//*[@id="a24"]').clear()
        driver.find_element_by_xpath('//*[@id="a24"]').send_keys(end_ip)
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/p[2]/input').click()
        time.sleep(1)
        res=driver.find_element_by_xpath('//*[@id="event"]').text
        res_list=res.split('\n')[0]
        qz=res_list.split('：')[1]
        cidr=start_ip+'/'+qz
        cidr_list.append(cidr)

        print(cidr)
    df=pd.DataFrame(columns=['cidr'])
    df['cidr']=cidr_list
    df.to_excel(city+'.xlsx')
    pass
    # print(ip_str)
    # end_ip=driver.find_element_by_xpath('//*[@id="result"]/div/table/tbody/tr[1]/td[2]')
    #     print(start_ip)


