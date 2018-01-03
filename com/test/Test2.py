# -*- coding: utf-8 -*-
from urllib2 import unquote
from urllib import urlencode
import httplib
import hashlib
import os.path
import hmac,re
import json
import binascii
#from M2Crypto import RSA
from base64 import b64decode
from xml.etree import ElementTree as ET
'''
Created on 2013-3-14

@author: Administrator
'''
def http_post(url, data=None, data_type = 'x-www-form-urlencoded',user_agent=''):
    res = None
    urlInfo = httplib.urlsplit(url)
    print(url)
    if url.find('https://')>-1:
        conn = httplib.HTTPSConnection(urlInfo.netloc,timeout=5)
    else:
        conn = httplib.HTTPConnection(urlInfo.netloc,timeout=5)
    try:
        conn.connect()
        
        if data:
            conn.putrequest("POST", urlInfo.path)
            conn.putheader("Content-Length", len(data))
            conn.putheader("Content-Type", "application/%s"%data_type)
            if url.find('gfan.com') > 0:
                conn.putheader("User-Agent",user_agent)
        else:
            conn.putrequest("GET", url)
            conn.putheader("Content-Length", 0)

        conn.putheader("Connection", "close")
        conn.endheaders()

        if data:
            conn.send(data)

        response = conn.getresponse()
        if response:
            res = response.read()
            response.close()
        
        return res
    except Exception, ex:
        raise ex
    
    conn.close()
def test():
    print 'hihi'
def testrsa():
    global g_rsa_foo
    data='ZrpB0Ow6pSeswlT853oh7JE1zzlVJc2qDyPag9OX9xb 8Sj1H7pTt1PEsLLFSERm4bQT9Agolk3sZc/3RVeQVYzVGAjzt3qs8eol 3kjSHBNR1bDPESBKXAW0WY9e0PTxOoPphyo00 vxR1cfMlj0vSOnHMJcv4rKEpjYD7inwuPD4ALZuSDQKnTtoHkrDX5OdpfNZy/WMd85ZzJqdQt3E7 AE9xaj3keT3H9wpAnUzpFJMZuSTMYS6rWokg8kaLiaH737o Ay2/FHsEYg/LYcCvGejwJWRjjn4jQ6Y4lXOOy GBGVgNML/WpTVWaoIqKQxXeNUtlVP7XD5oVI7Pbg=='
    b64string = b64decode(data)
    if not g_rsa_foo:
        pem_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'pphelper.pem'))
        g_rsa_foo = RSA.load_pub_key(pem_file)

    ctxt = g_rsa_foo.public_decrypt(b64string, RSA.pkcs1_padding)
    return json.loads(ctxt)
def testGetRequest():
    url=u'http://10.1.1.66/client/ads?para1=成功&para2=sucess'
    m={'_ym_url':url}
    callbackurl=urlencode(m)
    address='http://10.1.1.66/client/ads/youmi?_ym_uid=123456789&_ym_uid2=abcdefghijk&%s'%callbackurl
    print address
    result=http_post(address)
    print result
def testb64():
    token_key = b64decode("D19hUVX23AHWz5jw+N2dwQ==")
    print token_key
def md5(s):
    signStr=hashlib.md5() 
    signStr.update(s.encode('utf-8'))
    return signStr.hexdigest()
def test2():
    u="\u5145\u503c\u6210\u529f"
    c='充值成功'
    print c.decode('utf-8')
    custom=unquote(str(u"%E6%94%AF%E4%BB%98%E6%88%90%E5%8A%9F")).decode("utf8")
    custom=unquote(str(u"\\XF0\\X9F\\X98\\X81")).decode("utf8")
    print custom
