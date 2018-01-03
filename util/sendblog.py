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

log_console = logging.StreamHandler(sys.stderr)
default_logger = logging.getLogger(__name__)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)

USER={'user1':('goldhwi','password','5fbb7ffc7f53585700e3ec0ba815ae5d'),'user2':('hulianjiang@15yueliang.com','password','fd89d92014211a8cf3632814249f115e')}

head_desc=u'''
<div style='padding:0 0 20px 0'>
		<span style="padding:10px 10px;float:left;line-height:30px;overflow:hidden;color:#26afd9;font-size:14px;font-weight:bold;border:4px solid #ebebeb;">%s
		</span>
		<div style="clear:both; height:0px; font-size:1px; overflow:hidden;"></div>
</div>
'''
head_info=u'''
<div style="margin:0; padding:3px 5px; background-color:#c00;margin:0; width:462px; height:120px; overflow:hidden;">
		<a href='%(head_info_link)s' rel='nofollow' targe='_blank'><img src="%(head_info_pic)s" style="width: 120px;float: left;height: 120px;margin-right: 15px;" alt="%(head_info_title)s"></a>
		<div style="margin:0; padding:0; line-height:36px; height:100px; overflow:hidden; font-size:24px; font-family:黑体;">
			<a href='%(head_info_link)s' style="text-decoration: none;" rel='nofollow' targe='_blank'><span style="color:#fff;">%(head_info_title)s</span></a>
		</div>
		<div style="background-color:#449d44;height:20px;line-height:20px;float:right">
		<a href='%(head_info_category_link)s' targe='_blank'><span style="background-color:#449d44;color:#fff;line-height:20px;text-decoration: none;font-size:12px; height:20px;line-height:20px;float:right">%(head_info_category)s</span></a>
		</div>
	</div>
'''
rel_body_item=u'''
<div style="margin:0 20px 10px 0; padding:0; float:left; width:240px; display:inline; overflow:hidden;">
			<div style="margin:0; padding:0; width:240px; height:240px; overflow:hidden; position:relative;">
				<a href='%(link)s' rel='nofollow' targe='_blank'><img src="%(pic)s" style="width: 240px;height: 240px;" alt="%(cel_title)s"></a>
			</div>
			<div style="margin:10px 0 0 0; padding:0 0 0 10px; color:#ff0005; border-left:2px solid #ff0005; line-height:23px; height:23px; overflow:hidden; width:204px; font-size:14px;word-wrap:break-word; word-break:break-all;">
			<a href='%(link)s' rel='nofollow' targe='_blank'>%(cel_title)s</a>
			</div>
			<div style="margin:0; padding:5px 0 0 10px; height:88px; width:204px; overflow:hidden; border-left:2px solid #3c3c3c; color:#888; line-height:18px; font-size:12px;word-wrap:break-word; word-break:break-all;">
				<a href='%(link)s' rel='nofollow' targe='_blank'>%(reason)s</a>
			</div>
		</div>
'''
body=u'''
<div style='box-sizing:border-box;text-decoration: none;'>
	%(head_desc)s
	%(head_info)s
	<div style="margin:0; padding:20px 0 0 0; height:%(rel_body_height)s; width:520px; overflow:hidden;">
		%(rel_body)s
		<div style="clear:both; height:0px; font-size:1px; overflow:hidden;"></div>
	</div>
	<div style="margin:0; padding:12px 10px 0 0;  height:4px; overflow:hidden;">
		<img src="http://simg.sinajs.cn/blog7style/images/blog/editor_format/bg_color2.gif" alt="" style="width:100%%;">
	</div>
<div style="padding: 0px 0px 0px 21px; height: 22px; line-height: 22px; font-size: 12px; background-image: url(&quot;http://simg.sinajs.cn/blog7style/images/blog/editor_format/bg_editor.gif&quot;); background-attachment: initial; background-size: initial; background-origin: initial; background-clip: initial; background-position: 0%% 50%%; background-repeat: no-repeat;">
	<span style="color:#29b1d7;">作者：</span><a href='http://www.15yueliang.com/' targe='_blank'><span style="color:#ff01af;">十五的月亮</span></a></div>
</div>
'''

def read_json(path):
	d = json.load(open(path, 'r'),strict=False)
	return d


def process(sheet,u):
	word=[]
	name=['shouji','jiaju','qiche','guoji','meizhuang','xiansheng']
	d=read_json('D:/mywork/tmall/tmall_618_blog_%s.json'%name[sheet])
	for i in range(len(d)):
		if i!=6:
			continue;
		head=d[i]
		left=[item for item in d if item['iid'] and item['iid'] != head['iid']]
		blog_title=u'%s'%head['cel_title']
		blog_class='1'
		tag=head['tags']
		ref_key=u'%s %s'%(head['cel_title'] if head['cel_title'] else '',head['title'] if head['title'] else '')
		r=http('GET','http://127.0.0.1:8983/solr/category/select',q='name:%s'%escape_solr(ref_key),rows='1',wt='json')
		docs=json.loads(r).get('response').get('docs')
		if len(docs) == 0:
			head['head_category']=u'十五月亮网'
			head['head_category_link']='http://www.15yueliang.com/'
		else:
			three_id=docs[0].get('cid')
			cat_name=docs[0].get('name')
			head['head_category']=cat_name
			head['head_category_link']='http://www.15yueliang.com/tao/guonei/fenlei/%s/tmall'%open_yueliang_config.get_yueliang_cat_tag(None,None,three_id)
		head_desc_=head_desc%head['reason']
		head_info_dic={}
		head_info_dic.update({
			# 'head_info_link':head['link'],
			'head_info_link':head['link'],
			'head_info_pic':head['pic'],
			'head_info_title':head['cel_title'],
			'head_info_category':head['head_category'],
			'head_info_category_link':head['head_category_link'],
			})

		head_info_=head_info%(head_info_dic)
		per_row=2
		# default_logger.info(left)
		# default_logger.info(len(left))
		rel_body_height=int(ceil(len(left) / float(per_row)))*(88+23+10+240+10)
		rel_body=[]
		for left_item in left:
			rel_body.append(rel_body_item%left_item)
		# default_logger.info(len(rel_body))
		body_dic={
			'head_desc':head_desc_,
			'head_info':head_info_,
			'rel_body_height':u'%spx'%rel_body_height,
			'rel_body':''.join(rel_body)
		}

		blog_body=body%(body_dic)
		# default_logger.info('----------------------------------------------------')
		# default_logger.info(blog_body)
		# default_logger.info('----------------------------------------------------')
		send_blog(blog_title,blog_body,blog_class,tag,u=u)


#http://bbs.csdn.net/topics/390083000解决B06013要加refferft
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
}
# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
# }
