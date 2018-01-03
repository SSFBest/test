#-*- coding: utf-8 -*-
'''
Created on 2010-5-27

@author: Administrator
'''
import datetime, time, md5
import os

class Util:
    def __init__(self):
       pass
    def getRandomStr(self):
        import random
        print [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
        str = ''.join(random.sample([chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)], 16))
        print str
    def onTime(self):
        starttime = datetime.datetime.now()
        time.sleep(1)
        endtime = datetime.now()
        print (endtime - starttime).seconds
        
    def ondate(self):
        d1 = datetime.datetime(2005, 2, 16)
        d2 = datetime.datetime(2004, 12, 31)
        print (d1 - d2).days
    def ondate2(self):
        #日期转字符串
        print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #字符串转日期
        date_string = "2010-06-22 0:45:32"
        format = "%Y-%m-%d %H:%M:%S"
        yesterday = datetime.datetime.strptime(date_string, format)
        
        print yesterday + datetime.timedelta(0, 3300)
        print datetime.date(2010, 06, 22) + datetime.timedelta(1, 20)
        print (datetime.datetime.now() - yesterday)
        #得到datetime中的年
        print yesterday.year;
        print yesterday.month;
        print yesterday.day;
        now = datetime.datetime.now()
        today = datetime.date.today()
        #
        mo_dt = datetime.datetime.strftime(today + datetime.timedelta(days=1), '%Y-%m-%d 00:00:00')
        print mo_dt
        mo_dt = datetime.datetime.strptime(mo_dt, '%Y-%m-%d %H:%M:%S')
        print mo_dt
        in_time = (mo_dt - now).seconds
        print in_time
        #
        print (datetime.datetime.strptime(datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d 00:00:00'), '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(datetime.datetime.strftime(yesterday, '%Y-%m-%d 00:00:00'), '%Y-%m-%d %H:%M:%S')).days
       # print datetime.datetime.now().today()-datetime.date(2010,06,23)
def datetostr():
    dt = datetime.datetime(2010, 7, 31, 0, 8, 53)
    print dt.strftime("%Y-%m-%d %H:%M:%S")
def test_dic():
    dic = {'guido': 4127, 'irv': 4127, 'jack': 4098}
    for name in dic:
        print name
    d={1:100,2:200}
    for (k,v) in d.items():
        print k,v

def test_list():
    l = [{u'content': u'llll', u'url': u'http://www.sina.com.cn', u'category': None, u'id': 1L, u'title': u'jjj'}]
    for n in l:
        print n["url"]
def test_get():
    lang_locale = {
    'default' : 'en',
    'en' : 'en',
    'zh' : 'zh'
}
    locale = 'e'
    language = lang_locale.get(locale, 'default')
    print language
def test_var():
    i = 2
    i = +2
    print i
def test_datastru():
    s1 = [1, 2, 3, 6, 7, 9, 4]
    s2 = [3, 4, 5, 6]
    v = set(s1).intersection(s2)
    print v
    for i in v:
        print i
    print 3 * len(v)
    s1.remove(9)
    print s1
def test_list3():
    l = [u'45351169', u'60610946', u'49610891', u'38380100', u'52986295', u'23282848']
    u = '49610891'
    ifhaveInvted = False
    for i in l:
        if i == u:
            ifhaveInvted = True
            break
    print ifhaveInvted
def test_md5():
    a = ["2", "4"]
    vsig = md5.new(str('c5ad6f56a7f61c0f0d5c4c59834f80a4a0860507') + str(len(a))).hexdigest()
    print vsig
    import hashlib
    vsig = hashlib.md5(str('c5ad6f56a7f61c0f0d5c4c59834f80a4a0860507') + str(len(a))).hexdigest()
    print vsig
    vsig = hashlib.md5("12345678" + str('c5ad6f56a7f61c0f0d5c4c59834f80a4a0860507') + "true" + "success").hexdigest()
    print vsig
def test_hmac():
    import hashlib # 2.5
    import hmac
    key = 'opennate_payment_shared_key'
    raw = 'payment_key=92558b40ed4f685f905d06e3fc1add4c&user_id=62119946&apps_no=0&item_id=1&item_type=F_COIN&item_name=Sunshine+DeepSea--1+K_coin&item_dotori=1&status=ready&passthrough=undefined'
    hashed = hmac.new(key, raw, hashlib.md5)
    print hashed.hexdigest()
def test_urlencode():
    import urllib
    str = urllib.urlencode({'name':'c d'});
    print str
    from urllib import unquote
    str = "http://192.168.0.66:20001/cw_Farm_trunk||farm_lib.models.handbook.Handbook||62119946&abc=d"
    print unquote(str)
    from urllib import quote
    print quote("http://192.168.0.66:20001/cw_Farm_trunk||farm_lib.models.handbook.Handbook||62119946")
def test_replace():
    def tagRender(tag, tag_dict):
        if '{*' in tag:
            for tag_d in tag_dict:
                if tag_d in tag:
                    try:
                        tag = tag.replace(tag_d, tag_dict[tag_d].encode('utf8'))
                    except:
                            tag = tag.replace(tag_d, tag_dict[tag_d])
    
        return tag
    def linkRender(link, link_dict):
        for tag_d in link_dict:
                if tag_d in link:
                    try:
                        link = link.replace(tag_d, link_dict[tag_d].encode('utf8'))
                    except:
                        link = link.replace(tag_d, link_dict[tag_d])
        return link
    tag_dict = {'{*actor*}':u'光辉',
                        '{*app_name*}':u'阳光深海',
                        '{*uid*}':'62119946',
                        '{*app_id*}':'95',
                        '{*friend_id*}':'62379949',
                        }
    tagDict = {"{*sea_name*}":"中南海"}
    if tagDict:
                for tagk in tagDict:
                    tag_dict[tagk] = tagDict[tagk]
    link_dict = {
                       '{homelink}':'<a href = \'http://minihp.cyworld.com/pims/main/pims_main.asp?tid={*friend_id*}&urlstr=myap\'>',
                       '{gamelink}':'<a href = \'http://appstore.nate.com/Main/View?apps_no=1065\'>',
                       '{endlink}':'</a>'
                       }
    tag = "{homelink}{*actor*}{endlink}님이  {gamelink}햇빛목장<endlink>에서 렙업되었습니다.  축하해주{*sea_name*}세요."
    print linkRender(tag, link_dict)
    print tagRender(linkRender(tag, link_dict), tag_dict)
def test_unicode():
    dd = u"\u30e9\u30a4\u30d6\u30e9\u30ea\u30fc\u3078\u3088\u3046\u3053\u305d\uff01\u697d\u3057\u304f\u96c6\u3081\u3066\u8cde\u54c1\u3092\u30b2\u30c3\u30c8\u3057\u3088\u3046\uff01"
    print dd
def test_data():
    data = {"status": {"normal": True, }}
    if data and data.has_key("feed_data"):
        feed_data = data['feed_data']
        print feed_data
def test_dic2():
    import datetime
    nowdate = datetime.datetime.now()
    now_date = datetime.datetime.strftime(nowdate, '%Y-%m-%d')
    christmas_goodbaby = {'getGift': [100, 50], 'score': 140, 'lastdate': '2010-12-03', '2010-12-03': 14}
    christmas_goodbaby.update({now_date:0})
    print christmas_goodbaby

def test_kye():
    SHARD_DISPATCH_PASSWORD = {
        (0x00, 0x1f) : '0',
        (0x20, 0x3f) : '1',
        (0x40, 0x5f) : '2',
        (0x60, 0x7f) : '3',
        (0x80, 0x9f) : '4',
        (0xa0, 0xbf) : '5',
        (0xc0, 0xdf) : '6',
        (0xe0, 0xff) : '7',
        }
    SHARD_INDEX_TABLE = [None for x in range(0, 256)]
    print SHARD_INDEX_TABLE
    for item in SHARD_DISPATCH_PASSWORD :
        print item
        if type(item) == tuple :
            print "is tuple"
            print item[0], item[1] + 1
            for i in range(item[0], item[1] + 1):
                print i
                print SHARD_DISPATCH_PASSWORD[item]
                SHARD_INDEX_TABLE[i] = SHARD_DISPATCH_PASSWORD[item]
        elif type(item) == int:
            SHARD_INDEX_TABLE[item] = SHARD_DISPATCH_PASSWORD[item]
    
    key_md5 = md5.md5("hu").hexdigest()
    print 'key_md5', key_md5
    print 'int key md5:', key_md5[:2]
    shard_index = SHARD_INDEX_TABLE[int(key_md5[:2], 16)]
    print shard_index;
def testXrange():
    print range(10)
    print xrange(10)
    for i in xrange(10):
        print i
    for i in range(10):
        print i
def get_cond(**condition):
        cond = None
        for f in condition:
            if f.endswith('_gt'):
                field = f[0:-3]
                if cond:
                    cond = cond + ['%s > %s'%(field,condition[f])]
                else:
                    cond = ['%s > %s'%(field,condition[f])]
            elif f.endswith('_lt'):
                field = f[0:-3]
                if cond:
                    cond = cond + ['%s < %s'%(field,condition[f])]
                else:
                    cond = ['%s < %s'%(field,condition[f])]
            
            elif f.endswith('_gte'):
                field = f[0:-4]
                if cond:
                    cond = cond + ['%s >= %s'%(field,condition[f])]
                else:
                    cond = ['%s >= %s'%(field,condition[f])]
            
            elif f.endswith('_lte'):
                field = f[0:-4]
                if cond:
                    cond = cond + ['%s <= %s'%(field,condition[f])]
                else:
                    cond = ['%s <= %s'%(field,condition[f])]
            elif f.endswith('_not'):
                field = f[0:-4]
                if cond:
                    cond = cond + ['%s != %s'%(field,condition[f])]
                else:
                    cond = ['%s != %s'%(field,condition[f])]
            else:
                field = f
                if cond:
                    cond = cond + ['%s == %s'%(field,condition[f])]
                else:
                    cond = ['%s == %s'%(field,condition[f])]
        values = ' and '.join('%s' % value for value in cond)
        return values
def get_cond2(condition):
        cond = None
        condition=sorted(condition, key=lambda w: w[2])
        for f in condition:
            if f[0].endswith('_gt'):
                field = f[0][0:-3]
                if cond:
                    cond = cond + ['%s > %s'%(field,f[1])]
                else:
                    cond = ['%s > %s'%(field,f[1])]
            elif f[0].endswith('_lt'):
                field = f[0:-3]
                if cond:
                    cond = cond + ['%s < %s'%(field,f[1])]
                else:
                    cond = ['%s < %s'%(field,f[1])]
            
            elif f[0].endswith('_gte'):
                field = f[0:-4]
                if cond:
                    cond = cond + ['%s >= %s'%(field,f[1])]
                else:
                    cond = ['%s >= %s'%(field,f[1])]
            
            elif f[0].endswith('_lte'):
                field = f[0:-4]
                if cond:
                    cond = cond + ['%s <= %s'%(field,f[1])]
                else:
                    cond = ['%s <= %s'%(field,f[1])]
            elif f[0].endswith('_not'):
                field = f[0:-4]
                if cond:
                    cond = cond + ['%s != %s'%(field,f[1])]
                else:
                    cond = ['%s != %s'%(field,f[1])]
            else:
                field = f[0]
                if cond:
                    cond = cond + ['%s == %s'%(field,f[1])]
                else:
                    cond = ['%s == %s'%(field,f[1])]
        values = ' and '.join('%s' % value for value in cond)
        return values
def sorttest():
    student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('dave', 'B', 10),
        ]
    t=sorted(student_tuples, key=lambda student: student[2])   # sort by age
    print t
