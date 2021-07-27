# -*- coding: utf-8 -*-

import time
from selenium import webdriver
driver=webdriver.Chrome()#实例化Chrome类
url_1='https://www.baidu.com'

driver.get(url_1)#通过driver对象，调用get方法访问url
driver.implicitly_wait(10)#隐式等待


#元素定位
#id
driver.find_element_by_id('kw').send_keys('茶卡盐湖')
driver.find_element_by_id('su').click()



time.sleep(10)
driver.quit()