#-*- coding: utf8 -*-

import xlrd,re,logging,sys

import urllib
import urllib2
import cookielib
import base64
import re
import json
import hashlib
import rsa
import binascii
import gzip
from cStringIO import StringIO
import datetime
from yuelianglib.common.utils import escape_solr
from yuelianglib.logics import jd_config
from yuelianglib.logics import open_yueliang_config
from math import ceil
import time
import blog
import MySQLdb

def process(user,state='state_1'):
	dbargs = dict(
			host='192.168.56.181',
			db='yueliangapps',
			user='developer_yl',
			passwd='12345678',
			charset='utf8',
			use_unicode=True,
		)
	def follow():
		conn = MySQLdb.connect(**dbargs)
		# conn=MySQLdb.connect(host=host,port=3306,user=username,passwd=passworld,db=d)
		cursor=conn.cursor()
		sql = 'select uid from appsWeiboUsers where %s=0 limit 100'%state
		print sql
		cursor.execute(sql)
		cursor2=conn.cursor()
		n=cursor.fetchall()
		for p in n:
			uid = p[0]
			print uid
			success=user.followed(uid) 
			if success:
				# print 'cid is:',type(cid),type(p[0])
				sql3=u'update appsWeiboUsers set %s=1,%s_time=\'%s\' where uid=%s'%(state,state,datetime.datetime.now(),uid)
				print sql3
				# print sql3
				cursor2.execute(sql3)
			time.sleep(10)
		conn.commit()
		cursor2.close()
		cursor.close()
	if __name__ == '__main__':
		follow()

	
if __name__ == '__main__':
	USER={'user1':('goldhwi','goldhwi.com.cn','5fbb7ffc7f53585700e3ec0ba815ae5d'),'user2':('hulianjiang@15yueliang.com','iWeibo8866','fd89d92014211a8cf3632814249f115e')}
	user=USER.get('user2')
	u=blog.User(user[0],user[1],user[2])
	u.login()
	print u.uid,u.blog_vtoken
	if u.uid:
		process(u,'state_2')
	# sheet=5
	# process(sheet,u)