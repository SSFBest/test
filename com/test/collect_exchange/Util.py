#-*- coding: utf-8 -*-
'''
Created on 2010-9-16

@author: Administrator
'''
def testdic():
    dic={
         "farm":{"seeds":"xigua"}
         }
    if dic.has_key("farm"):
        print "ok"
def testdicone():
    atuple=({"a":1,"b":2},{"c":3,"d":4})
    print [b.keys() for b in [a for a in atuple]]
    print [a for a in ({"a":1,"b":2},{"c":3,"d":4})]
    print [atuple[b].keys() for b in [a for a in range(len(atuple))]]
    print sum( [item.keys() for item in ({"a":1,"b":2},{"c":3,"d":4})], [] )
def testNullDic():
    dic={}
    if dic==None:
        print "null"
    if dic=={}:
        print "{}"
    if dic.has_key("abc"):
        print "haskey"
def testCollect(award,type):
    collect_exchange={
   "event":{
         "land.friend.water":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}), 
         ],
         "land.friend.put_pest":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
         ],
         "fold.friend.cure":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
         ],
         "fold.friend.scare":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
         ],
         "land.friend.kill_pest":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
         ],
   },
   "tips":{
         "a_type":"你可以通过登陆获得该物品",
         "b_type":"你可以从商店中购买到该物品",
         "c_type":"你可以从商店中购买到该物品",
         "d_type":"好友赠送的礼物中暗藏惊喜",
         "e_type":"去好友家转转或许会有收获",
   },
   "activity":{
         "zhongqiu":{
               "need":{
                     "a_type":{
                            'farm' : {
                                   'seeds' : {'grapes':1},
                                   'properties': {
                                        'fertilizer': {
                                              'common': 1,
                                              'gaosu': 1,
                                              'jisu': 3,
                                        },
                                   }
                             }, 
                            'ranch':  {'babies' : {'dog':16}},
                      },
                     "b_type":{"a":"b"},
                     "c_type":{},
                     "d_type":{},
                     "e_type":{},
               },
               "exchange":{
                        'common': {
                                   'gift_bags': {'hflibao_1':1},
                                   'mystic_bags':{'mb_10' : 1},
                         },
                        "gold":1000,
                        'farm' : {'seeds' : {'xigua':1}}, 
                        'ranch':  {
                            'babies' : {'xigua':1},
                            'properties': {
                                  'fertilizer': {
                                       'common': 1,
                                       'gaosu': 1,
                                       'jisu': 3,
                                   },
                             }
                        }
                         
               },
               "used":True,
         },
         "guoqin":{
               "need":{
                     "a_type":{"a":"b"},
                     "b_type":{"a":"b"},
                     "c_type":{},
                     "d_type":{},
                     "e_type":{},
               },
               "used":True,
        },
   },
   "used":True
}
    collect={
  "zhongqiu": {
   "a_type": {
    "farm": {
     "seeds": {
      "grapes": 20
     }
    }
   }
  }
 }

    collect1={}
#    collect={}
    for activity in collect_exchange["activity"]:
        for s_type in collect_exchange["activity"][activity]["need"]:
            if s_type==type:
                print collect_exchange["activity"][activity]["need"][type]
                need_dic=collect_exchange["activity"][activity]["need"][type]
                if(award.has_key("farm")):
                    if(award["farm"].has_key("seeds")):
                        for seed in award["farm"]['seeds']:
                            if need_dic.has_key("farm") and need_dic["farm"] and need_dic["farm"]["seeds"] and need_dic["farm"]["seeds"].has_key(seed):
                                print seed
                                addnum=award["farm"]['seeds'][seed]
                                neednum=need_dic["farm"]["seeds"][seed]
                                if(collect.has_key(activity)):
                                    if  collect[activity].has_key(type) and collect[activity][type] and collect[activity][type].has_key("farm") and collect[activity][type]["farm"] and collect[activity][type]["farm"]["seeds"].has_key(seed):
                                        collect[activity][type]["farm"]["seeds"][seed]+=addnum
#                                        collect[activity][type]["farm"]["seeds"][seed]["need"]=neednum
                                    else:
                                        collect[activity][type].update({"farm":{"seeds":{seed:addnum}}})
                                else:
#                                    award["farm"]["seeds"].update({seed:{"has":addnum,"need":neednum}})
                                    collect.update({activity:{type:{"farm":{"seeds":{seed:addnum}}}}})
                                print collect
                if(award.has_key("ranch")):
                        if(award["ranch"].has_key("babies")):
                            for seed in award["ranch"]['babies']:
                                if need_dic.has_key("ranch") and need_dic["ranch"] and need_dic["ranch"]["babies"] and need_dic["ranch"]["babies"].has_key(seed):
                                    print seed
                                    addnum=award["ranch"]['babies'][seed]
                                    neednum=need_dic["ranch"]["babies"][seed]
                                    if(collect.has_key(activity)):
                                        if  collect[activity].has_key(type) and collect[activity][type] and collect[activity][type].has_key("ranch") and collect[activity][type]["ranch"] and collect[activity][type]["ranch"]["babies"].has_key(seed):
                                            collect[activity][type]["ranch"]["babies"][seed]+=addnum
                                        else:
                                            collect[activity][type].update({"ranch":{"babies":{seed:addnum}}})
                                    else:
                                        collect.update({activity:{type:{"ranch":{"babies":{seed:addnum}}}}})
                                    print collect
    print "collect",collect 

