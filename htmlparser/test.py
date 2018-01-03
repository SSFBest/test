# encoding: utf-8

from HTMLParser import HTMLParser  
from htmlentitydefs import name2codepoint
  
page ='''
<p itemprop="description">
<script>
ffff
</script>
<!-- dddddd-->
<strong>铂胜&i智能系列小黄条国行新低价</strong>。&nbsp;
<a href="http://www.smzdm.com/gourl/B828F3DBB57C6E0A/AA_YH_163" target="_blank" onclick="gtmAddToCart({'name':'Crucial 英睿达 Ballistix 铂胜 智能LP 8G 低电压台式机内存','id':'6070767' , 'price':'239','brand':'crucial/英睿达' ,'mall':'京东', 'category':'电脑数码/电脑配件/内存/台式机内存','metric1':'239','dimension10':'jd.com','dimension9':'youhui','dimension11':'5阶价格','dimension12':'','dimension20':'无'})" rel="nofollow">
京东</a>
目前特价至239元包邮，国行新低价，1.35V标准电压下节能稳定、1.5V超频后卓越高速、丧心病狂的加外频的话非
专业请慎重考虑。窄条马甲的好处就是不怕大型散&#62热器的封杀。单双条套装可选也是让网友针对自己的平台可以有
更多选择。
</p>
'''  

class hp(HTMLParser):

    def __init__(self):
        self.rt=[]
        HTMLParser.__init__(self)


    def handle_starttag(self,tag,attrs):  
        # print 'start',tag
        if tag == 'a':
            return
        r='<%s'%tag
        for attr in attrs:
            # print " attr:", attr
            r='%s %s=\'%s\''%(r,attr[0],attr[1])
        r='%s>'%r
        self.rt.append(r)
              
    def handle_endtag(self,tag):
        if tag == 'a':
            return
        # print 'end',tag
        self.rt.append('</%s>'%tag)
    def handle_data(self,data):  
        if data.strip():
            # print 'data',data.strip()
            self.rt.append(data.strip())
    def handle_startendtag(self,tag, attrs):
        pass
    def handle_comment(self, data):
        print 'comment'
    def handle_entityref(self, name):
        try:
            c = unichr(name2codepoint[name])
            print "Named ent:", c.encode('utf-8')
        except Exception,e:
            self.rt.append('&%s'%name)
        else:
            self.rt.append(c.encode('utf-8'))
    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        # print "Num ent  :", c
        self.rt.append(c.encode('utf-8'))
    def handle_decl(self, data):
        # print "Decl     :", data
        pass
              
yk = hp()  
yk.feed(page)  
yk.close()  
print yk.rt
print ''.join(yk.rt)
