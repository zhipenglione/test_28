# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/13 14:13
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
'''
读取excel 里面登录信息，url,username,pwd
'''
from class_28_UI_frame.public.utils.read_excel import Read_Excel#导入Read_Excel类
class Login_Data():
    def __init__(self):
        #实例化Read_Excel---为对象
        self.read_excel=Read_Excel('Data.xlsx',0)
    def get_url(self):
        #获取url
        url_value=self.read_excel.read_value(1,0)
        return url_value
    def get_user(self):
        #获取用户名
        user_value=self.read_excel.read_value(1,1)
        return user_value
    def get_password(self):
        #获取密码
        password_value=self.read_excel.read_value(1,2)
        return int(password_value)
if __name__ == '__main__':
    login_data=Login_Data()
    print(login_data.get_url())
    print(login_data.get_user())
    print(login_data.get_password())
