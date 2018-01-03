#-*- coding: utf-8 -*-
'''
Created on 2010-9-16

@author: Administrator
'''

activitys={
          "tips":{
             "a_type":unicode("你可以通过登陆获得该物品","utf-8"),#你可以通过登陆获得该物品
             "b_type":unicode("你可以从商店中购买到该物品","utf-8"),#你可以从商店中购买到该物品
             "c_type":unicode("你可以从商店中购买到该物品","utf-8"),#你可以从商店中购买到该物品
             "d_type":unicode("好友赠送的礼物中暗藏惊喜","utf-8"),#好友赠送的礼物中暗藏惊喜
             "e_type":unicode("去好友家转转或许会有收获","utf-8")#去好友家转转或许会有收获
          },
         "activity":{
             "zhongqiu":{
                  "need":{
                     "farm":{"xigua":{"tips":"a_type","num":30},"graps":{"tips":"b_type","num":30}},
                     "ranch":{"sheep":{"tips":"d_type","num":40},"dog":{"tips":"c_type","num":4}},
                   },
                  "exchange":{
                        "gold":1000,
                        "F_coin":50,
                        'farm' : {'seeds' : {'xigua':1}}, 
                        'ranch':  {
                            'babies' : {'xigua':1},
                            'properties': {
                                  'fertilizer': {
                                       'common': 1,
                                       'gaosu': 1,
                                       'jisu': 3,
                                   },
                             },
                        } ,   
               },
               "used":True,
           },
           "guoqing":{
               "need":{
                     "farm":{"xigua":{"tips":"a_type","num":30},"graps":{"tips":"b_type","num":30}},
                     "ranch":{"sheep":{"tips":"d_type","num":40},"dog":{"tips":"c_type","num":4}},
                   },
                  "exchange":{
                        "gold":1000,
                        "F_coin":50,
                        'farm' : {'seeds' : {'xigua':1}}, 
                        'ranch':  {
                            'babies' : {'xigua':1},
                            'properties': {
                                  'fertilizer': {
                                       'common': 1,
                                       'gaosu': 1,
                                       'jisu': 3,
                                   },
                             },
                        } ,   
               },
               "used":True,
        },
    },
     "used":True,
   }
def testexchange():
    atype_tips=None
    btype_tips=None
    tips={}
    activitys={
          "tips":{
             "a_type":unicode("你可以通过登陆获得该物品","utf-8"),#你可以通过登陆获得该物品
             "b_type":unicode("你可以从商店中购买到该物品","utf-8"),#你可以从商店中购买到该物品
             "c_type":unicode("你可以从商店中购买到该物品","utf-8"),#你可以从商店中购买到该物品
             "d_type":unicode("好友赠送的礼物中暗藏惊喜","utf-8"),#好友赠送的礼物中暗藏惊喜
             "e_type":unicode("去好友家转转或许会有收获","utf-8")#去好友家转转或许会有收获
          },
         "activity":{
             "zhongqiu":{
                  "need":{
                     "farm":{"xigua":{"tips":"a_type","num":30},"graps":{"tips":"b_type","num":30}},
                     "ranch":{"sheep":{"tips":"d_type","num":40},"dog":{"tips":"c_type","num":4}},
                   },
                  "exchange":{
                        "gold":1000,
                        "F_coin":50,
                        'farm' : {'seeds' : {'xigua':1}}, 
                        'ranch':  {
                            'babies' : {'xigua':1},
                            'properties': {
                                  'fertilizer': {
                                       'common': 1,
                                       'gaosu': 1,
                                       'jisu': 3,
                                   },
                             },
                        } ,   
               },
               "used":True,
           },
           "guoqing":{
               "need":{
                     "farm":{"xigua":{"tips":"a_type","num":30},"graps":{"tips":"b_type","num":30}},
                     "ranch":{"sheep":{"tips":"d_type","num":40},"dog":{"tips":"c_type","num":4}},
                   },
                  "exchange":{
                        "gold":1000,
                        "F_coin":50,
                        'farm' : {'seeds' : {'xigua':1}}, 
                        'ranch':  {
                            'babies' : {'xigua':1},
                            'properties': {
                                  'fertilizer': {
                                       'common': 1,
                                       'gaosu': 1,
                                       'jisu': 3,
                                   },
                             },
                        } ,   
               },
               "used":True,
        },
    },
     "used":True,
   }
    tips=activitys["tips"]
    for activity in activitys["activity"]:
        need_dic=activitys["activity"][activity]["need"]
        print need_dic
        if(need_dic.has_key("farm")):
            for crops_type in need_dic["farm"]:
                tips_type=need_dic["farm"][crops_type]["tips"]
                need_dic["farm"][crops_type]["tips"]=tips[tips_type]
        if(need_dic.has_key("ranch")):
            for babies_type in need_dic["ranch"]:
                tips_type=need_dic["ranch"][babies_type]["tips"]
                need_dic["ranch"][babies_type]["tips"]=tips[tips_type]
    if(activitys.has_key("tips")):
        del activitys["tips"]
    print activitys
