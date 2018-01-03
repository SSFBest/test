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
from yuelianglib.common.httprequest import http
log_console = logging.StreamHandler(sys.stderr)
default_logger = logging.getLogger(__name__)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)

#http://bbs.csdn.net/topics/390083000解决B06013要加refferft
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
}
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
# }
cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
urllib2.install_opener(opener)
postdata = {
	'entry': 'weibo',
	'gateway': '1',
	'from': '',
	'savestate': '7',
	'userticket': '1',
	'pagerefer':'',
	# 'ssosimplelogin': '1',
	'vsnf': '1',
	'vsnval': '',
	'su': '',
	'service': 'miniblog',
	'servertime': '',
	'nonce': '',
	'pwencode': 'rsa2',
	'rsakv':'',
	'sp': '',
	'sr':'1366*768',
	'prelt':'443',
	'encoding': 'UTF-8',
	'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
	'returntype': 'META'
}


def get_servertime():
	url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.18)&_=1465044863672'
	data = urllib2.urlopen(url).read()
	p = re.compile('\((.*)\)')
	try:
		json_data = p.search(data).group(1)
		data = json.loads(json_data)
		servertime = str(data['servertime'])
		nonce = data['nonce']
		pubkey = data['pubkey']
		rsakv = data['rsakv']

		return servertime, nonce,pubkey,rsakv
	except:
		print 'Get severtime error!'
		return None

def get_pwd(pwd, servertime, nonce):
	pwd1 = hashlib.sha1(pwd).hexdigest()
	pwd2 = hashlib.sha1(pwd1).hexdigest()
	pwd3_ = pwd2 + servertime + nonce
	pwd3 = hashlib.sha1(pwd3_).hexdigest()
	return pwd3
def get_pwd_rsa(password,servertime, nonce,pubkey):
	rsaPublickey = int(pubkey, 16)
	key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
	message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
	passwd = rsa.encrypt(message, key) #加密
	passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
	return passwd
def get_user(username):
	username_ = urllib.quote(username)
	username = base64.encodestring(username_)[:-1]
	return username

