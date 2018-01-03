#-*- coding: utf8 -*-
class baseclass(object):
    def __init__(self):
        print 'baseclass'
    def get(self):
        print "base get"
    def update(self):
        '''
        更新对象的部分属性
        '''
        #获取完整实例
        full_obj = self or self.__class__ 
        self.get()
        print full_obj
    @classmethod
    def query(cls, condition = None, offset = None, limit = None, order_by = None):
        print 'model query'
        if condition is None:
            condition = {}
        
             
    
    
class derivedClass(baseclass):
    def __init__(self,arg):
        super(derivedClass,self).__init__()
        print 'arg',arg
    def get(self):
        print "derived get"
    @classmethod
    def checkUser(cls, username):
        print 'checkuser'
        userdata = cls.query()
    
    print "jo"
    
def test(arg):
    print arg
if __name__ == '__main__':
#    test(1)
#    baseclass=derivedClass(1)
#    baseclass.get()
    #util.onTime()
    #util.ondate()
    #baseclass.update()
    derivedClass.query('dd')

    