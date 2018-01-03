#-*- coding: utf-8 -*-
import sys
'''
Created on 2010-9-9

@author: Administrator
'''
def command_test(argv=None):
    argv=sys.argv[1:]
    print argv
def check():
    data={
    "tips":{
         "a_type":"ￄ￣﾿￉ￒￔￍﾨﾹ�ﾵￇￂﾽﾻ￱ﾵￃﾸￃￎ￯ￆﾷ",
         "b_type":"ￄ￣﾿￉ￒￔﾴￓ￉ￌﾵ￪ￖ￐ﾹﾺￂ￲ﾵﾽﾸￃￎ￯ￆﾷ",
         "c_type":"ￄ￣﾿￉ￒￔﾴￓ￉ￌﾵ￪ￖ￐ﾹﾺￂ￲ﾵﾽﾸￃￎ￯ￆﾷ",
         "d_type":"ﾺￃￓ￑ￔ￹ￋￍﾵￄ￀￱ￎ￯ￖ￐ﾰﾵﾲ￘ﾾﾪￏﾲ",
         "e_type":"￈ﾥﾺￃￓ￑ﾼￒￗﾪￗﾪﾻ￲￐￭ﾻ￡ￓ￐ￊￕﾻ￱",
    },
   "activity":{
         "zhongqiu":{
            "need":{
                         "a_type":{
                                'farm' : {
                                       'seeds' : {'grapes':"10|5"},
                                 }, 
                          },
                         "b_type":{
                                'ranch':  {'babies' : {'wuguChook':"10|6"}},
                         },
                         "c_type":{
                                 'ranch':  {'babies' : {'wuguChook':"10|5"}},
                         },
                         "d_type":{
                                  'ranch':  {'babies' : {'wuguChook':"10|5"}},
                         },
                         "e_type":{
                                  'ranch':  {'babies' : {'wuguChook':"10|5"}},
                         },
               },
              "exchange":{
                         "gold":1000,
                         "K_coin":50,
                         'farm' : {
                      'seeds' : {'xigua':1},
                  'properties': {
                      'fertilizer': {
                     'common': 1,
                     'gaosu': 1,
                     'jisu': 3,
                                   },
                                }
                  }, 
                         'ranch':  {'babies' : {'xigua':1}},
              }
       },
         "guoqin":{
            "need":{
                   "a_type":{
                           'farm' : {
                                   'seeds' : {'grapes':"10|5"},
                            }, 
                     },
                    "b_type":{
                            'ranch':  {'babies' : {'wuguChook':"10|6"}},
                     },
                     "c_type":{
                             'ranch':  {'babies' : {'wuguChook':"10|5"}},
                     },
                     "d_type":{
                             'ranch':  {'babies' : {'wuguChook':"10|5"}},
                      },
                      "e_type":{
                             'ranch':  {'babies' : {'wuguChook':"10|5"}},
                      },
                   },
                   "exchange":{
                            "gold":1000,
                            "K_coin":50,
                            'farm' : {
                    'seeds' : {'xigua':1},
                    'properties': {
                        'fertilizer': {
                             'common': 1,
                             'gaosu': 1,
                                 'jisu': 3,
                                             },
                                     }
                }, 
                            'ranch':  {'babies' : {'xigua':1}},

                 }
        },
     },
}

    print data
def test1(a=2,b=3):
  print b,a
if __name__ == '__main__':
#    command_test()
    # argv=sys.argv[1:]
    # if argv[0]=='1':
    #     print '1'
    test1(b=5,a=6)
#    check()