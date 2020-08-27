#coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
url="http://117.132.182.230:18080/iopbj/"
# url="http://localhost:63342/Asiainfo/iop%E5%8C%BA%E5%9F%9F%E8%BE%B9%E7%95%8C/test.html"
driver.get(url)

driver.find_element_by_xpath("//input[@name='username']").send_keys('yujiang')
driver.find_element_by_xpath("//input[@name='pwd2']").send_keys('bajyie123!')
driver.find_element_by_xpath("//input[@type='image']").click()

# Select(driver.find_element_by_xpath("//select[@id='regform_queryCountyName']")).select_by_visible_text('重庆市')
# Select(driver.find_element_by_xpath("//select[@id='regform_querySubTypeName']")).select_by_visible_text('行政区划')
# driver.find_element_by_xpath("//input[@id='regform_0']").click()

driver.get('http://117.132.182.230:18080/iopbj/toNewChannelInfo.action')
sheng='湖北省'

id='465207568'
Select(driver.find_element_by_xpath("//select[@id='regform_countyName']")).select_by_visible_text(sheng)
time.sleep(1)
Select(driver.find_element_by_xpath("//select[@id='regform_channelSubtype']")).select_by_visible_text('行政区划')
time.sleep(1)
driver.find_element_by_xpath("//input[@id='regform_parentChannelId']").send_keys(id)
time.sleep(1)
with open(r'D:\文档\亚信实习\工作\iop\地区.txt') as f:
    lines=f.readline().split(',')
    shi=lines[0]
    del lines[0]
    for qu in lines:
        print(qu)
        driver.find_element_by_xpath("//input[@name='channelName']").send_keys("{0}_{1}_{2}".format(sheng,shi,qu))
        time.sleep(1)
        driver.find_element_by_xpath("//input[@id='regform_0']").click()
        time.sleep(2)
        driver.back()
        driver.find_element_by_xpath("//input[@name='channelName']").clear()

        time.sleep(2)

driver.quit()