# -*- coding: utf-8 -*-

import re,urllib2
from yuelianglib.common.httprequest import http
headers = { 
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',#有时间研究一下。好象不支持GZIP
    'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    # 'Host':'ip138.com',
    # 'Upgrade-Insecure-Requests':'1',
    # 'If-Modified-Since':'Fri, 19 Aug 2016 02:13:52 GMT',
    # 'If-None-Match':"6a30c054bff9d11:c4b",
    # 'Cookie':'pgv_pvi=7049239552; pgv_si=s9607102464',
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}
class Get_public_ip:
    
    def get_ip(self):
        print 'ddd'
        sd=http('GET','http://1212.ip138.com/ic.asp',headers=headers)
        print 'ddd,lll'
        print 'dddd88ss_%s'%(sd)
        # return re.search('d+.d+.d+.d+',s).group(0)
if __name__ == "__main__":
    getmyip = Get_public_ip()
    getmyip.get_ip()