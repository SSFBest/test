# -*- coding: utf-8 -*-

# import Image
import os
import string

def test1():
    str=u'中华人民共和国成立了'
    print str[0:3]
def test2():
	str='abcdef'
	str=string.replace(str,'bc','%%(meida_url)s%s'%'5678')
	print str
	return str
def is_mobile(ua):
    ismobile=False
    keywords = ['Android', 'iPhone', 'iPod', 'iPad', 'Windows Phone', 'MQQBrowser','IEMobile','UCBrowser']
    if ua.find("Windows NT") != -1 or  ua.find("Macintosh") != -1:
    	print 'ddd'
        return False

    for k in keywords:
        if ua.find(k)>-1:
            return True
    return False

if __name__ == '__main__':    
    # print test2()%({'meida_url':'http://www.youxi16.com'})
    print is_mobile('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')