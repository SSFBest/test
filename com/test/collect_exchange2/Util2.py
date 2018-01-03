#-*- coding: utf-8 -*-
'''
Created on 2010-9-16

@author: Administrator
'''
def testdic():
    collectexchange2={
          "used":True,                   #入口开关
         "activity":{ 
           "duihuan1":{                       #活动1
               "used":True,                 #活动1开关
               "need":{                        #收集需求
                     "farm":{
                            "seeds":{
                                   "songbing":990,"songshu":990
                            },
                            "harvest":{
                                   "songbing":990,"songshu":990
                            },
                            'properties': {
                                  'fertilizer': {
                                       'jisu': 1,  #急速化肥
                                   },
                            },
                       },
                     "ranch":{
                           "babies":{
                               "yutu":990,"jinsexiaomifeng":990
                           },
                           "harvest":{
                               "dog":5,"sheep":10
                           },
                            'properties': {
                                 'feedstuffs': {
                                       'common': 3
                                   },
                            },
                      },
                     "gold":50,
                     "F_coin":60,
                   },
                  "exchange":{              #兑换奖励
                        "gold":40000,
                        "F_coin":50,
                         "farm_experience":8000,
                         "ranch_experience":5000,
                        'farm' : {
                                'seeds' : {
                                       'yutuhua':7, #玉兔花
                                }, 
                            'properties': {
                                  'fertilizer': {
                                       'jisu': 9,  #急速化肥
                                   },
                             },
                            'decorations' : {
                                 'floor' : {
                                       'zhongqiujie':8,    #中秋节地板装饰品
                                }, 
                                 'sky' : {
                                       'zhongqiujie':2,   #中秋节天空装饰品
                                }, 
                                 'house' : {
                                       'zhongqiujie':2,   #中秋节房子装饰品
                                }, 
                               'butterfly' : {
                                       'youming':1,   #深渊幽冥蝶
                                }, 
                            }, 
                         }, 
                        'ranch':  {
                                'babies' : {
                                       'liumangtu':3,  #流氓兔宝宝
                            },
                            'properties': {
                                  'feedstuffs': {
                                       'common': 1,  #普通饲料
                                   },
                             },
                        } ,  
                        'common' : { 
                            'gift_bags' : { 
                                       'zhongqiujielibao': 7,   #中秋节礼包
                             },
                            'mystic_bags' : { 
                                       'mb_11': 3,   #宝箱
                                   },
                            },
                       },
                 },
#############################################################################
             "duihuan2":{                    #活动2
                  "used":True,                #活动2开关
                  "need":{                      #收集需求
                     "farm":{"seeds":{"songbing":990,"songshu":990}},
                     "ranch":{"babies":{"yutu":990,"jinsexiaomifeng":990}},
                   },
                  "exchange":{               #兑换奖励
                        'farm' : {
                                 'seeds' : {
                                        'mianju':{"num":1,"tips":"가면1"}, #面具1
                             },
                        }, 
                   },
             },
#############################################################################
           "duihuan3":{                       #活动3
               "used":True,                 #活动3开关
               "need":{                        #收集需求
                     "farm":{"seeds":{"songbing":990,"songshu":990}},
                     "ranch":{"babies":{"yutu":990,"jinsexiaomifeng":990}},
                   },
                  "exchange":{              #兑换奖励
                        'ranch':  {
                                  'babies' : {
                                       'baiqie':{"num":1,"tips":"흰 펭귄"},  #白企鹅
                            },
                        } ,   
                   },
              },
#############################################################################
       },
       "rule":"规则",
       "msg":{
         "0":unicode('0.', 'utf-8'),   #兑换成功
         "1":unicode('1.', 'utf-8'),      ##你还没有开始使用种植场
         "2":unicode('2.','utf-8'),             #需要种植场作物种子你还没有收集完成
         "3":unicode('3.', 'utf-8'),    #需要种植场仓库作物果实你还没有收集完成
         "4":unicode('4.', 'utf-8'),        #需要的牧场道剧你还没有收集完成
         "5":unicode('5.', 'utf-8'),       #你还没初始化畜牧场
         "6":unicode('6.', 'utf-8'),       #需要畜牧场动物宝宝你还没有收集完成 
         "7":unicode('7.', 'utf-8'),       #需要仓库中成熟动物你还没有收集完成
         "8":unicode('8.', 'utf-8'),       #需要畜牧场道剧你还没有收集完成
         "9":unicode('9.', 'utf-8'),       #金币不足
         "10":unicode('10.', 'utf-8'),       #酷币不足
         "11":unicode('11.', 'utf-8'),       #没有开始此活动，或者此活动已经结束
       }
   }
      
    activitys = collectexchange2["activity"] 
    scene={'fertilizer': {'shiyong': 1, 'jisu': 1, u'ceshi': 99979, 'tejiahuafei': 5}, 'pest': {}}
    need_dic = activitys["duihuan1"]["need"]
    for crops_type in need_dic["farm"]["properties"]:
        print 'crops_type',crops_type
        if(scene.has_key(crops_type)):
            for prop_type in need_dic["farm"]['properties'][crops_type]:
                print 'prop_type',prop_type
                need_dic["farm"]['properties'][crops_type][prop_type] = scene[crops_type].get(prop_type, 0) if scene else 0
                print need_dic["farm"]['properties'][crops_type][prop_type]
            
#    scene.seeds={'songshu': 990, 'ziluobo1': 1, 'songbing': 990}
#    scene.harvest={'songshu': 990, u'ziluobo1': 25, u'hongluobo1': 25, u'bailuobo1': 25, 'songbing': 990, u'huangluobo1': 25}
#    scene.properties={'fertilizer': {'shiyong': 1, 'jisu': 1, u'ceshi': 99979, 'tejiahuafei': 5}, 'pest': {}}
#    scene.babies={'jinsexiaomifeng': 990, 'yutu': 990}
    
  
def testdic2():
    scene={"seeds":{}}
    scene.seeds={
           'seeds':{'songshu': 990, 'ziluobo1': 1, 'songbing': 990},
           'harvest':{'songshu': 990, u'ziluobo1': 25, u'hongluobo1': 25, u'bailuobo1': 25, 'songbing': 990, u'huangluobo1': 25},
           'properties':{'fertilizer': {'shiyong': 1, 'jisu': 1, u'ceshi': 99979, 'tejiahuafei': 5}, 'pest': {}},
           'babies':{'jinsexiaomifeng': 990, 'yutu': 990}
           }
    print scene.seeds
if __name__ == '__main__':
#    testdic2()
    testdic()