def test_dic():
    dic={
   "tips":{
         "a_type":"你可以通过登陆获得该物品",
         "b_type":"你可以从商店中购买到该物品",
         "c_type":"你可以从商店中购买到该物品",
         "d_type":"好友赠送的礼物中暗藏惊喜",
         "e_type":"去好友家转转或许会有收获",
   },
   "activity":{
         "zhongqiu":{
               "need":{
                     "a_type":{
                            'farm' : {
                                   'seeds' : {'grapes':1},
                                   'properties': {
                                        'fertilizer': {
                                              'common': 1,
                                              'gaosu': 1,
                                              'jisu': 3,
                                        },
                                   }
                             }, 
                            'ranch':  {'babies' : {'wuguChook':1}},
                      },
               },
               "exchange":{
                        "gold":1000,
                        'farm' : {'seeds' : {'xigua':1}}, 
                        'ranch':  {
                            'babies' : {'xigua':1},
                            'properties': {
                                  'fertilizer': {
                                       'common': 1,
                                       'gaosu': 1,
                                       'jisu': 3,
                                   },
                             }
                        }
                         
               },
               "used":True,
         },
         "guoqin":{
               "need":{
                     "a_type":{"a":"b"},
                     "b_type":{"a":"b"},
                     "c_type":{},
                     "d_type":{},
                     "e_type":{},
               },
               "used":True,
        },
   },
   "used":True
}
    dic2={
    "zhongqiu":{
         "a_type":{
         "farm":{
               "seeds":{
                     "grapes":20,
                             "xigua":30
                    }
          }
          },
       "b_type":{
         "farm":{
               "seeds":{
                     "grapes":20,
                             "xigua":19
                    }
          }
          }
     },
     "zhongqiu":{
         "a_type":{
         "farm":{
               "seeds":{
                     "grapes":12,
                             "xigua":30
                    }
          }
          },
     },

  }
    dic3=""
    print dic
    print dic2
    print dic3
def test_dic2():
    collect_exchange={
   "event":{
         "land.friend.water":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}), 
         ],
         "land.friend.put_pest":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
         ],
         "fold.friend.cure":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
         ],
         "fold.friend.scare":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
         ],
         "land.friend.kill_pest":[
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
                  (0.05, {'farm' : {'seeds' : {'xigua':1}}}),
         ],
   },
   "tips":{
         "a_type":"你可以通过登陆获得该物品",
         "b_type":"你可以从商店中购买到该物品",
         "c_type":"你可以从商店中购买到该物品",
         "d_type":"好友赠送的礼物中暗藏惊喜",
         "e_type":"去好友家转转或许会有收获",
   },
   "activity":{
         "zhongqiu":{
               "need":{
                     "a_type":{
                            'farm' : {
                                   'seeds' : {'grapes':1},
                                   'properties': {
                                        'fertilizer': {
                                              'common': 1,
                                              'gaosu': 1,
                                              'jisu': 3,
                                        },
                                   }
                             }, 
                            'ranch':  {'babies' : {'wuguChook':1}},
                      },
                     "b_type":{"a":"b"},
                     "c_type":{},
                     "d_type":{},
                     "e_type":{},
               },
               "exchange":{
                        'common': {
                                   'gift_bags': {'hflibao_1':1},
                                   'mystic_bags':{'mb_10' : 1},
                         },
                        "gold":1000,
                        'farm' : {'seeds' : {'xigua':1}}, 
                        'ranch':  {
                            'babies' : {'xigua':1},
                            'properties': {
                                  'fertilizer': {
                                       'common': 1,
                                       'gaosu': 1,
                                       'jisu': 3,
                                   },
                             }
                        }
                         
               },
               "used":True,
         },
         "guoqin":{
               "need":{
                     "a_type":{"a":"b"},
                     "b_type":{"a":"b"},
                     "c_type":{},
                     "d_type":{},
                     "e_type":{},
               },
               "used":True,
        },
   },
   "used":True
}
    del collect_exchange["event"]
    print collect_exchange
if __name__ == '__main__':
    award={
           "farm":{"seeds":{"grapes":5,"putao":10}},
             "ranch":{"babies":{"dog":12,"pig":10}}
}
#    testCollect(award,"a_type")
#    testdicone()
#    testNullDic()
    test_dic()
#    test_dic2()
