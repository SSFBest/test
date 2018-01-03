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
            conn.putheader("Content-Type", "%s"%data_type)
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
IS_PY3=False
def force_bytes(value):
    """
    Forces a Unicode string to become a bytestring.
    """
    if IS_PY3:
        if isinstance(value, str):
            value = value.encode('utf-8', 'backslashreplace')
    else:
        if isinstance(value, unicode):
            value = value.encode('utf-8')

    return value
def force_unicode(value):
    """
    Forces a bytestring to become a Unicode string.
    """
    if IS_PY3:
        # Python 3.X
        if isinstance(value, bytes):
            value = value.decode('utf-8', errors='replace')
        elif not isinstance(value, str):
            value = str(value)
    else:
        # Python 2.X
        if isinstance(value, str):
            value = value.decode('utf-8', 'replace')
        elif not isinstance(value, basestring):
            value = unicode(value)

    return value
REPLACEMENTS = (
    # Nuke nasty control characters.
    (b'\x00', b''), # Start of heading
    (b'\x01', b''), # Start of heading
    (b'\x02', b''), # Start of text
    (b'\x03', b''), # End of text
    (b'\x04', b''), # End of transmission
    (b'\x05', b''), # Enquiry
    (b'\x06', b''), # Acknowledge
    (b'\x07', b''), # Ring terminal bell
    (b'\x08', b''), # Backspace
    (b'\x0b', b''), # Vertical tab
    (b'\x0c', b''), # Form feed
    (b'\x0e', b''), # Shift out
    (b'\x0f', b''), # Shift in
    (b'\x10', b''), # Data link escape
    (b'\x11', b''), # Device control 1
    (b'\x12', b''), # Device control 2
    (b'\x13', b''), # Device control 3
    (b'\x14', b''), # Device control 4
    (b'\x15', b''), # Negative acknowledge
    (b'\x16', b''), # Synchronous idle
    (b'\x17', b''), # End of transmission block
    (b'\x18', b''), # Cancel
    (b'\x19', b''), # End of medium
    (b'\x1a', b''), # Substitute character
    (b'\x1b', b''), # Escape
    (b'\x1c', b''), # File separator
    (b'\x1d', b''), # Group separator
    (b'\x1e', b''), # Record separator
    (b'\x1f', b''), # Unit separator
)

def sanitize(data):
    fixed_string = force_bytes(data)

    for bad, good in REPLACEMENTS:
        fixed_string = fixed_string.replace(bad, good)

    return force_unicode(fixed_string)
def testGetRequest():
    url=u'http://localhost:8983/solr/article/update'
    data=u'''
    {
        "add":{
            "doc":{
                "aid":2,
                "cid": 1,
                "title": "360baidu",
                "keywords": "360"
            }
        }
        }
        
    '''
    jsondata=u'''
        {
                "aid":3,
                "cid": 1,
                "title": "360baidu",
                "keywords": "360"
            },
    '''
    xmldata=u'''
        <add>
            <doc>
            <field name="aid">1</field>
            <field name="cid">1</field>
            <field name="title">360baidu</field>
            <field name="keywords">360</field>
            </doc>
        </add>
    '''
    commitdata=u'''
    {
        "commit":{}
    }
    '''
    result=http_post(url,data=sanitize(commitdata),data_type='application/json')
    print result


if __name__ == '__main__':
    testGetRequest()
#    testJson()
#    testGetRequest()