def test_fu():
    # eval("new='me'")
    new='me'
    dic={}
    # dic[new]="myself"
    dic.update({new:'myself'})
    for key,value in dic.items():
        print key,value
    # exec('new=5')
    # print me
    new='abc'
    v='def'
    exec(new+'=v')
    print abc
def test_format():
    str='aa/%(year)s/%(month)s/%(day)s/'
    dic={'extname': u'jpg', 'datetime': '20140705115630', 'basename': u'ad2', 'year': '2014', 'filename': u'ad2.jpg', 'rnd': 362, 'time': '115630', 'month': '07', 'day': '05'}
    print str%dic
def test_urllib():
    import urllib
    urllib.basejoin("http://www.15" , OutputPathFormat)
def queryAllCategory():
    all_catagory=[{'upcid':0,'id':1},{'upcid':0,'id':2},{'upcid':1,'id':3},{'upcid':1,'id':4},{'upcid':2,'id':5},{'upcid':2,'id':6},{'upcid':3,'id':7},{'upcid':4,'id':8}]
    for item in all_catagory:
        yield item
def queryAllCategoryList():
    a=queryAllCategory()
    r={}
    for c in a:
        r.update({c['upcid']:[c]}) if not c['upcid'] in r else r[c['upcid']].append(c) 
    # for a.next():
        # print c
    # print [c for c in a]
    # r={c['upcid']:[c] if not c['upcid'] in r else r[c['upcid']].append(c) for c in a}
    print r

