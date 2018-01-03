#-*- coding: utf-8 -*-

import random
import time
import datetime

'''
Created on 2010-7-2

@author: Administrator
'''
def random_choice(config):
    #config = [(0.1, 20), (0.2, 30), (0.7, 40)]
    #thesum = reduce(operator.add, [item[0] for item in config], 0)
    #if thesum>1:
    #    raise Exception, 'config error'
    
    r = random.random()
    print "r ",r
    kk = 0
    for item in config:
        kk += item[0]
        print "kk ",kk
        if r < kk:
            return item[1]
def random_test():
    print random.randint(12, 20)
def test_repeat():
    str = "abc"
    print str
    str = 5
    print str
    str = [2, 3, 5]
    print str
def test_power():
    i = 3
    print 3 * 2 ** 3
def test_if():
    award = True
    effect = 2 if award else False
    print effect

def test_for():
    today = time.strftime('%Y-%m-%d')
    award = [{"gift":{
     "farm": {
      "seeds": {
       "hudielan": 1
      }
     }
    }, "invalidate_date":"2010-12-30"},
    {"gift":{
     "farm": {
      "seeds": {
       "hudielan1": 1
      }
     }
    }, "invalidate_date":"2010-12-29"}]
    print today
    for aw in award:
        if aw['invalidate_date'] > today:
            print aw
        
    a = [aw for aw in award if aw['invalidate_date'] > today]
    print a
def test_fresh():
        data1 = [
        {
            'gift' : [
                (0.3, {'farm' : {'seeds' : {'xigua':1}}}),(0.7, 2), 
            ],'gold':[1,10],
        },
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'wuguChook':2}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'mulberry':3}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'milkCow':1}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'carrot':5}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'BaxiGui':1}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'jasmine':1}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'putianDuck':2}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'mexicocactus':1}}}), 
            ]
        },
     {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'nigerseed':1}}}), 
            ]
        },
        

]
        data = [
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'shizi':1}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'decorations' : {'hgneutral':1}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'common': {'gift_bags': {'hflibao_1':1,},},}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'common': {'gift_bags': {'hflibao_3':1,},},}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'carnation':1}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'violet':1}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'properties': { 'fertilizer': {'jisu':1,},},}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'properties': { 'fertilizer': {'yingyang':1}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'decorations'  : {'sanyue':1}}}), 
            ],
        },
     {
            'F_coin':(10,10),
        },

]
        state = list()
        for panel in data:
            print 'ddd'
            award = dict()
            if panel.has_key('gold'):
                gold = random.randint(panel['gold'][0], panel['gold'][1])
                award.update({'gold':gold})
            if panel.has_key('F_coin'):
                F_coin = random.randint(panel['F_coin'][0], panel['F_coin'][1])
                award.update({'F_coin':F_coin})
            if panel.has_key('gift'):
                gift = random_choice(panel['gift'])
                print gift
                if isinstance(gift, list):
                    gift = random_choice(gift)
                award.update({'gift':gift})
            state.append(award)
        return state
