# -*- coding: utf-8 -*-
"""
@Time ： 2021/7/15 11:12
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
import logging
# logging.debug('调试日志')#级别10
# logging.info('正常消息日志')#20
# logging.warning('警告日志')#30
# logging.error('错误日志')#40
# logging.critical('严重错误')#50

logger=logging.getLogger()#实例化拿到日志对象
#日志写入的文件
file_log=logging.FileHandler(r'D:\class_project\class_28\class_28_UI_frame\test_log\log_class28.log',encoding='utf-8')
#创建一个屏幕对象
stre_log=logging.StreamHandler()

#格式化输出日志
formatter=logging.Formatter('%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-%(module)s-%(message)s')

#设置日志写入的格式
file_log.setFormatter(formatter)
stre_log.setFormatter(formatter)

logger.addHandler(file_log)
logger.addHandler(stre_log)
#
logger.setLevel(10)
# file_log.setLevel(30)
# logging.debug('调试日志')#级别10
# logging.info('正常消息日志')#20
# logging.warning('警告日志')#30
# logging.error('错误日志')#40
# logging.critical('严重错误')#50

def add_1(x,y):
    logging.info('x+y的结果信息')  # 30
    return x+y
add_1(2,9)