def test_bai():
    a ='bbb'
    print '%s'%('%'+a+'%')
def test_urllib():
    import urllib
    print urllib.basejoin('http://127.0.0.1/media/','aa/bb/cc.png')
    print os.path.join('http://127.0.0.1/media/','aa/bb/cc.png')
def test_yield():
    a=[1,2,3]
    if a:
        for i in a:
            yield i
def test_yield2():
    d=test_yield()
    for i in d:
        print i
def test_xinghao3(*parm):
    test_xinghao(*parm)
def test_xinghao(*parm):
    print parm
def test_xinghao2():
    a=[1,2,3]
    test_xinghao3(a)
def test_get():
    d={'1':{'id':1,'name':'joy1'}}
    print d['1']
    print d.get('1')
    # print d.'1'
    print d['1']['id']
    print d['1'].get('id')

    print d.get('1')['id']
    print d.get('1').get('id')
def remove_br(a):
    # print a[0]
    print '%s:%s'%(a[-2:],type(a[-2:]))
    # print a[-1:0]
    
    if a[-1:][0] in [u'女',u'男',u'春',u'夏',u'秋',u'冬']:
        return remove_br(a[0:-1])
    if a[-2:][0] in [u'女童',u'男童',u'春季',u'夏季',u'秋季',u'冬季',u'春夏',u'夏秋',u'秋冬',u'夏天']:
        return remove_br(a[0:-2])
    else:
        return a



