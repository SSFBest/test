#-*- coding: utf8 -*-
'''
Created on 2010-9-13

@author: Administrator
'''

from pyExcelerator import *

if __name__ == '__main__':
    w = Workbook()
    ws0 = w.add_sheet(u'8月付费用户总数')
    ws0.write(0,0,u'总次数')
    ws0.write(0,1,u'35746')
    ws0.write(1,0,u'总人数')
    ws0.write(1,1,u'14383')
    ws1 = w.add_sheet(u'每个付费次数以及级别')
    ws2 = w.add_sheet(u'每个付费付费额度')
    ws3 = w.add_sheet(u'付费后到采集数据时仍未登陆的用户')
    ws4 = w.add_sheet(u'8月付费统计')
    ws5 = w.add_sheet(u'8月付费统计(用户)')
    ws6 = w.add_sheet(u'8月消费统计')
    ws7 = w.add_sheet(u'8月消费统计(用户)')
    w.save('stat.xls')