def test_roll():
        state1=[
   {
    "gold": 7817
   }, 
   {
    "gold": 420
   }, 
   {
    "gold": 29, 
    "gift": {
     "farm": {
      "seeds": {
       "fkmogu": 2
      }
     }
    }
   }, 
   {
    "gold": 85, 
    "gift": {
     "farm": {
      "seeds": {
       "tanhua": 1
      }
     }
    }
   }, 
   {
    "gift": {
     "farm": {
      "seeds": {
       "morningglory": 1
      }
     }
    }
   }, 
   {
    "gift": {
     "farm": {
      "seeds": {
       "hudielan": 1
      }
     }
    }
   }, 
   {
    "gift": {
     "ranch": {
      "babies": {
       "lanyijiaoxiao": 1
      }
     }
    }
   }, 
   {
    "gift": {
     "ranch": {
      "babies": {
       "qiaokeliguaishou": 1
      }
     }
    }
   }, 
   {
    "gift": {
     "ranch": {
      "babies": {
       "JiCiWeiXi": 1
      }
     }
    }
   }, 
   {
    "gift": {
     "ranch": {
      "babies": {
       "eyu": 1
      }
     }
    }
   }
  ]
        state=[
   {
    "gift": 1
   }, 
   {
    "gift": 2
   }, 
   {
    "gift": 1
   }, 
   {
    "gift": 2
   }, 
   {
    "gift": 0
   }, 
   {
    "gift": 1
   }, 
   {
    "gift": 2
   }, 
   {
    "gift": 0
   }, 
   {
    "gift": 2
   }, 
   {
    "gift": 1
   }
  ]
        roul = {
    'rou_switch': True,
    'refreshFlag': True,  # False就是变灰。不让用
    'rule': unicode('<b>转盘规则:</b><ul><li>매일  처음 3차는 골드를 사용하고, 그후 부터는 마일리지를 사용합니다 。</li><li>다이얼 우측 상단에 있는 “트로피를 바꾸기”를 클릭하면 트로피를 바꿀수 있습니다。 </li><li>반드시 ”트로피를 획득”을 클릭하여서 트로피를 찾아가야 합니다.트로피는 보자기에 들어갑니다,트로피는 찾아가지 않으면 자동으로 보자기에 들어가지 않으며 7일후에  실효합니다, ”트로피를 획득”이 클릭이 않되면 트로피가 이미 보자기에 들어가있습니다。</li></ul> ', 'utf-8'),   # 转盘规则
    'invalidate_days' : 7,              #奖品过期时间
    'refresh_coin' : 'F_coin',          #刷新需要的币种，如果为F_coin，会先遍历refresh_gold，如果为gold，则直接走算法
    'refresh_gold' : [0,0,0], #刷新前三次需要金币
    'refresh_base' : 2,                 
    'refresh_power' : 1,
    'roll_coin' : 'F_coin',
    'roll_gold' : [1,2,3,4,5],    #玩轮盘前三次需要的金币
    'roll_base' : 5,
    'roll_power' : 1,
    #十个轮盘面停止的几率，几率和为1
    'probability' : [(0.02, 0), (0.19, 1), (0.12, 2), (0.05, 3), (0.20, 4), (0.01, 5), (0.01, 6), (0.12, 7), (0.18, 8), (0.10, 9)],
    'data' : [
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'xigua':1}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'wuguChook':2}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'mulberry':3}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'milkCow':1}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'carrot':5}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'BaxiGui':1}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'jasmine':1}}}), 
            ]
        },
        {
            'gift' : [
                (1.00, {'ranch' : {'babies' : {'putianDuck':2}}}),
            ]
        },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'mexicocactus':1}}}), 
            ]
        },
     {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'nigerseed':1}}}), 
            ]
        },

],
    #神秘礼物，概率和为1
    'mystery' : [
        [
           (0.05, {'common' : {'gift_bags' : {'mb_8' : 1}}}), 
           (0.60, {'common' : {'gift_bags' : {'mb_4' : 1}}}), 
           (0.30, {'common' : {'gift_bags' : {'mb_6' : 1}}}), 
           (0.05, {'common' : {'gift_bags' : {'mb_7' : 1}}}), 

        ],

        [
            (0.50, {'common' : {'gift_bags' : {'hb_3' : 1}}}), 
            (0.30, {'common' : {'gift_bags' : {'hb_4' : 1}}}), 
            (0.20, {'common' : {'gift_bags' : {'hb_5' : 1}}}), 

        ],

        [
            (0.50, {'common' : {'gift_bags' : {'siliao_1' : 1}}}), 
            (0.30, {'common' : {'mystic_bags' : {'mb_10' : 1}}}), 
            (0.20, {'common' : {'mystic_bags' : {'mb_10_key' : 1}}}), 

        ],
    ],
}
        
        probability = roul['probability']
        mystery = roul['mystery']
        invalidate_days = roul['invalidate_days'] 
        
        i = random_choice(probability)
        print i
        award = state[i]
        if award.has_key('gift'):
            gift = award['gift']
            print "gift",gift
            if isinstance(gift, int):
                gift = random_choice(mystery[gift])
                award['gift'] = gift
        
        today = datetime.date.today()
        invalidate_date = datetime.date.today() + datetime.timedelta(days=invalidate_days)
        award['invalidate_date'] = datetime.datetime.strftime(invalidate_date, '%Y-%m-%d')
          
        return  dict({'no' : i, 'award' : award})
