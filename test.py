from selenium import webdriver
import time
driver=webdriver.PhantomJS()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')


search_handle=driver.current_window_handle
print(search_handle)

driver.find_element_by_link_text('登录').click()
time.sleep(2)
driver.find_element_by_link_text('立即注册').click()
driver.get_screenshot_as_file(r'baidu_img.png')

all_handles=driver.window_handles

for handle in all_handles:
   if handle !=search_handle:
      driver.switch_to.window(handle)
      print('now register window!')
      driver.find_element_by_name("userName").send_keys('username')
      driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys('password')
      time.sleep(2)


for handle in all_handles:
   if handle == search_handle:
      driver.switch_to.window(handle)
      print("now serach window")
      driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
      driver.find_element_by_id('kw').send_keys('selenium')
      driver.find_element_by_id('su').click()
      time.sleep(2)


driver.quit()