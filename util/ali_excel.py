#-*- coding: utf8 -*-

import xlrd,re,logging,sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time,json
from yuelianglib.libs.open import alihelper
import jieba
import jieba.analyse

USER_DICT='D:/mywork/lib/jieba/userdict.txt'
IDF_FILE='D:/mywork/lib/jieba/idf.txt'

jieba.load_userdict(USER_DICT)
jieba.analyse.set_idf_path(IDF_FILE)

log_console = logging.StreamHandler(sys.stderr)
default_logger = logging.getLogger(__name__)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)
driver = webdriver.PhantomJS( desired_capabilities=dcap)

def force_bytes(value):
    """
    Forces a Unicode string to become a bytestring.
    """
    # if IS_PY3:
        # if isinstance(value, str):
            # value = value.encode('utf-8', 'backslashreplace')
    # else:
    if isinstance(value, unicode):
        value = value.encode('utf-8')

    return value

def read_ci(path,word,sheet):
	data = xlrd.open_workbook(path)  #打开文件
	table = data.sheets()[sheet] #通过索引顺序获取
	nrows = table.nrows
	ncols = table.ncols
	# word={}
	# 循环行列表数据
	for r in xrange(1,nrows):
		d={}
		for c in xrange(0,ncols):
			col=table.cell(r,c).value
			if c == 0:
				d['cel_category']=col
			elif c==1:
				d['cel_title']=col
			elif c==2:
				d['cel_market_price']=col
			elif c==3:
				d['cel_offprice']=col
			elif c==4:
				d['cel_offprice_num']=col
			elif c==5:
				link=table.hyperlink_map.get((r, c))
				d['link']=link.url_or_path
				time.sleep(2)
				link=process_go_link(d['link'])
				m=re.search('id=([0-9]+)',link)
				if m:
					pid=m.group(1)
					iid,title,pic,price,volume,urll=alihelper.get_base(pid)

				# print d['link'],pid,iid,title,pic,price,volume,urll
				default_logger.debug('%s,%s,%s,%s,%s,%s,%s,%s'%(d['link'],pid,iid,title,pic,price,volume,urll))
				d['iid']=iid
				d['title']=title
				d['pic']=pic
				d['price']=price
				d['urll']=urll
				d['volume']=volume

			elif c==6:
				d['reason']=col

		seokeywords = jieba.analyse.extract_tags('%s %s %s'%(d['reason'],d['title'],d['cel_title']),topK=5,withWeight=False,HMM=False,allowPOS=('n','nz','nr'))
		# print 'hmm:false:%s'%(','.join(seokeywords))
		default_logger.debug('hmm:false:%s'%(','.join(seokeywords)))
		d['tags']=','.join(seokeywords)
		word.append(d)
		# seokeywords = jieba.analyse.extract_tags('%s %s %s'%(d['reason'],d['title'],d['cel_title']),topK=5,withWeight=False,HMM=True,allowPOS=('n','nz','nr'))
		# print 'hmm:true:%s'%(','.join(seokeywords))
		# link=table.cell(r,c).Hyperlinks.Item(1).Address
		# print col,link.url_or_path if link else None
	
def process():
	word=[]
	name=['shouji','jiaju','qiche','guoji','meizhuang','xiansheng']
	sheet=5
	read_ci('D:/mywork/tmall/tmall_618_blog.xls',word,sheet)
	json.dump(word, open('D:/mywork/tmall/tmall_618_blog_%s.json'%name[sheet], 'w'))

def process_go_link(go_link):
	# driver = webdriver.PhantomJS( desired_capabilities=dcap)
	driver.get(go_link)
	return driver.current_url
	# now_handle = driver.current_window_handle #获取当前窗口句柄
	# print now_handle   #输出当前获取的窗口句柄
	# time.sleep(2)
	
	# driver.close()


if __name__ == '__main__':
	process()