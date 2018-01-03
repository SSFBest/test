# -*- coding: utf-8 -*-

from datetime import datetime
from md5 import md5
import hashlib,re,simplejson

from yuelianglib.common.httprequest import http

from yuelianglib.common.utils import print_err,get_err

sl=[]
current_dir='C:/Users/lenovo/Documents'
def process_item(page=1):
	try:
		resp=http('GET','http://money.finance.sina.com.cn/quotes_service/api/jsonp_v2.php/IO.XSRV2.CallbackList[\'y2PhvJWEK4sZBTJW\']/StatisticsService.getVolumeReduceConList?page=%d&num=50&sort=day_con&asc=0&node=adr_hk'%page)
		# resp,num=re.subn(r'(process_comment\()({.*})(\));',r'\1%s\2%s\3'%('\'','\''),resp)
		# print resp
		m=re.match(ur'^(IO\.XSRV2\.CallbackList\[\'y2PhvJWEK4sZBTJW\'\]\()(\[\{.*\}\])(\))$',resp)
		if m:
			resp=m.group(2)
			process_sl(resp.decode('gbk'))
		else:
			print 'error in process_item '
		
	except Exception as e:
		print_err()

def process_sl(json_obj):
	json_obj=re.sub(r'(\w+):',r'"\1":',json_obj,flags=re.MULTILINE)	
	# print json_obj
	dd=simplejson.loads(json_obj)
	for d in dd:
		# print d.get('symbol')
		sl.append(d.get('symbol'))
if __name__ == '__main__':
	for i in range(7):
		process_item(i+1)
	FileConfigs = file('%s/sl.txt'%(current_dir),'w')
	print len(sl)
	for s in sl:
		# print s
		FileConfigs.write(u'%s\n'%(s[2:]))
	FileConfigs.close()