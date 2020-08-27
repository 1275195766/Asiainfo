#coding:utf-8
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from iop区域边界 import getpoiboundary
import time
def Drawborder(id,key_word,city,driver):

    # id = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td[4]").text
    # boundary_url = "http://117.132.182.230:18080/iopbj/ImportAreaPolygon.jsp?id={0}".format(id)

    # addrs_list=self.shi+self.qu
    try:
        import_url="http://117.132.182.230:18080/iopbj/ImportAreaPolygon.jsp?id={0}".format(id)
        driver.get(import_url)
        time.sleep(1)
        boundary=getpoiboundary.get_boundary(key_word, city)
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
    # driver.find_element_by_xpath("//input[@id='regform_queryByName']").clear()

if __name__=="__main__":
    driver=webdriver.Firefox()
    driver.get('http://117.132.182.230:18080/iopbj/')
    driver.find_element_by_xpath("//input[@name='username']").send_keys('yujiang')
    driver.find_element_by_xpath("//input[@name='pwd2']").send_keys('bajyie123!')
    driver.find_element_by_xpath("//input[@type='image']").click()
    yzm = input("请输入验证码：")

    driver.find_element_by_xpath('//*[@id="regform"]/div[1]/p/input[1]').send_keys(yzm)
    driver.find_element_by_xpath('//*[@id="regform"]/div[2]/input').click()

    Drawborder('465244688','首都国际机场','北京市',driver)