def testBaidu():
    api_key = '3d3a0724013d8c7c86a0202a3dc6632c'
    secret_key = '8a9a5db83d3a0724013d3dc6632c202b'
   # dic={u'server_id': [u'24'], u'user_id': [u'1084290402'], u'order_id': [u'463a6152078636d80'], u'timestamp': [u'2013-03-28 16:05:45'], u'sign': [u'B7188F89FCADA4A2ED9E56F9142FBD74'], u'currency': [u'CNY'], u'amount': [u'200'], u'result': [u'1'], u'wanba_oid': [u'2013032847896074'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083746284'], u'order_id': [u'463a60b6b20d74bb0'], u'timestamp': [u'2013-03-28 16:06:30'], u'sign': [u'85CF9E38254A5BD6BE41CDDB09B15399'], u'currency': [u'CNY'], u'amount': [u'80'], u'result': [u'1'], u'wanba_oid': [u'2013032819161956'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084327021'], u'order_id': [u'463a66fb5d73756b0'], u'timestamp': [u'2013-03-28 16:09:36'], u'sign': [u'28F6E0068AFE5EFD64B56334E9A09D85'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032840766473'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084338712'], u'order_id': [u'463a637bc30edfe90'], u'timestamp': [u'2013-03-28 16:17:24'], u'sign': [u'E7010E4D6E937076C42C88F59B79D2DE'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032846163860'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1082548813'], u'order_id': [u'463a6f6de381c1260'], u'timestamp': [u'2013-03-28 16:21:43'], u'sign': [u'6AEA556E58E93EF4E436711CFEE592B7'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032846174360'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084327021'], u'order_id': [u'463a629f8b0dbab08'], u'timestamp': [u'2013-03-28 16:27:07'], u'sign': [u'DD8A34DA1968A1BDAAE970B1247A9E25'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032840812673'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083777006'], u'order_id': [u'463a615d0ba390a68'], u'timestamp': [u'2013-03-28 16:37:32'], u'sign': [u'B67F35AB46E2F649552B5E5C5E34129D'], u'currency': [u'CNY'], u'amount': [u'45'], u'result': [u'1'], u'wanba_oid': [u'2013032818525718'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084092239'], u'order_id': [u'463a6105851d396c8'], u'timestamp': [u'2013-03-28 16:43:33'], u'sign': [u'8EE7A033336EED6CF7A752C77291C532'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032864093993'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084126679'], u'order_id': [u'463a6e680e47de138'], u'timestamp': [u'2013-03-28 16:46:08'], u'sign': [u'EC2375EDF87DFDA13ACA2B5E828868F0'], u'currency': [u'CNY'], u'amount': [u'10'], u'result': [u'1'], u'wanba_oid': [u'2013032867297195'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084126679'], u'order_id': [u'463a6a60e0cd5a9e0'], u'timestamp': [u'2013-03-28 16:47:34'], u'sign': [u'32690BAF4F04DE1EC918692E775B6FE9'], u'currency': [u'CNY'], u'amount': [u'10'], u'result': [u'1'], u'wanba_oid': [u'2013032867299995'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083777006'], u'order_id': [u'463a6a90e4dff2a18'], u'timestamp': [u'2013-03-28 16:48:24'], u'sign': [u'572113330C74A9BD56448FDC5BFC39E3'], u'currency': [u'CNY'], u'amount': [u'5'], u'result': [u'1'], u'wanba_oid': [u'2013032818554318'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083777006'], u'order_id': [u'463a6de663a66b7a0'], u'timestamp': [u'2013-03-28 16:58:39'], u'sign': [u'6494795F239355046FDE720AD4EFF39E'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032818577318'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083869423'], u'order_id': [u'463a603a7d93146b0'], u'timestamp': [u'2013-03-28 16:59:52'], u'sign': [u'F188FDFDB0485DDC26E66A612E1C53D5'], u'currency': [u'CNY'], u'amount': [u'100'], u'result': [u'1'], u'wanba_oid': [u'2013032818580418'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083545586'], u'order_id': [u'463a6d9cd60efeff0'], u'timestamp': [u'2013-03-28 17:31:36'], u'sign': [u'251E766424A7E88BF0FAE1CDB58CC9C8'], u'currency': [u'CNY'], u'amount': [u'50'], u'result': [u'1'], u'wanba_oid': [u'2013032840980373'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
    dic={u'server_id': [u'24'], u'user_id': [u'1083545586'], u'order_id': [u'463a69e313d11dc88'], u'timestamp': [u'2013-03-28 17:42:05'], u'sign': [u'679D2EF1B5D63157C3C53184D2EC4E28'], u'currency': [u'CNY'], u'amount': [u'10'], u'result': [u'1'], u'wanba_oid': [u'2013032841008473'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
    dic={u'server_id': [u'125'], u'user_id': [u'943434947'], u'order_id': [u'463c1030ca80b7640'], u'timestamp': [u'2013-06-20 17:29:50'], u'sign': [u'DCE08651424DE85FCBB5482A1FA1A8FC'], u'currency': [u'CNY'], u'amount': [u'2000'], u'result': [u'1'], u'wanba_oid': [u'137095113085578374'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}

    sign_str = '%samount%s' % (secret_key, dic['amount'][0])
    sign_str += 'api_key' + api_key
    sign_str += 'back_send' + dic['back_send'][0]
    sign_str += 'currency' +  dic['currency'][0]
    sign_str += 'order_id' + dic['order_id'][0]
    sign_str += 'result' + dic['result'][0]
    sign_str += 'server_id' + '125'
    sign_str += 'timestamp' + dic['timestamp'][0]
    sign_str += 'user_id' + dic['user_id'][0]
    sign_str += 'wanba_oid' +dic['wanba_oid'][0]
    
    genSign=md5(sign_str)
    
    print "curl -d 'server_id=125&user_id=%s&order_id=%s&timestamp=%s&sign=%s&currency=CNY&amount=%s&result=%s&wanba_oid=%s&api_key=%s&back_send=%s' 'http://127.0.0.1/service/confirm/baidu' "%(dic['user_id'][0],dic['order_id'][0],dic['timestamp'][0],genSign,dic['amount'][0], dic['result'][0],dic['wanba_oid'][0],'3d3a0724013d8c7c86a0202a3dc6632c',dic['back_send'][0])    
def test91():
    app_id = int(109241)
    app_key = 'f0f4854f0e5dc0be395e34759cbb49d4edb08f0beb4904f6'
    dic={u'PayStatus': [u'1'], u'OriginalMoney': [u'100.00'], u'AppId': [u'109241'], u'ProductName': [u'\u6bd4\u6b66\u62db\u4eb2'], u'Note': [u'\u8d2d\u4e70\u5143\u5b9d'], u'CooOrderSerial': [u'0_17829328_b6cfa5cb4fb243129d'], u'GoodsId': [u'0'], u'Sign': [u'd86d3c40b08d25c37f61ddfc4cfa222c'], u'CreateTime': [u'2013-04-01 13:06:28'], u'ConsumeStreamId': [u'3-27397-20130401130723-10000-1380'], u'Act': [u'1'], u'GoodsCount': [u'1000'], u'Uin': [u'390177028'], u'GoodsInfo': [u'\u5143\u5b9d'], u'OrderMoney': [u'100.00'], u'ProductId': [u'109241']}
    Act = dic['Act'][0]
    ProductName = dic['ProductName'][0]
    ConsumeStreamId = dic['ConsumeStreamId'][0]
    CooOrderSerial = dic['CooOrderSerial'][0]
    Uin = dic['Uin'][0]
    GoodsId = dic['GoodsId'][0]
    GoodsInfo = dic['GoodsInfo'][0]
    GoodsCount = dic['GoodsCount'][0]
    OriginalMoney = dic['OriginalMoney'][0]
    OrderMoney = dic['OrderMoney'][0]
    Note = dic['Note'][0]
    PayStatus = dic['PayStatus'][0]
    CreateTime = dic['CreateTime'][0]
    Sign = dic['Sign'][0]
    

   # dic={u'server_id': [u'24'], u'user_id': [u'1084290402'], u'order_id': [u'463a6152078636d80'], u'timestamp': [u'2013-03-28 16:05:45'], u'sign': [u'B7188F89FCADA4A2ED9E56F9142FBD74'], u'currency': [u'CNY'], u'amount': [u'200'], u'result': [u'1'], u'wanba_oid': [u'2013032847896074'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083746284'], u'order_id': [u'463a60b6b20d74bb0'], u'timestamp': [u'2013-03-28 16:06:30'], u'sign': [u'85CF9E38254A5BD6BE41CDDB09B15399'], u'currency': [u'CNY'], u'amount': [u'80'], u'result': [u'1'], u'wanba_oid': [u'2013032819161956'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084327021'], u'order_id': [u'463a66fb5d73756b0'], u'timestamp': [u'2013-03-28 16:09:36'], u'sign': [u'28F6E0068AFE5EFD64B56334E9A09D85'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032840766473'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084338712'], u'order_id': [u'463a637bc30edfe90'], u'timestamp': [u'2013-03-28 16:17:24'], u'sign': [u'E7010E4D6E937076C42C88F59B79D2DE'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032846163860'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1082548813'], u'order_id': [u'463a6f6de381c1260'], u'timestamp': [u'2013-03-28 16:21:43'], u'sign': [u'6AEA556E58E93EF4E436711CFEE592B7'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032846174360'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084327021'], u'order_id': [u'463a629f8b0dbab08'], u'timestamp': [u'2013-03-28 16:27:07'], u'sign': [u'DD8A34DA1968A1BDAAE970B1247A9E25'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032840812673'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083777006'], u'order_id': [u'463a615d0ba390a68'], u'timestamp': [u'2013-03-28 16:37:32'], u'sign': [u'B67F35AB46E2F649552B5E5C5E34129D'], u'currency': [u'CNY'], u'amount': [u'45'], u'result': [u'1'], u'wanba_oid': [u'2013032818525718'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084092239'], u'order_id': [u'463a6105851d396c8'], u'timestamp': [u'2013-03-28 16:43:33'], u'sign': [u'8EE7A033336EED6CF7A752C77291C532'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032864093993'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084126679'], u'order_id': [u'463a6e680e47de138'], u'timestamp': [u'2013-03-28 16:46:08'], u'sign': [u'EC2375EDF87DFDA13ACA2B5E828868F0'], u'currency': [u'CNY'], u'amount': [u'10'], u'result': [u'1'], u'wanba_oid': [u'2013032867297195'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1084126679'], u'order_id': [u'463a6a60e0cd5a9e0'], u'timestamp': [u'2013-03-28 16:47:34'], u'sign': [u'32690BAF4F04DE1EC918692E775B6FE9'], u'currency': [u'CNY'], u'amount': [u'10'], u'result': [u'1'], u'wanba_oid': [u'2013032867299995'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083777006'], u'order_id': [u'463a6a90e4dff2a18'], u'timestamp': [u'2013-03-28 16:48:24'], u'sign': [u'572113330C74A9BD56448FDC5BFC39E3'], u'currency': [u'CNY'], u'amount': [u'5'], u'result': [u'1'], u'wanba_oid': [u'2013032818554318'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083777006'], u'order_id': [u'463a6de663a66b7a0'], u'timestamp': [u'2013-03-28 16:58:39'], u'sign': [u'6494795F239355046FDE720AD4EFF39E'], u'currency': [u'CNY'], u'amount': [u'1'], u'result': [u'1'], u'wanba_oid': [u'2013032818577318'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083869423'], u'order_id': [u'463a603a7d93146b0'], u'timestamp': [u'2013-03-28 16:59:52'], u'sign': [u'F188FDFDB0485DDC26E66A612E1C53D5'], u'currency': [u'CNY'], u'amount': [u'100'], u'result': [u'1'], u'wanba_oid': [u'2013032818580418'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
#    dic={u'server_id': [u'24'], u'user_id': [u'1083545586'], u'order_id': [u'463a6d9cd60efeff0'], u'timestamp': [u'2013-03-28 17:31:36'], u'sign': [u'251E766424A7E88BF0FAE1CDB58CC9C8'], u'currency': [u'CNY'], u'amount': [u'50'], u'result': [u'1'], u'wanba_oid': [u'2013032840980373'], u'api_key': [u'3d3a0724013d8c7c86a0202a3dc6632c'], u'back_send': [u'Y']}
    sign_str = '%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s'%(app_id,Act,ProductName,ConsumeStreamId,CooOrderSerial,Uin,GoodsId,GoodsInfo,GoodsCount,OriginalMoney,OrderMoney,Note,PayStatus,CreateTime,app_key)
    sign_str = md5(sign_str)
    
    print "curl -d 'PayStatus=%s&OriginalMoney=%s&AppId=%s&ProductName=%s&Note=%s&CooOrderSerial=%s&GoodsId=%s&Sign=%s&CreateTime=%s&ConsumeStreamId=%s&Act=%s&GoodsCount=%s&Uin=%s&GoodsInfo=%s&OrderMoney=%s&ProductId=%s' 'http://127.0.0.1/service/confirm/a91' "%(dic['PayStatus'][0],dic['OriginalMoney'][0],dic['AppId'][0],dic['ProductName'][0], dic['Note'][0],dic['CooOrderSerial'][0],dic['GoodsId'][0],sign_str,dic['CreateTime'][0],dic['ConsumeStreamId'][0],dic['Act'][0],dic['GoodsCount'][0],dic['Uin'][0],dic['GoodsInfo'][0],dic['OrderMoney'][0],dic['ProductId'][0])    

def testxiaomi():
    app_id = int(7932)
    app_key='97a80405-76ca-4f21-2614-514ac78344ed'
    dic={u'orderId': [u'21136860560513333436'], u'cpOrderId': [u'53_53021918_1368605604381'], u'payFee': [u'5000'], u'uid': [u'672426'], u'productCode': [u'01'], u'signature': [u'f14854c3cebd1b6e29909d3d9c7d1b46d79a245a'], u'productCount': [u'500'], u'productName': [u'\u5143\u5b9d'], u'orderStatus': [u'TRADE_SUCCESS'], u'cpUserInfo': [u'0'], u'appId': [u'7932'], u'payTime': [u'2013-05-15 16:13:54']}
    orderId = dic['orderId'][0]
    cpOrderId = dic['cpOrderId'][0]
    payFee = dic['payFee'][0]
    uid = dic['uid'][0]
    productCode = dic['productCode'][0]
    productCount = dic['productCount'][0]
    productName = dic['productName'][0]
    orderStatus = dic['orderStatus'][0]
    cpUserInfo = dic['cpUserInfo'][0]
    payTime = dic['payTime'][0]

    
    

    server_sign = u'appId=%s&cpOrderId=%s&cpUserInfo=%s&orderId=%s&orderStatus=%s&payFee=%s&payTime=%s&productCode=%s&productCount=%s&productName=%s&uid=%s'
    server_sign = server_sign % (app_id, cpOrderId, cpUserInfo, orderId, orderStatus, payFee, payTime, productCode, productCount, productName, uid)
    server_sign = server_sign.encode('utf-8')
    hashed = hmac.new(app_key, server_sign, hashlib.sha1)
    server_sign = binascii.b2a_hex(hashed.digest())
    
    print "curl 'appId=7932&cpOrderId=%s&cpUserInfo=%s&orderId=%s&orderStatus=%s&payFee=%s&payTime=%s&productCode=%s&productCount=%s&productName=%s&uid=%s&signature=%s' 'http://127.0.0.1/service/confirm/xiaomi' "%(cpOrderId,cpUserInfo,orderId,orderStatus,payFee,payTime,productCode,productCount,productName,uid,server_sign)    

def testJson():
    
    from urllib2 import quote,unquote, urlopen
    result = urlopen('http://bwzq.fytxonline.com:8080/static/server/o_4399.json',timeout=5).read()
    pay_server_id=2
    server_id=0
    if result != '':
        result = json.loads(result)
        for serverlist in result["serverList"]:
            if serverlist["other"]["sdk_sid"]==pay_server_id:
                server_id=serverlist["id"]
                break;
    print server_id
def multi_replace(text, adict):
    rx = re.compile('|'.join(map(re.escape, adict)))
    def xlat(match):
        return adict[match.group(0)]
    return rx.sub(xlat, text)
def _is_null_value(value):
    return False
def _build_doc(doc, boost=None, fieldUpdates=None):
    doc_elem = ET.Element('doc')

    for key, value in doc.items():
        if key == 'boost':
            doc_elem.set('boost', force_unicode(value))
            continue

        # To avoid multiple code-paths we'd like to treat all of our values as iterables:
        if isinstance(value, (list, tuple)):
            values = value
        else:
            values = (value, )

        for bit in values:
            if _is_null_value(bit):
                continue

            attrs = {'name': key}

            if fieldUpdates and key in fieldUpdates:
                attrs['update'] = fieldUpdates[key]

            if boost and key in boost:
                attrs['boost'] = force_unicode(boost[key])

            field = ET.Element('field', **attrs)
            field.text = _from_python(bit)

            doc_elem.append(field)

        return doc_elem
def testEt():
    commitWithin=True
    boost='1' 
    fieldUpdates=None
    docs=[
                {
                    "id": "doc_1",
                    "title": "A test document",
                },
                {
                    "id": "doc_2",
                    "title": "The Banana: Tasty or Dangerous?",
                },
            ]
    message = ET.Element('add')

    if commitWithin:
        message.set('commitWithin', commitWithin)

    for doc in docs:
        message.append(_build_doc(doc, boost=boost, fieldUpdates=fieldUpdates))

    # This returns a bytestring. Ugh.
    m = ET.tostring(message, encoding='utf-8')
    # Convert back to Unicode please.
    # m = force_unicode(m)
    print m
def testfor():
    a=[]
    b=[av for av in a if av]
    print 'b:',b
    for av in a:
        print 'av:',av

if __name__ == '__main__':
    # testBaidu()
#    testJson()
#    testGetRequest()
    # dic={u'公司':'',u'有限':'',u'科技':'',u'深圳':'',u'市':'',u'广州':'',u'上海':'',u'北京':'',u'杭州':'',u'成都':'',u'武汉':'',u'技术':'',u'股份':''}
    # print multi_replace(u'深圳十五月亮网络技术有限公司',dic).encode('utf8')
    testfor()