# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/13 14:40
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
'''
存放二次封装的元素定位的方法
'''
from selenium import webdriver
import time
import unittest
from class_28_UI_frame.public.pages.page_element import Page_Element

class Base_Element_Method(unittest.TestCase):
    @classmethod
    def set_driver(cls,driver):
        '''设置浏览器的驱动'''
        cls.driver=driver

    @classmethod
    def get_driver(cls):#获取浏览器驱动----单例模式
        return cls.driver



    #调试
    # user_elem = ('ID', 'ls_username')
    # cls.driver = webdriver.Chrome()
    @classmethod
    def find_element(cls,element):
        '''封装元素定位的方法'''
        elemt_type=element[0]
        elemt_value=element[1]
        elemt_type=elemt_type.lower()
        try:
            if  elemt_type =='id':
                elem=cls.driver.find_element_by_id(elemt_value)
            elif elemt_type=='name':
                elem=cls.driver.find_element_by_name(elemt_value)
            elif elemt_type=='class':
                elem=cls.driver.find_element_by_class_name(elemt_value)
            elif elemt_type=='xpath':
                elem=cls.driver.find_element_by_xpath(elemt_value)
            elif elemt_type=='css':
                elem=cls.driver.find_element_by_css_selector(elemt_value)
            elif elemt_type=='link':
                elem=cls.driver.find_element_by_link_text(elemt_value)
            else:
                raise NameError('请输入正确的参数')
        except Exception as e:
            print('输入参数无法找到',e)

        return elem

    @classmethod
    def send_keys(cls,elem,text):
        '''二次封装输入文本内容'''
        elem.send_keys(text)
    @classmethod
    def get_click(cls,elem):
        '''二次封装点击元素'''
        elem.click()
    @classmethod
    def sleep(cls,sec):
        time.sleep(sec)
    @classmethod
    def close(cls):
        '''关闭浏览器'''
        cls.driver.quit()
    @classmethod
    def get_title(cls):
       return cls.driver.title

if __name__ == '__main__':
    user_elem = ('ID', 'ls_username')
    Base_Element_Method.find_element(user_elem)
