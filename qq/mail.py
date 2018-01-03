# -*- coding:utf-8 -*-
from django.core.mail import EmailMessage
import requests,datetime
from yuelianglib.common.utils import print_err,get_err
import MySQLdb,os,sys,simplejson

sys.path.append('d:/mywork/yueliang/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'apps.settings'
S={'API_USER':'15yueliang_no_reply','API_KEY':'ytx5BMt7G3VJ0hYV','FROM':'noreply@newsletter.15yueliang.com','FROM_NAME':'15月亮网(15yueliang.com)运营经理joy'}
plain_content1='''
您好,先生/女士,
     我们是15月亮网(15yueliang.com)运营团队,我们团队旨在目标国内一流的折扣搜索引擎,专做折扣搜索。
     我们自研折扣发现引擎网罗各大流电商优惠活动,及时发现折扣,优惠券,让你购物更省心,当然也更省钱。
     我们承诺我们绝不骚挠你,做最干净的折扣搜索。
     我们团队成员主要来自新浪网,京东还有阿里巴巴。
     目前我们正推出BETA版,还没有APP,但很快会有。
     我们再次承诺不挠民,不干坏事。不强求,如果你喜欢你可以来看看,多给我们提意见。
     意见邮箱:hulianjiang@15yueliang.com,也欢迎微信骚挠我:simplefastbest
                                                                   15月亮网运营经理joy。
'''
plain_content2='''
您好,先生/女士,
     我们是15月亮网(15yueliang.com)运营经理joy,恕我冒昧,今天我打挠你了。
     你之所以收到我们的邮件,是因为你曾经是我们的用户,但是你已经好一段时间没有访问我们的网站了。
     我们承诺绝不轻易骚挠你,放心绝不。
     15月亮网(15yueliang.com),是一个美丽的购物网站,但是我们不销售商品,你甚至不需要注册,因此不用担心你的信息泄露。
     我们是一个美丽的导购网站,我们保证所有商品信息全部来自主流电商:京东,天猫,1号店,亚马逊,你可放心购买。
     我们只是在帮你发现折扣,传播优惠信息之目的。
     目前我们正推出BETA版,还没有APP,但很快会有。
     意见邮箱:hulianjiang@15yueliang.com,也欢迎微信骚挠我:simplefastbest
                                                                   15月亮网运营经理joy。
'''
plain_content3='''您好,先生/女士,
     你收到我们的邮件,是因为你曾经是我们的用户,但是你已经好一段时间没有访问我们的网站了。
     15月亮网(www.15yueliang.com),一个美丽的购物网站,但我们不销售商品,我们帮你发现折扣,传播优惠信息。
     我们保证所有商品信息全部来自主流电商:京东,天猫,1号店,亚马逊,你可放心购买。
     目前我们只推出网站BETA版,还没有APP,但很快会有。
                                                                   15月亮网运营经理joy。
'''

html_content='''您好,先生/女士,
我们是15月亮网(<a href='http://www.15yueliang.com'>15yueliang.com</a>)运营团队,我们团队旨在目标国内一流的折扣搜索引擎,专做折扣搜索。
我们自研折扣发现引擎网罗各大流电商优惠活动,及时发现折扣,优惠券,让你购物更省心,当然也更省钱。
我们承诺我们绝不骚挠你,做最干净的折扣搜索。
我们团队成员主要来自新浪网,京东还有阿里巴巴。
目前我们正推出BETA版,还没有APP,但很快会有。
我们再次承诺不挠民,不干坏事。不强求,如果你喜欢你可以来看看,多给我们提意见。
15月亮网运营经理joy。意见邮箱:hulianjiang@15yueliang.com,也欢迎微信骚挠我:simplefastbest
'''
sendmail={
	'prefix':'m4',
	'title':u'这是标题',
    'm1':('smtp.exmail.qq.com',25,'service@youxi16.com','password',True),
    'm2':('smtp.163.com',25,'goldhwi@163.com','password&#!',True),#适合单独发用
    'm3':('smtp.qq.com',25,'41578974@qq.com','password',True),#不能用，要授权码
    'm4':('smtp.mxhichina.com',25,'service@15yueliang.com','password',False),
	}
dbargs = dict(
			host='192.168.56.181',
			db='yueliangapps',
			user='developer_yl',
			passwd='12345678',
			charset='utf8',
			use_unicode=True,
		)
mail_subject='欢迎你再回来体验15月亮网'
html_content,plain_content=None,plain_content3
def send_html_mail(subject, html_content, recipient_list,plain_content=None,connection=None):

    msg = EmailMessage(subject, html_content if html_content else plain_content,'%s<%s>'%('15月亮网运营经理joy',sendmail.get(sendmail.get('prefix'))[2]), recipient_list,connection=connection)
    if html_content:
    	msg.content_subtype = "html" # Main content is now text/html
    result = msg.send()
    return result
def sendcloud_html_mail(subject, html_content, recipient_list,plain_content=None,**kwargs):
	url = "http://api.sendcloud.net/apiv2/mail/send"
	print kwargs
	if not subject or (not html_content and not plain_content) or not recipient_list:
		raise
	print kwargs
	params = {
	    "apiUser": kwargs.get('API_USER') or SENDCLOUD.get('API_USER'), # 使用api_user和api_key进行验证
	    "apiKey" : kwargs.get('API_KEY') or SENDCLOUD.get('API_KEY'),
	    "to" : ';'.join(recipient_list), # 收件人地址, 用正确邮件地址替代, 多个地址用';'分隔
	    "from" : kwargs.get('FROM') or SENDCLOUD.get('FROM') , # 发信人, 用正确邮件地址替代
	    "fromName" : kwargs.get('FROM_NAME') or SENDCLOUD.get('FROM_NAME'),
	    "subject" : subject,
	    "useAddressList":"false"
	}
	if plain_content:
		params.update({'plain':plain_content})
	else:
		params.update({'html':html_content})
	# print params

	r = requests.post(url, files=None, data=params)
	return r.text
def db_process_mail():
	conn = MySQLdb.connect(**dbargs)
	cursor=conn.cursor()
	today=datetime.date.today()
	gt_time= today-datetime.timedelta(days=30)

	cursor.execute("""
				SELECT mail FROM appsMails WHERE refused is NULL and (updatetime is NULL or updatetime < %s) limit 200
			""", (gt_time, ))
	ret = cursor.fetchall()
	if ret:
		print 'ret:',ret
		from django.core import mail
		backend='yuelianglib.logics.smtp.EmailBackend'
		host,port,username,password,use_tls=sendmail.get(sendmail.get('prefix'))
		connection = mail.get_connection(backend,host=host,port=port,username=username,password=password,use_tls=use_tls)
		connection.open()
		for r in ret:
			print r,'%s@qq.com'%r[0]
			result=send_html_mail(mail_subject,html_content,['<%s@qq.com>'%r[0]],plain_content,connection)
			print result
			if result.get('num_sent') == 1:
				cursor.execute("""
					UPDATE appsMails SET updatetime=%s WHERE mail=%s
				""", (today,r[0]))
			if result.get('refused'):
				cursor.execute("""
					UPDATE appsMails
					SET updatetime=%s,refused=1
					WHERE mail=%s
				""", (datetime.datetime.strftime(today,'%Y-%m-%d') + ' 00:00:00',r[0]))
		connection.close()

	conn.commit()
	cursor.close()
	conn.close()
def db_process_sendcloud():
	conn = MySQLdb.connect(**dbargs)
	cursor=conn.cursor()
	today=datetime.date.today()
	gt_time= today-datetime.timedelta(days=30)

	cursor.execute("""
				SELECT mail FROM appsMails WHERE refused is NULL and (updatetime is NULL or updatetime < %s) limit 200
			""", (gt_time, ))
	ret = cursor.fetchall()
	if ret:
		print 'ret:',ret

		for r in ret:
			print r,'%s@qq.com'%r[0]
			result=sendcloud_html_mail(mail_subject,html_content,['%s@qq.com'%r[0]],plain_content,**S)
			print result
			result=simplejson.loads(result)
			if result.get('statusCode') == 200:
				cursor.execute("""
					UPDATE appsMails SET updatetime=%s WHERE mail=%s
				""", (today,r[0]))
			if result.get('refused'):
				cursor.execute("""
					UPDATE appsMails
					SET updatetime=%s,refused=1
					WHERE mail=%s
				""", (datetime.datetime.strftime(today,'%Y-%m-%d') + ' 00:00:00',r[0]))

	conn.commit()
	cursor.close()
	conn.close()

if __name__ == '__main__':
	# db_process_mail()
	db_process_sendcloud()
	# sendcloud_html_mail('欢迎您体验15月亮网',None,['goldhwi@163.com'],plain_content,**S)