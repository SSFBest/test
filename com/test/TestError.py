'''
Created on 2010-7-5

@author: Administrator
'''
import sys
x=2
def a():
    x=x+2
    print x
def b():
    print x
    x=3
    print x
def Assignment():
    a = b = 3
    a = 4
    print a, b # 4, 3
def test_raise():
    age = 150
    if(age > 100 or age < 0):
        raise Model_Error(2,u'555555')
    print "helll"
    return age
def test_try():
    try:
        raise Model_Error(2,u'222')
    except Model_Error,e:
        print sys.exc_info()[:2]
        code=e.msg
    return code


class Model_Error(Exception):
    """Exception class for Model"""

    def __init__(self, code, msg, data=None, args=None):
        if not isinstance(msg, unicode):
            msg = msg.decode('utf-8')
        self.code = code
        self.msg = msg
        self.data = data
        self.args = (args or [])

    def __str__(self):
        return (u'Error %s: %s' % (self.code, self.msg)).encode('utf-8')

    
if __name__ == '__main__':
    # test_raise()
   print test_try()