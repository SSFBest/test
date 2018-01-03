#-*- coding: utf8 -*-
# import settings
# from django.core.management import setup_environ
# setup_environ(settings)
from PIL import Image,ImageFont,ImageDraw
import urllib2,io,re,random,math
# from yuelianglib.common.image import Graphics

'''
Created on 2010-7-23

@author: Administrator
'''
#from testimport.load_config import *
#from testimport import *

def createTable():
	print 'start clean tables'
	img = Image.open(r'C:\Users\LENOVO\Pictures\test\sprites-1.9.2.png')
	region = (200,165,213,173)

	#裁切图片
	cropImg = img.crop(region)

	#保存裁切后的图片
	cropImg.save(r'C:\Users\LENOVO\Pictures\test\crop.png')
def crop():
	def crop_pic(url_img,region):
		byte_img=urllib2.urlopen(url_img).read()
		data_img = io.BytesIO(byte_img)
		img = Image.open(data_img)
		# region = (0,0,180,180)

		#裁切图片
		cropImg = img.crop(region)

		#保存裁切后的图片
		cropImg.save(r'C:\Users\LENOVO\Pictures\test\new_crop.jpg' ,'jpeg',quality=100)
	if __name__ == '__main__':
		crop_pic('https://images-cn.ssl-images-amazon.com/images/G/28/PeterHsiao/2016/Promo/07-200-100/wml_160708_230170_book._V284250748_.jpg',(0,52,230,167))


def new_pic():

	def add_txt():

		mode='png'
		ext='png'
		quality=100

		image = Image.new('RGBA',(400,300),(92,184,92,255))
		# image = Image.new('RGBA',(width,height),color[0])
		#产生draw对象，draw是一些算法的集合
		txt = Image.new('RGBA', image.size, (255,255,255,0))
		draw = ImageDraw.Draw(txt)

		# draw.rectangle([0,0,logo_width,18],(217,0,47))
		draw.text((0,0),u'中国人',font=ImageFont.truetype('C:/windows/fonts/'+'msyhl.ttc',15),fill=(255,255,255),align='center')
		print draw.textsize(u'中国',font=ImageFont.truetype('C:/windows/fonts/'+'msyhl.ttc',15))
		del draw
		image = Image.alpha_composite(image, txt)
		#保存原始版本
		# print width,height
		# image.thumbnail((width,height))
		# if image.mode=='RGBA':
		# 	print 'dd'
		# 	background = Image.new('RGBA', image.size, (255, 255, 255,0))
		# 	# background.show()
		# 	background.paste(image,image)
		# 	image=background.convert('RGBA')
		image.save(r'E:\test\newpic.%s'%ext ,mode,quality=quality)
	def add_m_txt():

		mode='png'
		ext='png'
		quality=100

		image = Image.new('RGBA',(400,300),(92,184,92))
		# image = Image.new('RGBA',(width,height),color[0])
		#产生draw对象，draw是一些算法的集合
		txt = Image.new('RGBA', image.size, (255,255,255,0))
		draw = ImageDraw.Draw(txt)

		# draw.rectangle([0,0,logo_width,18],(217,0,47))
		draw.text((0,0),u'中国人民解放军\n爱中国\n好',font=ImageFont.truetype('C:/windows/fonts/'+'msyhl.ttc',15),fill=(255,255,255),align='center',spacing=0)
		print draw.textsize(u'中国人民解放军中国人民解放军中国人民解放军中国人民解放军中国人民解放军中国人民解放军\n爱中国\n好',font=ImageFont.truetype('C:/windows/fonts/'+'msyhl.ttc',15),spacing=20)
		del draw
		image = Image.alpha_composite(image, txt)
		#保存原始版本
		# print width,height
		# image.thumbnail((width,height))
		# if image.mode=='RGBA':
		# 	print 'dd'
		# 	background = Image.new('RGBA', image.size, (255, 255, 255,0))
		# 	# background.show()
		# 	background.paste(image,image)
		# 	image=background.convert('RGBA')
		image.save(r'E:\test\newpic.%s'%ext ,mode,quality=quality)
	def add_ml_txt():

		mode='png'
		ext='png'
		quality=100

		image = Image.new('RGBA',(400,300),(92,184,92))
		# image = Image.new('RGBA',(width,height),color[0])
		#产生draw对象，draw是一些算法的集合
		txt = Image.new('RGBA', image.size, (255,255,255,0))
		draw = ImageDraw.Draw(txt)

		# draw.rectangle([0,0,logo_width,18],(217,0,47))
		draw.multiline_text((0,0),u'中国人民\n中国好',font=ImageFont.truetype('C:/windows/fonts/'+'msyhl.ttc',15),fill=(255,255,255),align='center',spacing=0)
		# print draw.textsize(u'中国人民解放军中国人民解放军中国人民解放军中国人民解放军中国人民解放军中国人民解放军\n爱中国\n好',font=ImageFont.truetype('C:/windows/fonts/'+'msyhl.ttc',15),spacing=20)
		del draw
		image = Image.alpha_composite(image, txt)
		#保存原始版本
		# print width,height
		# image.thumbnail((width,height))
		# if image.mode=='RGBA':
		# 	print 'dd'
		# 	background = Image.new('RGBA', image.size, (255, 255, 255,0))
		# 	# background.show()
		# 	background.paste(image,image)
		# 	image=background.convert('RGBA')
		image.save(r'E:\test\newpic.%s'%ext ,mode,quality=quality)


	if __name__ == '__main__':
		# add_txt()
		# add_m_txt()
		add_ml_txt()



if __name__ == '__main__':
	# crop()
	new_pic()
	# new_pic2()