from selenium import webdriver
import pandas as pd

driver=webdriver.Firefox()
driver.set_window_size(800,1000)

driver.get('https://baike.baidu.com/item/%E5%9B%BD%E5%AE%B6AAA%E7%BA%A7%E6%97%85%E6%B8%B8%E6%99%AF%E5%8C%BA/1461119')
# for i in range(1,30):
tables=driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/div[2]/table/tbody/tr/td[1]/div')
# print(tables)
l=[]
for table in tables:
    l.append(table.text)
df=pd.DataFrame(l)
df.to_excel(r'D:\文档\亚信实习\工作\iop\景区数据\3A景区名单.xlsx',header=['名称'])
driver.quit()