#-*- coding: utf8 -*-
import   traceback
def private(func):
    def   access_check(*args):
        sf   =     traceback.extract_stack()
        if   len(sf)   <   2   or   sf[-2][2]   !=   'getMyClass'   or   sf[-2][0]   !=   sf[-1][0]:
            raise   "Access   Denied "
        else:
            return   func(*args)
    return   access_check

class   MyClass:
    @classmethod
    def   getMyClass(cls):
        return   cls()

    @private
    def   __init__(self):
        self.val   =   9
    def test(self):
        print self.val
    
if   __name__   ==   '__main__':
    #a   =   MyClass()
    a   =   MyClass.getMyClass()
    a.test()
    print   a.val
