#coding:utf-8
import time

from selenium import webdriver
import os

# driver = webdriver.Firefox()
#
# url="http://localhost:63342/Asiainfo/iop%E5%8C%BA%E5%9F%9F%E8%BE%B9%E7%95%8C/test.html"
# driver.get(url)
# sheng='河北省'
# shi='承德市'
# qu='兴隆县'
# # 河北省承德市兴隆县
# driver.find_element_by_xpath("//body/input[@id='districtName']").send_keys('{0}{1}{2}'.format(sheng,shi,qu))
# # time.sleep(1)
# driver.find_element_by_xpath("/html/body/input[2]").click()
#
# driver.find_element_by_xpath("/html/body/input[2]").click()
# res=driver.find_element_by_xpath("//textarea[@id='Div1']")
# s=res.text
with open(r'D:\文档\亚信实习\工作\iop\zb.txt','r') as f:
    s=f.read()
    print(s)
    l=s.split(';')
    l1=[n.split(',') for n in l]
    print(l1)

list=[]
list1=[]
with open("zb.txt",'a+') as z:

    for i in range(len(l1)):
        w=','.join(l1[i])
        z.write(w)
        z.write('\n')
        if len(l1[i])==2:
            list.append(l1[i])
        else:
            print(len(l1[i]))
            print(True)

            list1.append(l1[i][2:])
            temp =l1[i]


            # else:
            #     print(False)


pass
# driver.close()