def testactivity():
    data={}
    activitys={
             "zhongqiu":{
                  "need":{
                     "farm":{"xigua":{"tips":"a_type","num":30},"graps":{"tips":"b_type","num":80}},
                     "ranch":{"sheep":{"tips":"d_type","num":80},"dog":{"tips":"c_type","num":4}},
                   },
                  
               "used":True,
              },
           "guoqing":{
               "need":{
                     "farm":{"xigua":{"tips":"a_type","num":10},"graps":{"tips":"b_type","num":530}},
                     "ranch":{"sheep":{"tips":"d_type","num":90},"dog":{"tips":"c_type","num":89}},
                   },
               "used":True,
           }
        }
    for activity in activitys:
        if (activitys[activity]["used"]):
            need_dic=activitys[activity]["need"]
            if(need_dic.has_key("farm")):
                for crops_type in need_dic["farm"]:
                    if(data.has_key(activity)and data[activity].has_key("farm")):
                        data[activity]["farm"].update({crops_type:need_dic["farm"][crops_type]["num"]})
                    elif(data.has_key(activity)):
                        data[activity].update({"farm":{crops_type:need_dic["farm"][crops_type]["num"]}})
                    else:
                        data.update({activity:{"farm":{crops_type:need_dic["farm"][crops_type]["num"]}}})
                        
            if(need_dic.has_key("ranch")):
                for babies_type in need_dic["ranch"]:
                    print babies_type
                    if(data.has_key(activity) and data[activity].has_key("ranch")):
                        data[activity]["ranch"].update({babies_type:need_dic["ranch"][babies_type]["num"]})
                    elif(data.has_key(activity)):
                         data[activity].update({"ranch":{babies_type:need_dic["ranch"][babies_type]["num"]}})
                    else:
                        data.update({activity:{"ranch":{babies_type:need_dic["ranch"][babies_type]["num"]}}})
    print data
def test_dic():
    data={'guoqing': {'farm': {'graps': 530, 'xigua': 10}, 'ranch': {'sheep': 90, 'dog': 89}}, 'zhongqiu': {'farm': {'graps': 80, 'xigua': 30}, 'ranch': {'sheep': 80, 'dog': 4}}}
    farm_harvest={"graps":100}
    ranch_harvest={"sheep":1000}
    for activity in data:
        if data[activity].has_key("farm"):
            for crops_type in data[activity]["farm"]:
                if farm_harvest and farm_harvest.has_key(crops_type):
                    data[activity]["farm"][crops_type]=farm_harvest[crops_type]
                else:
                    data[activity]["farm"][crops_type]=0
        if data[activity].has_key("ranch"):
            for babies_type in data[activity]["ranch"]:
                if ranch_harvest and ranch_harvest.has_key(babies_type):
                    data[activity]["ranch"][babies_type]=ranch_harvest[babies_type]
                else:
                    data[activity]["ranch"][babies_type]=0
    print data
def test_dic2():
    exchange_dic={}
    type="zhongqiu"
#    data={'guoqing': {'farm': {'graps': 50, 'xigua': 10}, 'ranch': {'sheep': 90, 'dog': 89}}, 'zhongqiu': {'farm': {'graps': 80, 'xigua': 30}, 'ranch': {'sheep': 80, 'dog': 4}}}
    farm_harvest={"graps":1000,"xigua":1000}
    ranch_harvest={"sheep":1000,"dog":1000}
    for activity in activitys["activity"]:
            if(activity==type):
                need_dic=activitys["activity"][activity]["need"]
                for scene_type in need_dic:
                    if scene_type=="farm":
                        for crops_type in need_dic[scene_type]:
                            neednum=need_dic[scene_type][crops_type]["num"]
                            if farm_harvest.has_key(crops_type):
                                if(farm_harvest[crops_type]<neednum):
#                                    raise model.Model_Error(500, u'你还没有收集完成')
                                    print "except"
                                if(exchange_dic.has_key("farm")):
                                    exchange_dic["farm"].update({crops_type:neednum})
                                else:
                                    exchange_dic.update({"farm":{crops_type:neednum}})
                    if scene_type=="ranch":
                        for babies_type in need_dic[scene_type]:
                            neednum=need_dic[scene_type][babies_type]["num"]
                            if ranch_harvest.has_key(babies_type):
                                if(ranch_harvest[babies_type]<neednum):
                                    print "except"
