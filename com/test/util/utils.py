#-*- coding: utf-8 -*-
import random
import operator
import traceback, sys, cStringIO, os
import datetime, time
from cgi import parse_qsl
import cPickle as pickle
import socket
from math import ceil

#from rkcache import RKCache

def random_occur(probability = 0.5):
    r = random.random()
    if r<probability:
        return True
    else:
        return False

def random_choice(config):
    #config = [(0.1, 20), (0.2, 30), (0.7, 40)]
    #thesum = reduce(operator.add, [item[0] for item in config], 0)
    #if thesum>1:
    #    raise Exception, 'config error'
    
    r = random.random()
    kk = 0
    for item in config:
        kk += item[0]
        if r<kk:
            return item[1]

def random_range(start, end):
    r = random.random()
    return r*(end-start)+start

def random_range_multi(start, end, num, interval):
    #0, 24, 4, 1 从0-24中选择4个数且间隔不能小于1
    res = []
    section_range = (end-start)/(num+0.0)

    select_num = None
    for i in range(num):
        if select_num is None:
            select_start = start
        else:
            select_start = select_num + interval

        select_end = start + section_range*(i+1)

        select_num = random_range(select_start, select_end)
        res.append(select_num)
    
    return res

#增加字典某个字段的值
def add2dict(d, k, v):
    if d.has_key(k):
        d[k] += v
    else:
        d[k] = v

#将两个字典的value合并成一个列表
def merge_dict(d1, d2):
    
    d3 = {}
    for k in d1:
        d2_value = d2[k] if d2.has_key(k) else 0
        d3[k] = [d1[k], d2_value]
    
    return d3

#将两个字典的key value 合并成一个字典
def merge_dict2(d1, d2):
    d3 = d1.copy()
    for k in d2:
        if d3.has_key(k):
            d3[k] += d2[k]
        else:
            d3[k] = d2[k]
    return d3

def get_err():
    f = cStringIO.StringIO( )
    traceback.print_exc(file=f)
    return f.getvalue( )

def print_err():
    sys.stderr.write('=='*30+os.linesep)
    sys.stderr.write('err time: '+str(datetime.datetime.now())+os.linesep)
    sys.stderr.write('--'*30+os.linesep)
    traceback.print_exc(file=sys.stderr)
    sys.stderr.write('=='*30+os.linesep)

def get_date_str(dt = None):
    if dt is None:
        dt = datetime.datetime.now()
    
    return dt.strftime('%Y-%m-%d')

def get_time_str(dt = None):
    if dt is None:
        dt = datetime.datetime.now()
    
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def parse_time_str(date_str):
    t = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    return datetime.datetime(*t[0:6])


def format_time(target_time):
  now = datetime.datetime.now()
  tdelta = now - target_time

  if tdelta.days < 0:
    ret_time = u"就在刚才"
  else:
    if tdelta.days > 0:
      ret_time = u"%d天前" % tdelta.days
    elif (tdelta.seconds / (60*60)) > 0:
      ret_time = u"%d小时前" % (tdelta.seconds / (60*60))
    elif (tdelta.seconds / (60)) > 0:
      ret_time = u"%d分钟前" % (tdelta.seconds / 60)
    else:
      ret_time = u"就在刚才"

  return ret_time
  
def send_udp(server, data, is_dumped=True):
    udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if is_dumped:
        data = pickle.dumps(data)
    udp_client.sendto(data, server)
def page_list2dic(l,per_page):
    hits=len(l)
    num_pages = int(ceil(hits / float(per_page)))
    d={}
    for number in range(1,num_pages+1):
        bottom = (number-1) * per_page
        top = bottom + per_page
        d.update({number:l[bottom:top]})
    return d
def test(*a):
    print type(a)
    print a
def test2(**aa):
    print aa
def test_for():
    for s in ['a','b','c'] + ['1','2']:
        print s

# print page_list2dic([1,2,3,4,5,6,7,8],6)
# test(*[1,2])
# test(1)
test_for()
#def _parse_backend_uri(backend_uri):
#    """
#    Converts the "backend_uri" into a cache scheme ('db', 'memcached', etc), a
#    host and any extra params that are required for the backend. Returns a
#    (scheme, host, params) tuple.
#    """
#    if backend_uri.find(':') == -1:
#        raise Error, "Backend URI must start with scheme://"
#    scheme, rest = backend_uri.split(':', 1)
#    if not rest.startswith('//'):
#        raise Error, "Backend URI must start with scheme://"
#
#    host = rest[2:]
#    qpos = rest.find('?')
#    if qpos != -1:
#        params = dict(parse_qsl(rest[qpos+1:]))
#        host = rest[2:qpos]
#    else:
#        params = {}
#    if host.endswith('/'):
#        host = host[:-1]
#
#    return scheme, host, params
#
#from django.conf import settings    
#def _get_cache():
#    scheme, host, params = _parse_backend_uri(settings.APP_CACHE_BACKEND)
#    return RKCache(host)
#    
#cache = _get_cache()
#
#from django.core import signals
#signals.request_finished.connect(cache.close)