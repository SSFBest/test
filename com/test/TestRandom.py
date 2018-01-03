#-*- coding: utf8 -*-
import random

'''
Created on 2010-7-16

@author: Administrator
'''
def test_sample():
    print random.sample(xrange(10000000), 60)
    point_bonus={'bonus':{  #积分奖励 gold-金币，goods-物品
                 1000:[
                          {
                             'bonus_type':'goods',     #物品
                             'category':'common_fish', #物品分类
                             'goods_type':'',          #子分类，有的话填
                             'name':['jinlongyu'],     #键值
                             'num':1,                  #数量
                          },
                          {
                             'bonus_type':'goods',     #物品
                             'category':'common_fish2', #物品分类
                             'goods_type':'',          #子分类，有的话填
                             'name':['jinlongyu2'],     #键值
                             'num':1,                  #数量
                          },
                      ],
                      }
    }
    bonus_count=1
    
    rand_bonus = random.sample(point_bonus["bonus"][1000],bonus_count)
    print rand_bonus
#coding=utf-8  
import random

def langren():
    pai = ['狼','狼','村','村','预','丘','猎','巫']
    l = len(pai)
    c = 1
    for i in range(0,l):
        count = random.randrange(len(pai))
        print c,'.......',pai[count]
        pai.remove(pai[count])
        c +=1
def test_randomGen():
    uid='66973233'
    print str(int(random.random()*10**14))
    mycard_tg = 'rekoo'+uid+str(int(random.random()*10**(20-len(uid))))
    print mycard_tg

if __name__ == '__main__':
    test_sample()
#    langren()
#    test_randomGen()