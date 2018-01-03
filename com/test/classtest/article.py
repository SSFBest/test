#-*- coding: utf8 -*-


class Article(object):

    def __init__(self):
        self.tag_1=1
        self.tag_2=0
        self.tag_3=0
        self.tag_4=0
        self.tag_5=0
        self.tag_6=0
        self.tag_7=0
        self.tag_8=0
        
    def get_tagname(self):
        # n=[1 if self.tag_%d%num == 1 for num in range(1,9)]
        n=[1 if eval('self.tag_%d == 1 '%num) else 0 for num in range(1,9)]
        n=[1 for num in range(1,9) if eval('self.tag_%d == 1 '%num) ]
        # n=[num for num in range(1,9)]
        print n
        # print self.tag_1
class A:   
    def __init__(self):   
        self.name = 'zhangjing'  
        self.age='24'
    # def method(self):   
    #     print"method print"  
    def method1(self):   
        print"method print1"
  
a = A()

address=getattr(a,'address',{})
setattr(a,'address',address)
p=address.get('p',[])
address.update({'p':p.append(5)})
print address
print address,a.address
address.update({'p':p})
setattr(a,'address',address)
print address,a.address


print getattr(a , 'name', 'not find' ) #果Instance 对象中有属性name则打印self.name的值，否则打印
print getattr(a , 'age', 'not find')   #如果Instance 对象中有属性age则打印self.age的值，否则打印'not find'
print getattr(a, 'method', 'default')   
#如果有方法method，否则打印其地址，否则打印default   
# print getattr(a, 'method', method1)()   
#如果有方法method，运行函数并打印None否则打印default


# if __name__ == '__main__':
#     article=Article()
#     article.get_tagname()