#-*- coding: utf8 -*-

import xlrd,re,logging,sys,json
import platform
from scrapy.selector import Selector
from yuelianglib.common.httprequest import http

log_console = logging.StreamHandler(sys.stderr)
default_logger = logging.getLogger(__name__)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)

LOCAL = 'Windows' in platform.system()

if LOCAL:
  JINXUAN_DIR='D:/mywork'
else:
  JINXUAN_DIR='D:/data/appdata/yueliang/jinxuan'
cookie={'cookie1': 'UNICLQDxGeiUdu2e8mzQbAdAJ72nNq7WNSx7YehUHhE%3D', 'cookie2': '154c4639b250d9ef19f142795f0fa270', 'uc3': 'sg2', 'uc1': 'cookie14', 'whl': '-1%260%260%260', 'lgc': 'teemimi', '_nk_': 'teemimi', ' l': 'AikpFLg1YgMPSEGFBvnMvOVYud6DXR0o', '_l_g_': 'Ug%3D%3D', 'Hm_lpvt_a89472e458c9b0854d6a2577d245fb34': '1504079155', 'cq': 'ccp%3D0', '_tb_token_': 'ebaeee13ebeef', 'swfstore': '97538', 'pnm_cku822': '005UW5TcyMNYQwiAiwQRHhBfEF8QXtHcklnMWc%3D%7CUm5Ockp3TnNJfUF5QX9AfCo%3D%7CU2xMHDJ7G2AHYg8hAS8XIw0tA18%2BWDRTLVd5L3k%3D%7CVGhXd1llXWBZZF5qVm5WaFdrXGFDfUd4RnJMeUJ5TXFLck5xS2Uz%7CVWldfS0SMg4zBiYdPRM0H2pBZgEveS8%3D%7CVmhIGCUFOBgkGiMXNwk9CTERLRMoEzMJMgcnGyUeJQU%2FATRiNA%3D%3D%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D', 'Hm_lvt_a89472e458c9b0854d6a2577d245fb34': '1504075336,1504075352,1504076424,1504079155', 'isg': 'Aufnyo-RclhoSfYUhh1fcX9ldhtxxHzfZSkC9blUA3adqAdqwTxLniWqvJ_M', 'hng': 'CN%7Czh-CN%7CCNY%7C156', 'otherx': 'e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0', 'cookie17': 'UNGQXF%2FfFY8%3D', 'unb': '31634811', 'uss': 'BYS4a5%2F3Or%2FEE6D%2BfmTgBuu%2BIWGSaXxF%2F05WAU8WfO9gFPtwBVDXaTh1AoM%3D', 't': '088af55a7362bbc4fb14c8d40f68d5bf', 'cna': 'bazrEeYU5QcCAXhVQtprsIeN', 'x': '__ll%3D-1%26_ato%3D0', 'login': 'true', 'sg': 'i1e', 'tracknick': 'teemimi'}
# headers = {
# 	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
# }
headers = {
# 'Host': 'detail.tmall.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.04',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Cookie': 'isg=AkZGLZLxY_f0xDaIAfTgM0tqljwID03wRnQdaDBvMmlEM-ZNmDfacSzBfVQB; cna=BA/DEMNPDw8CAXhVUl3m1JOE; l=Au3tut7esZZXJ9SGFAdALTXT/YNnSiEc; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; cq=ccp%3D1; um=BA335E4DD2FD504FAB515310CFA44A09AAB50F2C35549BF2B5CBC0F9BC5755C96934A31A407A9441CD43AD3E795C914CE8E30C6FF2F7D9F92DE450B2DE78A2AA; uss=WvKT1P051Zvu2RYqw6RKxbwxn3YDtz8beTa4JfRQdHU0K5xS7awj%2F4zyeg%3D%3D; pnm_cku822=153UW5TcyMNYQwiAiwTR3tCf0J%2FQnhEcUpkMmQ%3D%7CUm5Ockp3TnNGeUR%2BRH9Aey0%3D%7CU2xMHDJ%2BH2QJZwBxX39Rb1R6WnQoSS9DJFogDlgO%7CVGhXd1llXWBZZFFuU2lTaFdsW2ZEcUpxTnVBdEx0SXxFeEF1TWM1%7CVWldfS0RMQ00Cj8fIQEvEC0XOW85%7CVmhIGCMXNwoqFigRJQU7AToEJBgmHSYGPAcyEi4QKxAwCjQBVwE%3D%7CV25Tbk5zU2xMcEl1VWtTaUlwJg%3D%3D; x=__ll%3D-1%26_ato%3D0; t=00e2dd5d9c9695f28a9d32775060ac5b; uc3=sg2=B0T8cG%2Fyx89hAxiviDRvZwl20D1cVwmefaepIHK25do%3D&nk2=EFed7YQ3KRfGTCkUvTY%3D&id2=UU8OdBtPhrCrpQ%3D%3D&vt3=F8dBzWYesuGmA3035BA%3D&lg2=W5iHLLyFOGW7aA%3D%3D; lgc=simplefastbest; tracknick=simplefastbest; cookie2=1850a386b7543c750942326025e7e246; _tb_token_=e1b93886860fe; uc1=cookie14=UoTcC%2BwPvqyvDA%3D%3D&lng=zh_CN&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie21=UIHiLt3xTw%3D%3D&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; swfstore=22145',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0',
}
# headers={
# 	':authority':'detail.tmall.com',
# ':method':'GET',
# ':scheme':'https',
# 'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# 'accept-encoding':'gzip, deflate, br',
# 'accept-language':'zh-CN,zh;q=0.8',
# 'cache-control':'no-cache'
# }
# headers.update(Cookie="; ".join('%s=%s' % (k,v) for k,v in cookie.items()))