def add2dict(d, k, v):
    if d.has_key(k):
        d[k] += v
    else:
        d[k] = v
def test_stat_award(award,res=None):
    
    if res is None:
        res = {}
    for res_key in award:
        if res_key == 'F_coin':
            add2dict(res, 'F_coin', award['F_coin'])
        if res_key == 'gold':
            add2dict(res, 'gold', award['gold'])
        if res_key == 'gift':
            if not res.has_key('gift'):
                res['gift'] = {}
            gift = award['gift']
            for scene_type in gift :
                if not res['gift'].has_key(scene_type):
                    res['gift'][scene_type] = {}   
                for res_type in gift[scene_type]:
                    if  not res['gift'][scene_type].has_key(res_type):
                        res['gift'][scene_type][res_type] = {}
                    if res_type in ['seeds', 'babies', 'gift_bags', 'mystic_bags']: 
                        for name in gift[scene_type][res_type]:
                            add2dict(res['gift'][scene_type][res_type], name, gift[scene_type][res_type][name])
                    elif res_type in ['properties', 'decorations']:
                        for item_type in gift[scene_type][res_type]:
                            if not res['gift'][scene_type][res_type].has_key(item_type):
                                res['gift'][scene_type][res_type][item_type] = {}
                            for name in gift[scene_type][res_type][item_type]:
                                add2dict(res['gift'][scene_type][res_type][item_type], name, gift[scene_type][res_type][item_type][name])
                    else:
                        pass  
    
    return res   
def merge_dict2(d1, d2):
    d3={}
    if(d1!=None):
        d3 = d1.copy()
    for k in d2:
        if d3.has_key(k):
            d3[k] += d2[k]
        else:
            d3[k] = d2[k]
    return d3
def test_random_int():
    print random.randint(2,3)

