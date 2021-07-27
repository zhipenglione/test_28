# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/13 16:06
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
from class_28_UI_frame.public.pages.page_element import Page_Element as PE#登录用的元素
from class_28_UI_frame.public.pages.base_element_method import Base_Element_Method as BEM#定位方法的类
from  selenium import webdriver
import unittest
from class_28_UI_frame.public.utils.login_data import Login_Data
from class_28_UI_frame.public.utils.logger import trace_log

url_value=Login_Data().get_url()
user_value=Login_Data().get_user()
pwd_value=Login_Data().get_password()

class Test_Login(BEM):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        BEM.set_driver(cls.driver)
    @classmethod
    def tearDownClass(cls):
        BEM.sleep(2)
    @trace_log
    def test_001_login(self):
        driver=BEM.get_driver()
        driver.get(url_value)
        #login
        elemt=BEM.find_element(PE.user_elem)
        BEM.send_keys(elemt,user_value)

        elemt=BEM.find_element(PE.pwd_elem)
        BEM.send_keys(elemt,pwd_value)

        elemt=BEM.find_element(PE.click_login)
        BEM.get_click(elemt)
        # print(BEM.get_title())
        # self.assertEqual(BEM.get_title(),'论坛 - Powered by Discuz!',msg='断言失败，内容不相等')
        BEM.sleep(3)
        text=BEM.find_element(PE.guanli).text
        self.assertIn(text,'管理中心11111')
        return BEM.get_title()
if __name__ == '__main__':
    unittest.main(verbosity=2)