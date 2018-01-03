# -*- coding: utf-8 -*-

from yuelianglib.common.utils import print_err,get_err
import MySQLdb
from HTMLParser import HTMLParser

dbargs = dict(
			host='192.168.56.181',
			db='yueliangapps',
			user='developer_yl',
			passwd='12345678',
			charset='utf8',
			use_unicode=True,
		)
class GoHtmlParser(HTMLParser):

	def __init__(self):
		self.rt=[]

		HTMLParser.__init__(self)

	def handle_starttag(self,tag,attrs):
		if tag == 'li':
			for attr in attrs:
				if attr[0] == '_uin':
					qq=attr[1]
					self.rt.append(qq)
					break

		return

	def handle_endtag(self,tag):
		pass

	def handle_data(self,data):
		pass

	def handle_startendtag(self,tag, attrs):
		pass

	def handle_comment(self, data):
		# print 'comment'
		return
	def handle_entityref(self, name):
		pass
	def handle_charref(self, name):
		pass
def db_process(rt):
	conn = MySQLdb.connect(**dbargs)
	cursor=conn.cursor()
	for qq in rt:
		print qq
		cursor.execute("""
				SELECT mail FROM appsMails WHERE mail = %s
			""", (qq, ))
		ret = cursor.fetchall()
		if not ret:
			cursor.execute("""
						INSERT INTO appsMails (mail)
						VALUES (%s)
					""", (qq,))
	conn.commit()
	cursor.close()
	conn.close()
def gent_qq_num_2():
	f = open('123.txt', 'rb')
	print f,type(f)
	try:
		content=f.read()
		go=GoHtmlParser()
		go.feed(content)
		go.close()
		# go.rt=['41578974','1327298135','3327620009']
		# print go.rt
	except:
		print_err()
	else:
		db_process(go.rt)
	f.close()
def gent_qq_num():
	f = open('qun.txt', 'rb')
	print f,type(f)
	arr_qq=[]
	for lineno, line in enumerate(f, 1):
		try:
			line = line.strip()
			arr_qq.append(line)
		except:
			print_err()
	else:
		db_process(arr_qq)
	f.close()

if __name__ == '__main__':
	gent_qq_num()
