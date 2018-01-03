# -*- coding: utf-8 -*-
from urllib2 import unquote
from urllib import urlencode
import httplib
import hashlib
import os.path
import hmac
import json
import binascii
#from M2Crypto import RSA
from base64 import b64decode
import cPickle as pickle

def test2():
	print len(u'汉')
	print len(u'汉'.encode('utf-8'))
    # u="\u5145\u503c\u6210\u529f"
	print u'\u5145\u503c\u6210\u529f'.encode('utf-8')
	c=u'充值成功'
	print c.encode('utf-8')
	custom=unquote(u"%E6%94%AF%E4%BB%98%E6%88%90%E5%8A%9F")
	print len(custom)
    # custom=unquote(str(u"\xc7\xeb\xb5\xc7\xc2\xbcexmail.qq.com\xd0\xde\xb8\xc4\xc3\xdc\xc2\xeb")).decode("utf8")
	# print u'\xc7\xeb\xb5\xc7\xc2\xbcexmail.qq.com\xd0\xde\xb8\xc4\xc3\xdc\xc2\xeb'
	print repr('\xc7\xeb\xb5\xc7\xc2\xbcexmail.qq.com\xd0\xde\xb8\xc4\xc3\xdc\xc2\xeb'.decode('gbk'))
	print u'\u8bf7\u767b\u5f55exmail.qq.com\u4fee\u6539\u5bc6\u7801'.encode('utf8')
    # print repr(custom).encode('gbk')
    # print repr('\xba\xba'.decode('gb2312'))
def valid_value(value):
        "Check to see if the provided value is a valid choice"
        for k, v in self.choices:
            if isinstance(v, (list, tuple)):
                # This is an optgroup, so look inside the group for options
                for k2, v2 in v:
                    if value == smart_unicode(k2):
                        return True
            else:
                if value == smart_unicode(k):
                    return True
        return False

def is_chinese(uchar):  
    """判断一个unicode是否是汉字"""  
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':  
        return True  
    else:  
        return False  
  
def is_number(uchar):  
    """判断一个unicode是否是数字"""  
    if uchar >= u'\u0030' and uchar<=u'\u0039':  
        return True  
    else:  
        return False  
  
def is_alphabet(uchar):  
    """判断一个unicode是否是英文字母"""  
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):  
        return True  
    else:  
        return False  
  
def is_other(uchar):  
    """判断是否非汉字，数字和英文字符"""  
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):  
        return True  
    else:  
        return False  
  
def B2Q(uchar):  
    """半角转全角"""  
    inside_code=ord(uchar)  
    if inside_code<0x0020 or inside_code>0x7e: #不是半角字符就返回原来的字符  
        return uchar  
    if inside_code==0x0020: #除了空格其他的全角半角的公式为:半角=全角-0xfee0  
        inside_code=0x3000  
    else:  
        inside_code+=0xfee0  
    return unichr(inside_code)  
  
def Q2B(uchar):  
    """全角转半角"""  
    inside_code=ord(uchar)  
    if inside_code==0x3000:  
        inside_code=0x0020  
    else:  
        inside_code-=0xfee0  
    if inside_code<0x0020 or inside_code>0x7e: #转完之后不是半角字符返回原来的字符  
        return uchar  
    return unichr(inside_code)  
  
def stringQ2B(ustring):  
    """把字符串全角转半角"""  
    return "".join([Q2B(uchar) for uchar in ustring])  
  
def uniform(ustring):  
    """格式化字符串，完成全角转半角，大写转小写的工作"""  
    return stringQ2B(ustring).lower() 
def pk():
    a=[u'深圳',u'15yueliang']
    print len(pickle.dumps(a))
def get_mail_domain(m1):
    m=m1.split('@')
    if m1.find('.com'):
        pre=m1.split('.com')[0]
    elif m1.find('.net'):
        pre=m1.split('.net')[0]
    elif m1.find('.cn'):
        pre=m1.split('.cn')[0]
    else:
        pre=''
    return 'http://mail.%s'%(m[1]),'登陆%s邮箱'%(pre)
def test_for():
    aa=[('1','11','111'),('2','22','222')]
    for i in range(len(aa)):
        if aa[i][0] == '2':
            # a=('2','22','222222')
            break
    else:
        print 'nnnnn' 
    aa[i]=('2','22','222222')
    print aa
if __name__ == '__main__':
    # test2()
    # valid_value()
    # print is_chinese(u'我')
    # print B2Q(u',')
    # pk()
    # print get_mail_domain('13@qq.com')
    test_for()