def read_ci(path,word):
	data = xlrd.open_workbook(path)  #打开文件
	table = data.sheets()[0] #通过索引顺序获取
	# table = data.sheet_by_index(0) #通过索引顺序获取
	# table = data.sheet_by_name(u'Sheet1')#通过名称获取
	# 获取整行和整列的值（数组）
	# table.row_values(i)
	# table.col_values(i)
	# 获取行数和列数
	nrows = table.nrows
	ncols = table.ncols

	# word={}
	# 循环行列表数据
	for r in xrange(1,nrows):
		for c in xrange(0,ncols):
			col=table.cell(r,c).value
			link=table.hyperlink_map.get((r, c))
			# link=table.cell(r,c).Hyperlinks.Item(1).Address
			print col,link.url_or_path if link else None

def process():
	word={}

	read_ci('D:/mywork/tmall/tmall_618.xls',word)



re_userdict = re.compile('^(.+?)( [0-9]+)?( [a-z]+)?$', re.U)
def read():
    f = open('D:/projects/python_projects/pytest/src/excel/xlrd/data.txt', 'rb')
    word_dic={}
    for lineno, ln in enumerate(f, 1):
            line = ln.strip()
            # print type(line)
            if not isinstance(line, unicode):
                try:
                    line = line.decode('utf-8').lstrip('\ufeff')
                except UnicodeDecodeError:
                    raise ValueError('dictionary file %s must be utf-8' % f_name)
            if not line:
                continue
            word, freq, tag = re_userdict.match(line).groups()
            if freq is not None:
                freq = freq.strip()
            if tag is not None:
                tag = tag.strip()
            word_dic.setdefault(word,1)
    output = open('ik_word.txt', 'w')
    for k,v in word_dic.items():
        output.write('%s\n'%(k.encode('utf8')))
    output.close()
def read_jingxuan_for_json2(path):
	data = xlrd.open_workbook(path)  #打开文件
	table = data.sheets()[0] #通过索引顺序获取
	# table = data.sheet_by_index(0) #通过索引顺序获取
	# table = data.sheet_by_name(u'Sheet1')#通过名称获取
	# 获取整行和整列的值（数组）
	# table.row_values(i)
	# table.col_values(i)
	# 获取行数和列数
	nrows = table.nrows
	ncols = table.ncols
	print nrows,ncols

	# word={}
	# 循环行列表数据
	j={}
	d={'fenlei':0,'shop':1,'open':2,'name':4,'item_url':5,'image':6,'price':7,'quan':10,'final_price':11,'start':14,'end':15,'link':16}
	for r in xrange(1,nrows):
		jinxuan={}
		for k,v in d.items():
			col=table.cell(r,v).value
			link=table.hyperlink_map.get((r, v))
			# link=table.cell(r,c).Hyperlinks.Item(1).Address
			print col,link.url_or_path if link else None
			if k == 'fenlei':
				simple=col.split('/',1)[0]
				if len(simple)>4:
					jinxuan.update({'simple':''})
				else:
					jinxuan.update({'simple':simple})
			jinxuan.update({k:link.url_or_path if link else col})
		fenlei=j.get(jinxuan.get('fenlei'))
		if fenlei:
			shop=fenlei.get(jinxuan.get('shop'))
			if shop:
				shop.append(jinxuan)
			else:
				shop=[jinxuan]
			fenlei.update({jinxuan.get('shop'):shop})
			j.update({jinxuan.get('fenlei'):fenlei})
		else:
			j.update({jinxuan.get('fenlei'):{jinxuan.get('shop'):[jinxuan]}})


	json.dump(j, open('%s/%s'%(JINXUAN_DIR,'jinxuan2.json'), 'w'))
