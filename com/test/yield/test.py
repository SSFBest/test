# -*- coding: utf-8 -*-

# import Image
import os,re
import string

def test1():
    a=[1]
    for o in a:
        yield o
def test2():
    a=[]
    for aa in a:
        print aa
    else:
        print 'ok'
def test3():
    a=[1,2]
    for aa in a:
        yield aa
        print aa
    else:
        print 'ok'
 
if __name__ == '__main__':    
    # print test2()%({'meida_url':'http://www.youxi16.com'})
    # d=test1()
    # type(d)
    # print [s for s in test3()]

    test2()