def test_eval():
    str={
    'rou_switch': True,
    'refreshFlag': True,  # Falseﾾￍￊￇﾱ￤ﾻￒﾡﾣﾲﾻ￈ￃￓￃ
    'rule': unicode('<b>?? ?? ??:</b><ul><li>??  ?? 3?? ??? ????, ?? ??? ????? ????? ﾡﾣ</li><li>??? ?? ??? ?? ﾡﾰ???? ???ﾡﾱ? ???? ???? ??? ????ﾡﾣ </li><li>??? ﾡﾱ???? ??ﾡﾱ? ????? ???? ???? ???.???? ???? ?????,???? ???? ??? ???? ???? ???? ??? 7???  ?????, ﾡﾱ???? ??ﾡﾱ? ??? ??? ???? ?? ???? ???????ﾡﾣ</li></ul> ', 'utf-8'),   # ￗﾪￅￌﾹ￦ￔ￲
    'invalidate_days' : 7,              #ﾽﾱￆﾷﾹ�ￆￚￊﾱﾼ￤
    'refresh_coin' : 'F_coin',          #ￋﾢ￐ￂ￐￨ￒﾪﾵￄﾱￒￖￖﾣﾬ￈￧ﾹ￻ￎﾪF_coinﾣﾬﾻ￡ￏ￈ﾱ￩￀￺refresh_goldﾣﾬ￈￧ﾹ￻ￎﾪgoldﾣﾬￔ￲ￖﾱﾽￓￗ￟ￋ￣ﾷﾨ
    'refresh_gold' : [1,2,3], #ￋﾢ￐ￂￇﾰ￈�ﾴￎ￐￨ￒﾪﾽ￰ﾱￒ
    'refresh_base' : 2,                 
    'refresh_power' : 1,
    'roll_coin' : 'F_coin',
    'roll_gold' : [1,2,3,4,5],    #ￍ￦ￂￖￅￌￇﾰ￈�ﾴￎ￐￨ￒﾪﾵￄﾽ￰ﾱￒ
    'roll_base' : 5,
    'roll_power' : 1,
    #ￊﾮﾸ￶ￂￖￅￌￃ￦ￍﾣￖﾹﾵￄﾼﾸￂￊﾣﾬﾼﾸￂￊﾺￍￎﾪ1
    'probability' : [(0.02, 0), (0.19, 1), (0.12, 2), (0.05, 3), (0.20, 4), (0.01, 5), (0.01, 6), (0.12, 7), (0.18, 8), (0.10, 9)],
    'data' : [
         {
        'gold':(20,30),
     },
     {
        'F_coin':(1,10),
     },
        {
            'gift' : [
                (1.00, {'farm' : {'seeds' : {'xigua':1}}}), 
            ],
            'gold':(10,100)
        },
        {
            'gift' : [
                (0.23, {'ranch' : {'babies' : {'wuguChook':2}}}),(0.77, {'farm' : {'seeds' : {'mexicocactus':1}}})
            ],
        'gold':(1,20),
        'F_coin':(1,3),
        },
        {
            'gift' : [
                (0.29, {'farm' : {'seeds' : {'mulberry':3}}}), (0.71, {'farm' : {'seeds' : {'nigerseed':1}}}),
            ]
        },
        {
            'gift' : [
                (0.32, {'ranch' : {'babies' : {'milkCow':1}}}), (0.68, {'ranch' : {'babies' : {'beijingDuck':1}}}),
            ]
        },
        {
            'gift' : [
                (0.56, {'farm' : {'seeds' : {'carrot':5}}}), (0.44, {'farm' : {'seeds' : {'lavender':5}}}),
            ]
        },
        {
            'gift' : [
                (0.89, {'ranch' : {'babies' : {'goose':1}}}),(0.11, {'ranch' : {'babies' : {'BaxiGui':1}}}),
            ]
        },
        {
            'gift' : [
                (0.75, {'farm' : {'seeds' : {'jasmine':1}}}), (0.25, {'farm' : {'seeds' : {'sunflower':1}}}), 
            ]
        },
        {
            'gift' : [
                (0.3, {'ranch' : {'babies' : {'putianDuck':2}}}),(0.7, 2),
            ]
        },
],
    #￉￱ￃ￘￀￱ￎ￯ﾣﾬﾸￅￂￊﾺￍￎﾪ1
    'mystery' : [
        [
           (0.05, {'common' : {'gift_bags' : {'gb_4' : 1}}}), 
           (0.60, {'common' : {'gift_bags' : {'hb_1' : 1}}}), 
           (0.30, {'common' : {'gift_bags' : {'hflibao_1' : 1}}}), 
           (0.05, {'common' : {'gift_bags' : {'hflibao_2' : 1}}}), 

        ],

        [
            (0.50, {'common' : {'gift_bags' : {'lianhualibao' : 1}}}), 
            (0.30, {'common' : {'gift_bags' : {'sun_gift1' : 1}}}), 
            (0.20, {'common' : {'gift_bags' : {'sun_gift2' : 1}}}), 

        ],

        [
            (0.50, {'common' : {'gift_bags' : {'gao' : 1}}}), 
            (0.30, {'common' : {'mystic_bags' : {'mb_10' : 1}}}), 
            (0.20, {'common' : {'mystic_bags' : {'mb_10_key' : 1}}}), 

        ],
    ],
}
def test_dic():
    dic1={'house': [{'get_time': datetime.datetime(2010, 7, 13, 18, 8, 57, 973215), 'used': True, 'deadline': None, 'name': 'maocaowu'}, {'get_time': datetime.datetime(2010, 7, 13, 18, 35, 20, 264521), 'used': False, 'deadline': datetime.datetime(2010, 8, 12, 18, 35, 20, 264521), 'name': u'lianhuafz'}, {'get_time': datetime.datetime(2010, 7, 13, 18, 41, 21, 890657), 'used': False, 'deadline': datetime.datetime(2010, 9, 11, 18, 35, 20, 264521), 'name': u'lianhuafz'}]}
    dic1["house"].append({'get_time': datetime.datetime(2010, 7, 13, 18, 8, 57, 973215), 'used': True, 'deadline': None, 'name': 'maocaowu2'})
