# -*- coding=utf-8 -*-
import urllib, urllib2, cookielib, sys, re

reload(sys)
sys.setdefaultencoding('utf-8')

__cookie = cookielib.CookieJar()
__req = urllib2.build_opener(urllib2.HTTPCookieProcessor(__cookie))
__req.addheaders = [
  ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
  ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36')
]

urllib2.install_opener(__req)

def Get(url):
  req = urllib2.Request(url)
  return urllib2.urlopen(req).read()

url = 'https://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto=10'

html = Get(url).replace('&', '&')

# print html

reForProduct = re.compile('<div class="product  " data-id="(\d+)"[\s\S]+?<p class="productPrice">\s+<em title="(.+?)">[\s\S]+?<p class="productTitle">\s+<a href="(.+?)" target="_blank" title="(.+?)"[\s\S]+?<\/div>\s+<\/div>')


#找到所有的 products
products = reForProduct.findall(html)

i = 0

reForShop = re.compile('<div class="extend">[\s\S]+?<a href="(.+?)".+?>(.+?)<\/a>[\s\S]+<div class="right">\s+(.+?)\s+<\/div>\s+<\/li>\s+<li class="locus">[\s\S]+?<div class="right">\s+(.+?)\s+<\/div>')


for (pid, price, url, title) in products:
    if url.startswith('//'):
      url = 'https:' + url

    print ("%s\t%s\t%s\t%s") % (pid, price, title, url)

    #仅为了演示, 此处只获取第一个搜索结果中的 店铺信息
    if i < 4:
      i = i + 1
      shopDetail = Get(url)
      shop = reForShop.findall(shopDetail)
      (shopUrl, shopName, companyName, companyAddress) = shop[0]

      if shopUrl.startswith('//'):
        shopUrl = 'https:' + shopUrl

      print ("%s\t%s\t%s\t%s") % (shopName, shopUrl, companyName, companyAddress)