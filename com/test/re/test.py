# -*- coding: utf-8 -*-

# import Image
import os,re
import string

def test1():
    result=u'<p><strong>共k</strong>和国<strong>成立</strong>了'
    result,num=re.subn(r'<strong>([^strong]*)</strong>([^strong]+)', r'\2d', result,flags=re.DOTALL)
    print num,result.encode('utf-8')
    result=u'<p>d<strong>国成立</strong>c</p>'
    result,num=re.subn(r'<strong>(?P<mp>(.(?!<strong>))*)</strong>(?P<hp>[^<]+)', r'\g<mp>\g<hp>', result,flags=re.DOTALL)
    print num,result.encode('utf-8')
    result=u'<p><strong>共和国成立</strong>了'
    def _rep_strong(matched):
        return '11%s22%s'%(matched.group(1),matched.group(2));
    result,num=re.subn(r'<strong>(.*)</strong>([^\\S]+)', _rep_strong, result,flags=re.DOTALL)
    print num,result.encode('utf-8')
    p='(.*)(?!Asimov)'
    c = re.compile(p)
    print c.match('Isaac Asimov')
 
def test2():
    def _url_replace(matchobj):
        return '<a href=\'http://www.15yueliang.com\'>%s</a>'%matchobj.group('mp')
    a='''<a go='http://wwwbaidu.com'>123</a>456<a go='http://www.youxi.com'>112233</a>'''
    rs=re.subn('<a go=\'.*?\'>(?P<mp>.*?)</a>',_url_replace,a)
    print rs
def test3():
    s='<div class="goods_ref" itemprop="6910"><a isconvert="1" href="http://detail.tmall.com/item.htm?id=43538143059" rel="nofollow" target="_blank"><img src="http://img2.tbcdn.cn/tfscom/i3/749311050/TB2Zt9XhFXXXXXhXpXXXXXXXXXX_!!749311050.jpg"/></a><a isconvert="1" href="http://detail.tmall.com/item.htm?id=43538143059" rel="nofollow" target="_blank"><h3>贝亲 多功能授乳枕 喂奶枕孕妇哺乳枕哺乳枕垫喂奶护腰 婴儿抱枕</h3></a><div class="info"><em>价格:</em><span class="price">249.00元包邮</span><span class="mall"><a href="http://www.15yueliang.com/go/tmall/mall/0.html" rel="nofollow" target="_blank">天猫</a></span><span class="volume">销量:27</span></div><div class="ad"></div></div>'
    
    m=re.match(r'<div class=["\']{1}goods_ref["\']{1}.*?</div></div>',s)
    print m


if __name__ == '__main__':    
    # print test2()%({'meida_url':'http://www.youxi16.com'})
    # test2()
    test3()