# -*- coding: utf-8 -*-

# import Image
import os,re
import string

def test1(aid=None,title=None):
    print title
    print aid
def test2(**kwargs):
    print kwargs.get('aid',None)
def test3(a='a',b='b',*cc):
	print 'a:',a
	print 'b:',b
	print 'cc:',cc
def test4(a=5,*l):
    print a
    print l

 



if __name__ == '__main__':    
    # print test2()%({'meida_url':'http://www.youxi16.com'})
    k={'title':'goldhwi'}
    test1(**k)
    b=test2(aid=9)
    print b, type(b)
    print '----------------'
    print test3(2,3,*[3,4])
    print '_'*9
    print test4(5,6,7,8)