class User(object):
	def __init__(self,username,password,blog_vtoken=None):
		self.username=username
		self.password=password
		self.uid=None
		self.blog_vtoken=blog_vtoken
		super(User, self).__init__()
	def login(self):

		url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
		try:
			servertime, nonce,pubkey,rsakv = get_servertime()
		except:
			return
		global postdata
		postdata['servertime'] = servertime
		postdata['nonce'] = nonce
		postdata['rsakv'] = rsakv
		postdata['su'] = get_user(self.username)
		postdata['sp'] = get_pwd_rsa(self.password, servertime, nonce,pubkey)
		postdata = urllib.urlencode(postdata)

		req  = urllib2.Request(
			url = url,
			data = postdata,
			headers = headers
		)
		result = urllib2.urlopen(req)
		text = result.read()
		print text
		print '-----------'
		p = re.compile('location\.replace\(\'(.*?)\'\)')
		try:
			login_url = p.search(text).group(1)
			print urllib.unquote(login_url)
			print '-----------'
			result=urllib2.urlopen(login_url)
			text = result.read()
			print text
			self.uid = re.findall('"uniqueid":"(\d+)",',text)[0]
			print self.uid
			print "登录成功!"
		except Exception,e:
			print e
			print 'Login error!'
	def followed(self,dstuid):
		followedurl = "http://weibo.com/aj/f/followed?ajwvr=6&__rnd=%s"% int(time.time())
		data = {
				'uid':'%s'%dstuid,
				'rank':'0',
				'location':'mblog',
				'_t':'0',
				'extra':'',
				'f':'1',
				'oid':'%s'%self.uid,
				'nogroup':'false',
				'challenge_uids':'',
				'check_challenge_value':'',
				'location':'home',
				'refer_sort':'card',
				'refer_flag':'followed',
				'refer_flag':'0000020001_',
				'refer_lflag':'',
				'template':'1',
				}
		# headers['set-cookie'] = resp.headers['set-cookie']
		headers.update(Referer='http://weibo.com/u/'+self.uid+'?topnav=1&wv=5')
		result=http('POST',followedurl,headers,**data)
		default_logger.info('-----------------result-----------------------------------')
		default_logger.info(result)
		default_logger.info('----------------------------------------------------')
		result=json.loads(result)
		if result['code'] == '100000':
			return True
		else:
			default_logger.info('-----------------fail msg-----------------------------------')
			default_logger.info(result['msg'])
			default_logger.info('----------------------------------------------------')
			return False
	def send_blog(self,blog_title,blog_body,blog_class,tag,vtoken,blog_vote=None):
		vote={
			'voteId':'',
			'blogVote':'yes',
			'voteType':'1',
			'voteTitle':'我 是 一  个 中 国 人   哈',
			'voteData[]':'1111',
			'voteData[]':'2222',
			'voteData[]':'3333',
			'voteData[]':'4444',
			'voteData[]':'',
			'rad':'on',
			'votePos':'0',
			'voteYear':'2016',
			'voteMonth':'8',
			'voteDay':'5',
			'voteHour':'10',
		}
		assoc={
			'assoc_article':'3d837c2c0102whmy,3d837c2c0100c4wm',
			'assoc_style':'1',
			'assoc_article_data':'',
		}
		kw={
			'ptype':'',
			'teams':'',
			'worldcuptags':'',
			'album':'',
			'album_cite':'',
			'blog_id':'',
			'is_album':'0',
			'old365':'0',
			'stag':'',
			'sno':'',
			'book_worksid':'',
			'channel_id':'',
			'url':'',
			'channel':'',
			'newsid':'',
			'fromuid':'',
			'wid':'',
			'articletj':'',
			'vtoken':'vtoken',
			'is_media':'0',
			'is_stock':'0',
			'is_tpl':'0',
			'assoc_article':'',
			'assoc_style':'1',
			'assoc_article_data':'',
			'article_BGM':'',
			'xRankStatus':'',
			'commentGlobalSwitch':'',
			'commenthideGlobalSwitch':'',
			'articleStatus_preview':'1',
			'source':'',
			'topic_id':'0',
			'topic_channel':'0',
			'topic_more':'',
			'utf8':'1',
			'conlen':'15',
			'date_pub':'2016-06-04',
			'time':'22:16:37',
			'new_time':'',
			'isTimed':'0',
			'immediatepub':'0',
			'blog_title':'this is title9',
			'blog_body':'this is content9',
			'blog_class':'2',
			'tag':'tag1,tag2,tag3,tag4,健康',
			'x_cms_flag':'0',
			'sina_sort_id':'117',
		}
		kw['blog_title']=blog_title
		kw['blog_body']=blog_body
		kw['blog_class']=blog_class
		kw['date_pub']=datetime.datetime.now().strftime('%Y-%m-%d')
		kw['time']=datetime.datetime.now().strftime('%H:%M:%S')
		kw['tag']=tag
		kw['vtoken']=vtoken
		try:
			assoc_article = json.load(open('D:/mywork/tmall/assoc_user_%s.json'%u, 'r'),strict=False)
		except:
			assoc_article=None
		if assoc_article:
			assoc['assoc_article']=','.join(assoc_article)
			kw.update(**assoc)
		if blog_vote:
			kw.update(**blog_vote)
		headers.update(Referer='http://control.blog.sina.com.cn/admin/article/article_add.php')
		result=http('POST','http://control.blog.sina.com.cn/admin/article/article_post.php',headers,**kw)

		default_logger.info('-----------------result-----------------------------------')
		default_logger.info(result)
		default_logger.info('----------------------------------------------------')
		result=json.loads(result)
		if result['code'] == 'B06001':
			result_id=result['data']
			if not assoc_article:
				assoc_article=[]
			assoc_article.insert(0,result_id)
			del assoc_article[10:]
			json.dump(assoc_article, open('D:/mywork/tmall/assoc_user_%s.json'%u, 'w'))
		# default_logger.info('-----------------kw-----------------------------------')
		# default_logger.info(kw)
		# default_logger.info('----------------------------------------------------')

if __name__ == '__main__':
	USER={'user1':('goldhwi','password','5fbb7ffc7f53585700e3ec0ba815ae5d'),'user2':('hulianjiang@15yueliang.com','password','fd89d92014211a8cf3632814249f115e')}
	user=USER.get('user2')
	u=User(user[0],user[1],user[2])
	u.login()
	print u.uid,u.blog_vtoken
	# login(USER.get('user%s'%u)[0],USER.get('user%s'%u)[1])
	# u.followed('5796716770')
	# sheet=5
	# process(sheet,u)