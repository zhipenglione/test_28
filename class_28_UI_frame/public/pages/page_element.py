# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/13 14:32
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
'''
存放页面元素
'''
'''
PO设计模式----page object  页面对象模型
把所有页面的元素当作对象
1、元素，定位方法和用例进行分离
2、维护代码更容易，减少冗余的代码
3、降低代码的耦合度

'''

class Page_Element():
    #登录
    user_elem=('id','ls_username')
    pwd_elem=('xpath','//*[@id="ls_password"]')
    click_login=('css','[class="pn vm"]')


    #设置
    sett_elem=('xpath','//*[@id="um"]/p[1]/a[2]')



    #管理中心
    guanli=('xpath','//*[@id="um"]/p[1]/a[6]')