if __name__ == '__main__':
    print __name__
    print remove_br(u'花花公子男鞋夏天')
    # util = Util()
    # test_get()
    # test_xinghao2()
    # test_yield2()
    # test_urllib()
    # test_bai()
    # queryAllCategoryList()
    # test_format()
    # test_fu()
#    datetostr()
    #util.onTime()
    #util.ondate()
#    util.ondate2()
    # test_dic()
#    test_list()
#    test_get()
#    test_var()
#    test_datastru()
#    test_list3()
#    test_md5()
#    test_hmac()
#    test_urlencode()
#    test_replace()
#    test_unicode()
#    test_data()
#    test_dic2()
    # test_kye();
#    testXrange()
#    util.getRandomStr()
#    tup2=('uid=62119946')
#    a+('finishtime > 1')
#    tup2 = ('abc', 'xyz')
#    tup3=('ddd','oo')
#    print tup2+tup3
#    print tup2
    # print get_cond(uid = 62119946, finishtime_gt = 1,abc = 2,abf = 3,ert=5)
    # print get_cond2([('uid',62119946,1), ('finishtime_gt',20,3),('abc',30,2),('abf',40,4),('ert',50,5)])
    # sorttest()
    # offset=1
    # if offset:
    #     print "ddd"
       
       
       
       
       
       
       
       
       
       
       
       
    
