#coding:utf-8
import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from iop区域边界 import Get_Region_Boundary


class bianjie():
    def __init__(self):
        self.sheng = '山东省'
        self.shi = '舟山市'
        self.qu = '定海区'

    def login(self,driver):

        url="http://117.132.182.230:18080/iopbj/"
        # url="http://localhost:63342/Asiainfo/iop%E5%8C%BA%E5%9F%9F%E8%BE%B9%E7%95%8C/test.html"
        driver.get(url)

        # 登录
        driver.find_element_by_xpath("//input[@name='username']").send_keys('yujiang')
        driver.find_element_by_xpath("//input[@name='pwd2']").send_keys('bajyie123!')
        driver.find_element_by_xpath("//input[@type='image']").click()
        time.sleep(1)
        yzm=input("请输入验证码：")
        driver.find_element_by_xpath('//*[@id="regform"]/div[1]/p/input[1]').send_keys(yzm)
        driver.find_element_by_xpath('//*[@id="regform"]/div[2]/input').click()
        pass

    def search(self,driver):

        #选择省份，行政区域
        Select(driver.find_element_by_xpath("//select[@id='regform_queryCountyName']")).select_by_visible_text(self.sheng)
        Select(driver.find_element_by_xpath("//select[@id='regform_querySubTypeName']")).select_by_visible_text('行政区划')

        with open(r'D:\文档\亚信实习\工作\iop\地区.txt') as f:
            #取出地市，区县
            lines = f.readlines()
        self.shi = lines[0].strip().replace('\n','')

        del lines[0]

        for qu in lines:
            print(qu)
            try:
                self.qu=qu.strip().replace('\n','')
                driver.get("http://117.132.182.230:18080/iopbj/ListChannelInfoAction.action")

                Select(driver.find_element_by_xpath("//select[@id='regform_queryCountyName']")).select_by_visible_text(self.sheng)
                Select(driver.find_element_by_xpath("//select[@id='regform_querySubTypeName']")).select_by_visible_text('行政区划')

                driver.find_element_by_xpath("//input[@id='regform_queryByName']").send_keys("{0}_{1}_{2}".format(self.sheng,self.shi,self.qu))
                time.sleep(1)
                driver.find_element_by_xpath("//input[@id='regform_0']").click()
                # res=driver.find_element_by_xpath("//table[@border='1']/tbody/tr[2]/td/table/tbody/tr[2]/td[7]/a")
                res=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[7]/a")
                if res.text =='否':
                    # link=res.get_attribute('href')
                    id=driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]").text
                    boundary_url="http://117.132.182.230:18080/iopbj/ImportAreaPolygon.jsp?id={0}".format(id)

                    # addrs_list=self.shi+self.qu
                    res=self.get_boundary(driver)

                    if not self.is_Hollow(res):
                        boundary=res.text.replace(';','\n')
                        time.sleep(1)
                        driver.get(boundary_url)
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
                        pass

                else:
                    driver.find_element_by_xpath("//input[@id='regform_queryByName']").clear()
            except BaseException as e:
                print(self.qu)
        driver.quit()

        # print(link)


    def get_boundary(self,driver):
        url = "http://localhost:63342/Asiainfo/iop%E5%8C%BA%E5%9F%9F%E8%BE%B9%E7%95%8C/test.html"
        driver.get(url)
        # sheng = '浙江省'
        # shi = '舟山市'
        # qu = '定海区'

        driver.find_element_by_xpath("//body/input[@id='districtName']").send_keys('{0}{1}{2}'.format(self.sheng[:-1], self.shi, self.qu))
        # time.sleep(1)
        driver.find_element_by_xpath("/html/body/input[2]").click()

        driver.find_element_by_xpath("/html/body/input[2]").click()
        res = driver.find_element_by_xpath("//textarea[@id='Div1']")
        time.sleep(2)

        # res=Get_Region_Boundary.start(addrs_list)

        return res
    def is_Hollow(self,res):
        s = res.text
        # print(s)
        l = s.split(';')
        l1 = [n.split(',') for n in l]

        for i in l1:

            if len(i) > 2:
                print(self.sheng+self.shi+self.qu+"有空洞")
                return True

        return False
    # driver.get('http://117.132.182.230:18080/iopbj/toNewChannelInfo.action')
    def start(self):
        driver = webdriver.Firefox()
        self.login(driver)
        self.search(driver)


if __name__=="__main__":
    bianjie().start()