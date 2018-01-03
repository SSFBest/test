#-*- coding: utf-8 -*-
'''
Created on 2010-9-16

@author: Administrator
'''
def testdic():
    dic={
'default' : {
    'start_time': '2009-07-09',
    'gift_str': unicode('Click to open the gift package for new player, it includes different types of baby animals and feeds, which helps you have a good beginning in Animal Paradise.', 'utf-8'),   #开启新手礼包，你可以获得各种动物宝宝、饲料，帮助你渡过新手阶段
    'data':{
        'ranch': {
            'babies': {
                'gaosu':[5, 1.00],
                'jisu': [2, 1.00],
                'kuaisu':[10,1.00]
               },
         },
    },
},

'cn' : {
    'start_time': '2009-07-09',
    'gift_str': unicode('开启新手礼包，你可以获得各种动物宝宝、饲料，帮助你渡过新手阶段', 'utf-8'),   #开启新手礼包，你可以获得各种动物宝宝、饲料，帮助你渡过新手阶段
    'data':{
        'ranch': {
            'babies': {
                'quail':[2, 1.00],
                'WhiteRabbit': [2, 1.00],
                'HuaPig': [1, 1.00],
               },
         },
    },
},

'french' : {
    'start_time': '2009-07-09',
    'gift_str': unicode('Click to open the gift package for new player, it includes different types of baby animals and feeds, which helps you have a good beginning in Animal Paradise.', 'utf-8'),   #开启新手礼包，你可以获得各种动物宝宝、饲料，帮助你渡过新手阶段
    'data':{
        'ranch': {
            'babies': {
                'quail':[2, 1.00],
                'WhiteRabbit': [2, 1.00],
                'HuaPig': [1, 1.00],
               },
         },

    },
},

'spain' : {
    'start_time': '2009-07-09',
    'gift_str': unicode('Click to open the gift package for new player, it includes different types of baby animals and feeds, which helps you have a good beginning in Animal Paradise.', 'utf-8'),   #开启新手礼包，你可以获得各种动物宝宝、饲料，帮助你渡过新手阶段
    'data':{
        'ranch': {
            'babies': {
                'quail':[2, 1.00],
                'WhiteRabbit': [2, 1.00],
                'HuaPig': [1, 1.00],
               },
         },
    },
},

'italia' : {
    'start_time': '2009-07-09',
    'gift_str': unicode('Clicchi aprire il pacco di regalo per giocatore nuovo, include tipi diversi di animali di bambino ed alimentazioni che Laiutano hanno un buon inizio in Paradiso Animale.', 'utf-8'),   #开启新手礼包，你可以获得各种动物宝宝、饲料，帮助你渡过新手阶段
    'data':{
        'ranch': {
            'babies': {
                'quail':[2, 1.00],
                'WhiteRabbit': [2, 1.00],
                'HuaPig': [1, 1.00],
               },
         },
    },
},

}
    print dic
if __name__ == '__main__':
    award={
           "farm":{"seeds":{"grapes":5,"putao":10}},
             "ranch":{"babies":{"dog":12,"pig":10}}
}
#    testCollect(award,"a_type")
#    testdicone()
#    testNullDic()
    testdic()
#    test_dic2()
