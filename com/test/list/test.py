#-*- coding: utf-8 -*-

def test_get():
    l=[1,2,3,4]
    for x in range(len(l)):
        print l[x]
        if l[x]==2:
            print x
            # del l[x]
        
    print l
def test2():
    l = [1,2,3,4]
    l = filter(lambda x:x !=4,l)
    print l
def test3():
    l = [1,2,3,4]
    l = [ i for i in l if i !=4] #同样产生一个新序列，复值给l
    print l
def test4(*args,**kwargs):
    print args
    print kwargs
    kwargs.update({'c':5})
    print kwargs
def not_scrapy(d):
        # 取最后10条
    ref_d=d[-50:]
    ref_d_pid=[ref_dd.get('pid') for ref_dd in ref_d]
    print 'ref_d_pid',ref_d_pid
    d_pid=[dd.get('pid') for dd in d[:-50]]
    print 'd_pid',d_pid
    last_d_pid=set(ref_d_pid)-set(d_pid)
    print 'last_d_pid',last_d_pid
    return filter(lambda x:x.get('pid') in last_d_pid,ref_d)
def remove_br(a):
   if a[-1:][0] in ['<br>','<br/>']:
       return remove_br(a[0:-1])
   else:
       return a
def remove_last(a):
    # print a[0]
    print '%s:%s'%(a[-2:],type(a[-2:]))
    # print a[-1:0]
    
    if a[-1:] in [u'女',u'男',u'春',u'夏',u'秋',u'冬']:
        return remove_last(a[0:-1])
    if a[-2:] in [u'女童',u'男童',u'春季',u'夏季',u'秋季',u'冬季',u'春夏',u'夏秋',u'秋冬',u'夏天']:
        return remove_last(a[0:-2])
    else:
        return a

if __name__ == '__main__':
    # print remove_br(['a','b','c','br','/br','<br>','<br/>'])
    print remove_last(u'运动装女童夏季')
    # test_get()
    # test3()
    # test4(1,2,a=3,b=4)
    d=[
    {'id':1,'pid':'1234'},{'id':2,'pid':'2234'},{'id':3,'pid':'3234'},{'id':4,'pid':'4234'},{'id':5,'pid':'5234'},
    {'id':11,'pid':'11234'},{'id':12,'pid':'12234'},{'id':13,'pid':'13234'},{'id':14,'pid':'14234'},{'id':15,'pid':'15234'},
    {'id':21,'pid':'21234'},{'id':22,'pid':'22234'},{'id':23,'pid':'23234'},{'id':24,'pid':'24234'},{'id':25,'pid':'25234'},
    {'id':31,'pid':'31234'},{'id':32,'pid':'32234'},{'id':33,'pid':'33234'},{'id':34,'pid':'34234'},{'id':35,'pid':'1234'},
    ]
    print not_scrapy(d)