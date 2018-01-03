#-*- coding: utf-8 -*-
'''
Created on 2010-9-16

@author: Administrator
'''
from TestClass import MyClass

def testNo():
    award = {}
    if not award:
        print 'ok'
def test_dic():
    dic={'main': {1: None, 2: MyClass(), 3: MyClass(), 4: None, 5: MyClass(), 6: None, 7: MyClass(), 8: None, 9: None, 10: None, 11: None, 12: MyClass(), 13: None, 14: None, 15: MyClass(), 16: None, 17: None}}
    crops = dic['main']
    data = {}
    print crops.items()
    for crop in crops.items():
        if crop[1]:
            print 'ok'
def test_sort():
    arr=[2,5,6,8]
#    arr.sort(key=lambda x: )
    print arr
if __name__ == '__main__':
#    testdic()
#    testNo()
    test_dic()
#    test_sort()

