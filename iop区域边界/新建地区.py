#coding:utf-8
import time
from  iop区域边界 import Getairtportname,iopboundary
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import re

driver = webdriver.Firefox()
driver.set_window_size(950, 1030)
url="http://117.132.182.230:18080/iopbj/"
driver.get(url)

driver.find_element_by_xpath("//input[@name='username']").send_keys('yujiang')
driver.find_element_by_xpath("//input[@name='pwd2']").send_keys('bajyie123!')
driver.find_element_by_xpath("//input[@type='image']").click()
yzm=input("请输入验证码：")

driver.find_element_by_xpath('//*[@id="regform"]/div[1]/p/input[1]').send_keys(yzm)
driver.find_element_by_xpath('//*[@id="regform"]/div[2]/input').click()
time.sleep(1)



#换成自己构造的字典
# name_dic=Getairtportname.airport()
name_dic={'北京市': ['定陵机场',  '北京平谷金海湖机场', '北京密云穆家峪机场'], '天津市': ['天津滨海窦庄通用机场'], '上海市': ['上海金山水上机场'], '重庆市': ['重庆黔江武陵山机场', '重庆巫山机场', '永川大安通用机场'], '河北省': ['邯郸机场', '河北迁安五重安机场',  '唐山三女河机场', '秦皇岛北戴河国际机场'], '辽宁省': ['大连国际机场',  '新开河通用机场', '法库财湖机场'], '吉林省': [ '长春龙嘉国际机场', '白山长白山机场', '松原查干湖机场'], '黑龙江省': ['加格达奇机场', '漠河古莲机场', '哈尔滨太平国际机场', '佳木斯东郊机场', '牡丹江海浪机场', '齐齐哈尔三家子机场', '黑河瑷珲机场', '伊春林都机场',  '抚远东极机场', '鸡西兴凯湖机场'], '甘肃省': [ '庆阳机场', '敦煌莫高国际机场', '陇南成县机场', '张掖甘州机场', '庆阳机场' ], '内蒙古自治区': ['阿拉善左旗机场', '包头东河机场', '赤峰玉龙机场', '集宁机场',  '巴彦淖尔天吉泰机场', '鄂尔多斯伊金霍洛国际机场'], '广西壮族自治区': ['柳州白莲机场', '百色巴马机场', '柳州白莲机场', '梧州西江机场'],  '宁夏回族自治区': ['中卫沙坡头机场', '固原六盘山机场'], '新疆维吾尔自治区': ['阿克苏机场', '阿勒泰机场', '和田机场', '克拉玛依机场', '且末玉都机场', '塔城机场', '新源那拉提机场', '若羌楼兰机场', '吐鲁番交河机场', '博乐阿拉山口机场', '库车龟兹机场', '石河子山丹湖通用航空机场', '布尔津喀纳斯机场']}
try:
    for key in name_dic.keys():

        for name in name_dic[key]:
            print(name)
            #进入新建界面
            driver.get('http://117.132.182.230:18080/iopbj/toNewChannelInfo.action?countyName=-&queryTypeName=&querySubTypeName=')
            #选择省
            Select(driver.find_element_by_xpath('//*[@id="regform_countyName"]')).select_by_visible_text(key)
            time.sleep(0.3)
            #选择地区子类型
            Select(driver.find_element_by_xpath('//*[@id="regform_channelSubtype"]')).select_by_visible_text('机场')
            time.sleep(0.3)
            #输入地区名称
            driver.find_element_by_xpath('//*[@id="regform_channelName"]').send_keys(key+"_{0}".format(name))
            time.sleep(0.5)
            #新建
            driver.find_element_by_xpath('//*[@id="regform_0"]').click()
            time.sleep(3)            # driver.back()
            try:
                #获取id
                boundary_url=driver.find_element_by_xpath('//*[@id="regform"]/table/tbody/tr[9]/td[2]/a').get_attribute('href')
                id=re.search(r'.*channelId=(.*)',boundary_url).group(1)
                time.sleep(1)
                # driver.back()
                print('id:',id)
                #画边界
                iopboundary.Drawborder(id,name,key,driver)
            except BaseException as e:
                print(e)
            pass
except BaseException as e :
    print(e)

driver.quit()