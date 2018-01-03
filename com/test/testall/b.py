#-*- coding: utf-8 -*-
'''
Created on 2010-7-15

@author: Administrator
'''
#只能导入a中，__all__中存在对象
#from a import *
from com.test.testall import a
from a import *
a.d()
c()
d()

if __name__ == '__main__':
	c()