def read_jingxuan_for_json(path):
	data = xlrd.open_workbook(path)  #打开文件
	table = data.sheets()[0] #通过索引顺序获取
	# table = data.sheet_by_index(0) #通过索引顺序获取
	# table = data.sheet_by_name(u'Sheet1')#通过名称获取
	# 获取整行和整列的值（数组）
	# table.row_values(i)
	# table.col_values(i)
	# 获取行数和列数
	nrows = table.nrows
	ncols = table.ncols
	print nrows,ncols

	# word={}
	# 循环行列表数据

	j={}
	d={'fenlei':0,'shop':1,'open':2,'id':3,'name':4,'item_url':5,'image':6,'price':7,'quan':10,'final_price':11,'start':14,'end':15,'link':16}
	for r in xrange(1,nrows):
		jinxuan={}
		for k,v in d.items():
			col=table.cell(r,v).value
			link=table.hyperlink_map.get((r, v))
			# link=table.cell(r,c).Hyperlinks.Item(1).Address
			print col,link.url_or_path if link else None
			if k == 'fenlei':
				simple=col.split('/',1)[0]
				if len(simple)>4:
					jinxuan.update({'simple':''})
				else:
					jinxuan.update({'simple':simple})
			if k == 'id':
				id_col=col
			jinxuan.update({k:link.url_or_path if link else col})
		kw={'timeout':30,'id':id_col}
		request_url='https://detail.tmall.com/item.htm'

		fenlei=j.get(jinxuan.get('fenlei'))
		if fenlei:
			shop=fenlei.get(jinxuan.get('shop'))
			if shop:
				shop_link=shop.get('url')
				if not shop_link:
					r=http('GET',request_url,headers,**kw)
					# sel=Selector(text=r).xpath('/html/head/link[@rel="canonical"]/@href')
					shop_link,shop_age=get_shop_parameter(r,jinxuan.get('open'))
				else:
					shop_age=shop.get('age')
				shop_list=shop.get('list')
				if shop_list:
					shop_list.append(jinxuan)
				else:
					shop_list=[jinxuan]

				shop={'url':shop_link,'open':jinxuan.get('open'),'age':shop_age,'list':shop_list}
			else:
				r=http('GET',request_url,headers,**kw)
				# sel=Selector(text=r).xpath('/html/head/link[@rel="canonical"]/@href')
				shop_link,shop_age=get_shop_parameter(r,jinxuan.get('open'))
				shop={'list':[jinxuan],'url':shop_link,'open':jinxuan.get('open'),'age':shop_age}
			fenlei.update({jinxuan.get('shop'):shop})
			j.update({jinxuan.get('fenlei'):fenlei})
		else:
			# print jinxuan.get('item_url'),'-----------------------'
			r=http('GET',request_url,headers,**kw)
			# print r,'-----------------------'
			# sel=Selector(text=r).xpath('/html/head/link[@rel="canonical"]/@href')
			shop_link,shop_age=get_shop_parameter(r,jinxuan.get('open'))
			j.update({jinxuan.get('fenlei'):{jinxuan.get('shop'):{'list':[jinxuan],'url':shop_link,'age':shop_age,'open':jinxuan.get('open')}}})


	json.dump(j, open('%s/%s'%(JINXUAN_DIR,'jinxuan.json'), 'w'))
def get_shop_parameter(r,open):
	if open == u'天猫':
		shop_link=Selector(text=r).xpath('//*[@id="shopExtra"]//a[@class="slogo-shopname"]/@href').extract()
		if shop_link:
			shop_link=shop_link[0]
		else:
			shop_link=None
		shop_age=Selector(text=r).xpath('//*[@id="shopExtra"]//span[@class="tm-shop-age-num"]/text()').extract()
		if shop_age:
			shop_age=shop_age[0]
		else:
			shop_age=None
	elif open == u'淘宝':
		m=re.search(r'\w{0}\s{0,}url\s{0,}:\s{0,}\'(?P<shop_link>.*)\'\s{1,}',r)
		if m:
			shop_link=m.group('shop_link')
		else:
			shop_link=None
		m=re.search(r'\w{0}\s{0,}shopAge\s{0,}:\s{0,}\'(?P<shopAge>.*)\'\s{0,}',r)
		if m:
			shop_age=m.group('shopAge')
		else:
			shop_age=None

	return shop_link,shop_age


if __name__ == '__main__':
    # read()
	# process()
	# test()
	read_jingxuan_for_json('E:/downloads/firefox/jx_site.xls')