#    dic1["house"]=({'get_time': datetime.datetime(2010, 7, 13, 18, 8, 57, 973215), 'used': True, 'deadline': None, 'name': 'maocaowu2'})
    for item in range(len(dic1["house"])):
        print item,dic1["house"][item]
        if dic1["house"][item]['name'] == "maocaowu":
           dic1["house"][item]={'get_time': datetime.datetime(2010, 7, 13, 18, 8, 57, 973215), 'used': False, 'deadline': None, 'name': 'maocaowu2'}

    print dic1
def test_dic2():
    gift_dict={
                'seeds': {
                    'carnation':[2, 1.00],
                    'lily':[2, 1.00],
                },
                'properties': {
                    'fertilizer': {
                        'gaosu':[5, 1.00],
                        'jisu':[3, 1.00],
                    },
                },
                'decorations': {
                    'floor': {
                        'hgneutral':2,
                    },
                },
            }
    decorations={'floor':[{"name":"hgneutral"}]}
    if gift_dict.has_key('decorations'):
            for decoration in gift_dict['decorations']:
                if not decorations.has_key(decoration):
                    decorations[decoration]=[]
                for name in gift_dict['decorations'][decoration]:
                    for i in range(gift_dict['decorations'][decoration][name]):
                        for item in range(len(decorations[decoration])):
                            if decorations[decoration][item]['name'] == name:
                                print "ok"
                            else:
                                print ""
                            
    print decorations
def test_list():
    config_keys = (
    'title_config',
    'love_config',
    'skill_config',
    'fish_config',
    'food_config',
    'global_config',
    'lang_config',
    'item_config',
    'feed_config',
    'decoration_config',
    'level_gift_config',
    'system_config',
    'original_config',
    'notice_config',
    'bubble_config',
    'day_gift_config',
    'invite_config',
    'send_gift_config',
    'score_gift_config',
    'user_control_config',
    'rookie_mission_config',
    'mermaid_config',
#    'ship_mission_config',#沉船配置
    'jaws_mission_config',#大白鲨配置
    'sea_area_config', #海域配置
    'picture_config', #图鉴配置
    'question_config',#玩家反馈通道设置
    )
    print str(config_keys)
if __name__ == '__main__':
    config = [
                (1.00, {'farm' : {'seeds' : {'xigua':1}}}),
            ]
    config2=[
                (0.3, {'farm' : {'seeds' : {'xigua':1}}}),(0.7, 2), 
            ]
    config1 = [(0.02, 0), (0.19, 1), (0.12, 2), (0.05, 3), (0.20, 4), (0.01, 5), (0.01, 6), (0.12, 7), (0.18, 8), (0.10, 9)]
#    print random_choice(config2)
#    print random_test()
#    print test_repeat()
#    print test_power()
#    print test_if()
    test_for();
#    print test_fresh()
#    print test_roll()
############
#    award=[{'invalidate_date': '2010-07-12', 'gift': {'farm': {'seeds': {'lemon': 3}}}}, {'invalidate_date': '2010-07-12', 'gift': {'ranch': {'babies': {'wuguChook': 2}}}}, {'invalidate_date': '2010-07-12', 'gift': {'common': {'gift_bags': {'hb_3': 1}}}}]
#    goods={}
#    for every in award:
#        test_stat_award(every,goods)
#    print goods
##############
#    print merge_dict2(None,{'common': {'gift_bags': {'hb_3': 1}}})
###################
#    test_random_int()
#    test_dic()
#    test_dic2()
#    test_list()

    
    
