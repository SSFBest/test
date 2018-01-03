# -*- coding: utf-8 -*-

import requests

def test_reqest():
	url='http://m.baidu.com/from=1012585f/bd_page_type=1/ssid=15567761646568656174327407/uid=0/pu=usm%402%2Csz%401320_2001%2Cta%40iphone_1_3.0_3_528/baiduid=F8CF1C9B13A69F341A9A38C3718410D8/w=10_10_%E9%B1%BC%E8%82%9D%E6%B2%B9%E7%9A%84%E5%8A%9F%E6%95%88%E4%B8%8E%E4%BD%9C%E7%94%A8/t=iphone/l=1/tc?ref=www_iphone&lid=16538771669423618855&order=4&waplogo=1&fm=wnor&dict=-1&tj=www_zhidao_normal_4_10_10_title&sec=8644&di=312580a852c21860&bdenc=1&nsrc=IlPT2AEptyoA_yixCFOxXnANedT62v3IDBqMMS6LLDivpEmixP4kHREsRC0aNWiCGkb8gTCcshYFuX3b_71l8hRArKtosWka6SWhuKC'
	# url='http://www.smzdm.com/gourl/DD714917912662A2/AA_YH_95'
	res = requests.head(url)
	print res.headers
	print res.headers['Location']
def test_req_lib():
	import urllib2,gzip
	# url='http://m.baidu.com/from=1012585f/bd_page_type=1/ssid=15567761646568656174327407/uid=0/pu=usm%402%2Csz%401320_2001%2Cta%40iphone_1_3.0_3_528/baiduid=F8CF1C9B13A69F341A9A38C3718410D8/w=10_10_%E9%B1%BC%E8%82%9D%E6%B2%B9%E7%9A%84%E5%8A%9F%E6%95%88%E4%B8%8E%E4%BD%9C%E7%94%A8/t=iphone/l=1/tc?ref=www_iphone&lid=16538771669423618855&order=4&waplogo=1&fm=wnor&dict=-1&tj=www_zhidao_normal_4_10_10_title&sec=8644&di=312580a852c21860&bdenc=1&nsrc=IlPT2AEptyoA_yixCFOxXnANedT62v3IDBqMMS6LLDivpEmixP4kHREsRC0aNWiCGkb8gTCcshYFuX3b_71l8hRArKtosWka6SWhuKC'
	url='http://www.smzdm.com/gourl/DD714917912662A2/AA_YH_95'
	headers={
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36',
		# 'referer':'https://detail.tmall.com/item.htm?id=527393215035',
		}
	# req=urllib2.Request(url)
	request = urllib2.Request(url)
	if headers:
		for k, v in headers.iteritems():
			request.add_header(k, v)
	content = urllib2.urlopen(request)
	location = content.info()
	print location
	print content
	using_gzip = content.headers.get('Content-Encoding', '')=='gzip'
	body = content.read()
	print 'body:',body
	if using_gzip:
		gzipper = gzip.GzipFile(fileobj=StringIO(body))
		fcontent = gzipper.read()
		gzipper.close()
		print 'fcontent:',fcontent
def test_urlopen():
	import urllib
	# url='http://m.baidu.com/from=1012585f/bd_page_type=1/ssid=15567761646568656174327407/uid=0/pu=usm%402%2Csz%401320_2001%2Cta%40iphone_1_3.0_3_528/baiduid=F8CF1C9B13A69F341A9A38C3718410D8/w=10_10_%E9%B1%BC%E8%82%9D%E6%B2%B9%E7%9A%84%E5%8A%9F%E6%95%88%E4%B8%8E%E4%BD%9C%E7%94%A8/t=iphone/l=1/tc?ref=www_iphone&lid=16538771669423618855&order=4&waplogo=1&fm=wnor&dict=-1&tj=www_zhidao_normal_4_10_10_title&sec=8644&di=312580a852c21860&bdenc=1&nsrc=IlPT2AEptyoA_yixCFOxXnANedT62v3IDBqMMS6LLDivpEmixP4kHREsRC0aNWiCGkb8gTCcshYFuX3b_71l8hRArKtosWka6SWhuKC'
	url='http://www.smzdm.com/gourl/DD714917912662A2/AA_YH_95'
	print urllib.urlopen(url).geturl()


if __name__ == '__main__':
	# test_reqest()
	# test_req_lib()
	test_urlopen()