# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/13 17:22
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""

from class_28_UI_frame.public.pages.base_element_method import Base_Element_Method as BEM
from class_28_UI_frame.public.pages.page_element import Page_Element as PE


class Test_Setting(BEM):
    @classmethod
    def setUpClass(cls):
        BEM.sleep(2)
    @classmethod
    def tearDownClass(cls):
        BEM.sleep(3)
        BEM.close()

    def test_002_setting(self):
        elem=BEM.find_element(PE.sett_elem)
        BEM.get_click(elem)