#                                    raise model.Model_Error(500, u'你还没有收集完成')
                                if(exchange_dic.has_key("ranch")):
                                    exchange_dic["ranch"].update({babies_type:neednum})
                                else:
                                    exchange_dic.update({"ranch":{babies_type:neednum}})
                                    
    print exchange_dic
def test_dic3():
    dic={
                        "gold":1000,
                        "F_coin":50,
                        'farm' : {'seeds' : {'xigua':1}}, 
                        'ranch':  {
                            'babies' : {'xigua':1},
                            'properties': {
                                  'fertilizer': {
                                       'common': 1,
                                       'gaosu': 1,
                                       'jisu': 3,
                                   },
                             },
                        } ,   
               }
    for d in dic:
        print d
def test_unicode():
    s="我爱中华"
    print unicode(s, "utf-8")
def process_dic():
    exchange_dic1={              #兑换奖励
                       'gold':50,
                       'F_coin':90,
                        'farm' : {
                                'seeds' : {
                                       'yutuhua':{"num":1,"tips":"玉免花"}
                                }, 
                            'properties': {
                                  'fertilizer': {
                                       'jisu': {"num":1,"tips":"急速化肥"},
                                   },
                             },
                            'decorations' : {
                                 'floor' : {
                                       'zhongqiujie':{"num":1,"tips":"中秋节地板"}
                                }, 
                                 'sky' : {
                                       'zhongqiujie':{"num":1,"tips":"中秋节天空"}
                                }, 
                                 'house' : {
                                       'zhongqiujie':{"num":1,"tips":"中秋节房子"}
                                }, 
                               'butterfly' : {
                                       'youming':{"num":1,"tips":"蝴蝶装饰"}
                                }, 
                            }, 
                         }, 
                        'ranch':  {
                                'babies' : {
                                       'liumangtu':{"num":1,"tips":"牛氓兔宝宝"}
                            },
                            'properties': {
                                  'feedstuffs': {
                                       'common': {"num":1,"tips":"普通饲料"},
                                   },
                             },
                        } ,  
                        'common' : { 
                            'gift_bags' : { 
                                       'zhongqiujielibao': {"num":1,"tips":"中秋节大礼包"},
                             },
                            'mystic_bags' : { 
                                       'mb_11': {"num":1,"tips":"宝箱"},
                                   },
                            },
                       }
    exchange_dic={'farm' : {
                                
                                'properties': {
                                  'fertilizer': {
                                       'jisu': {"num":1,"tips":"急速化肥"},
                                   },
                             },
                            'decorations' : {
                                 'floor' : {
                                       'zhongqiujie':{"num":1,"tips":"中秋节地板"}
                                }, 
                                 'sky' : {
                                       'zhongqiujie':{"num":1,"tips":"中秋节天空"}
                                }, 
                                 'house' : {
                                       'zhongqiujie':{"num":1,"tips":"中秋节房子"}
                                }, 
                               'butterfly' : {
                                       'youming':{"num":1,"tips":"蝴蝶装饰"}
                                }, 
                            }, 
                                }
                  
                  }
    for exchange_type in exchange_dic:
        if(exchange_type=="farm"):
            for type in exchange_dic[exchange_type]:
                if(type=="seeds"):
                    for crops in exchange_dic[exchange_type][type]:
                        exchange_dic[exchange_type][type][crops]=exchange_dic[exchange_type][type][crops]["num"]
                if(type=="properties" or type=="decorations"):
                    for subtype in exchange_dic[exchange_type][type]:
                        for sub_subtype in exchange_dic[exchange_type][type][subtype]:
                            print sub_subtype
                            exchange_dic[exchange_type][type][subtype][sub_subtype]=exchange_dic[exchange_type][type][subtype][sub_subtype]["num"]
        
        if(exchange_type=="ranch"):
            for type in exchange_dic[exchange_type]:
                if(type=="babies"):
                    for crops in exchange_dic[exchange_type][type]:
                        exchange_dic[exchange_type][type][crops]=exchange_dic[exchange_type][type][crops]["num"]
                if(type=="properties" or type=="decorations"):
                    for subtype in exchange_dic[exchange_type][type]:
                        for sub_subtype in exchange_dic[exchange_type][type][subtype]:
                            print sub_subtype
                            exchange_dic[exchange_type][type][subtype][sub_subtype]=exchange_dic[exchange_type][type][subtype][sub_subtype]["num"]
        if(exchange_type=="common"):
            for type in exchange_dic[exchange_type]:
                    for bags in exchange_dic[exchange_type][type]:
                        exchange_dic[exchange_type][type][bags]=exchange_dic[exchange_type][type][bags]["num"]
    print exchange_dic
if __name__ == '__main__':
#    test_dic()
#    testexchange()
#    test_dic2()
#    test_dic3()
#    test_unicode()
    process_dic()

