# -*- coding: utf-8 -*-
import HTMLParser
import re
'''
Created on 2013-3-14

@author: Administrator
'''
def test1():
    str = "我爱派森"
    print repr(str.decode('UTF-8'))
    html_parser = HTMLParser.HTMLParser()
    html = u'''<p>
    &nbsp;&nbsp;&nbsp; 8888中国的
</p>''' 
    # html = '&lt;abc&gt;'
    result = html_parser.unescape(html)
    print type(result)
    print '111:',repr(result)
    result,num=re.subn(u'<p>[\xa0\s\u3000]+', '<p>', result)
    print result.encode('utf-8'),num

if __name__ == '__main__':
    # testBaidu()
#    testJson()
#    testGetRequest()
    # dic={u'公司':'',u'有限':'',u'科技':'',u'深圳':'',u'市':'',u'广州':'',u'上海':'',u'北京':'',u'杭州':'',u'成都':'',u'武汉':'',u'技术':'',u'股份':''}
    # print multi_replace(u'深圳十五月亮网络技术有限公司',dic).encode('utf8')
    test1()