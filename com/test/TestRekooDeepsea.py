#-*- coding: utf-8 -*-
import operator

'''
Created on 2010-7-19

@author: Administrator
'''
def test_question():
    ck='title_config'
    title_config_isinstance_config_value={
#####################################################################
  'configs':{
      'feedstuffs': {
            'fast': {
                'name': unicode('%(feedstuffs_fast_name)s', 'utf-8'),
                'intro': unicode('%(feedstuffs_fast_intro)s', 'utf-8'),
                'used':True,
                'price': {'gold':0,'F_coin':2},
                'effect': 2.5,
                'point':20,
            },
            'high': {
                'name': unicode('%(feedstuffs_high_name)s', 'utf-8'),
                'intro': unicode('%(feedstuffs_high_intro)s', 'utf-8'),
                'used':True,
                'price': {'gold':0,'F_coin':4},
                'effect': 6,
                'point':40,
            },
            'magic': {
                'name': unicode('%(feedstuffs_magic_name)s', 'utf-8'),
                'intro': unicode('%(feedstuffs_magic_intro)s', 'utf-8'),
                'used':True,
                'price': {'gold':0,'F_coin':8},
                'effect': 100,
                'point':60,
            },
         },
       'cameo':{
            'greencameo': {
                'name': unicode('%(cameo_green_name)s', 'utf-8'),
                'intro': unicode('%(cameo_green_intro)s', 'utf-8'),
                'used':True,
                'price': {'gold':3,'F_coin':1},
                'effect': 30,
                'point':12,
            },
      },

     },
   
   'trans':{
       'en':{
             'feedstuffs_fast_name': unicode('쾌속 사료', 'utf-8'),
             'feedstuffs_high_name': unicode('고속 사료', 'utf-8'),
             'feedstuffs_magic_name': unicode('마력 사료', 'utf-8'),
             'cameo_green_name':unicode('绿宝石', 'utf-8'),
             'feedstuffs_fast_intro': unicode('쾌속 사료를 사고, 사용해면  2.5시간 물고기의 성장 시간을 단축할 수 있고, 일찌감치 수확해서 다른 사람이 당신의 노동 성과를 따 잡는 것을 방지할 수 있습니다', 'utf-8'),
             'feedstuffs_high_intro': unicode('고속 사료를 사고, 사용해면  6시간 물고기의 성장 시간을 단축할 수 있고, 일찌감치 수확해서 다른 사람이 당신의 노동 성과를 따 잡는 것을 방지할 수 있습니다 ', 'utf-8'),
             'feedstuffs_magic_intro': unicode('마력 사료를 사고, 사용후 직접 다음 성장단계로 이동 할수 있어요, 일찌감치 수확해서 다른 사람이 당신의 노동 성과를 따 잡는 것을 방지할 수 있습니다', 'utf-8'),
             'cameo_green_intro':unicode('绿宝石', 'utf-8'),
            },
       'zh':{
             'feedstuffs_fast_name': unicode('这是一个例子', 'utf-8'),
             'cameo_green_name':unicode('This is a example', 'utf-8'),
             'feedstuffs_high_name': unicode('This is a example', 'utf-8'),
             'feedstuffs_magic_name': unicode('This is a example', 'utf-8'),
             'feedstuffs_fast_intro': unicode('中级饲料', 'utf-8'),
             'feedstuffs_high_intro': unicode('中级饲料', 'utf-8'),
             'feedstuffs_magic_intro': unicode('中级饲料', 'utf-8'),
             'cameo_green_intro':unicode('绿宝石', 'utf-8'),
            },
     },
#####################################################################
}
    trans=''
    configs=''
    lang_locale = {
    'default' : 'en',
    'en' : 'en',
    'zh' : 'zh'
}
    exec('trans, configs = '+ck+'_isinstance_config_value["trans"], unicode('+ck+'_isinstance_config_value["configs"])')
    print trans
    print configs
    title_config_trans=''
    title_config_generate_config_value={}
    for t in trans:
        exec(ck+'_generate_config_value[t] = eval(configs % trans[t])')
    print title_config_generate_config_value
    exec(ck+'_trans=lambda k="default":'+ck+'_generate_config_value.get(lang_locale.get(k,"en")) or '+ck+'_generate_config_value[lang_locale["default"]]')
    print title_config_trans
    print lang_locale["default"]
    title_config_generate_config_value={'en': {'cameo': {'greencameo': {'used': True, 'name': u'\u7eff\u5b9d\u77f3', 'point': 12, 'price': {'F_coin': 1, 'gold': 3}, 'effect': 30, 'intro': u'\u7eff\u5b9d\u77f3'}}, 'feedstuffs': {'high': {'used': True, 'name': u'\uace0\uc18d \uc0ac\ub8cc', 'point': 40, 'price': {'F_coin': 4, 'gold': 0}, 'effect': 6, 'intro': u'\uace0\uc18d \uc0ac\ub8cc\ub97c \uc0ac\uace0, \uc0ac\uc6a9\ud574\uba74  6\uc2dc\uac04 \ubb3c\uace0\uae30\uc758 \uc131\uc7a5 \uc2dc\uac04\uc744 \ub2e8\ucd95\ud560 \uc218 \uc788\uace0, \uc77c\ucc0c\uac10\uce58 \uc218\ud655\ud574\uc11c \ub2e4\ub978 \uc0ac\ub78c\uc774 \ub2f9\uc2e0\uc758 \ub178\ub3d9 \uc131\uacfc\ub97c \ub530 \uc7a1\ub294 \uac83\uc744 \ubc29\uc9c0\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4 '}, 'magic': {'used': True, 'name': u'\ub9c8\ub825 \uc0ac\ub8cc', 'point': 60, 'price': {'F_coin': 8, 'gold': 0}, 'effect': 100, 'intro': u'\ub9c8\ub825 \uc0ac\ub8cc\ub97c \uc0ac\uace0, \uc0ac\uc6a9\ud6c4 \uc9c1\uc811 \ub2e4\uc74c \uc131\uc7a5\ub2e8\uacc4\ub85c \uc774\ub3d9 \ud560\uc218 \uc788\uc5b4\uc694, \uc77c\ucc0c\uac10\uce58 \uc218\ud655\ud574\uc11c \ub2e4\ub978 \uc0ac\ub78c\uc774 \ub2f9\uc2e0\uc758 \ub178\ub3d9 \uc131\uacfc\ub97c \ub530 \uc7a1\ub294 \uac83\uc744 \ubc29\uc9c0\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4'}, 'fast': {'used': True, 'name': u'\ucf8c\uc18d \uc0ac\ub8cc', 'point': 20, 'price': {'F_coin': 2, 'gold': 0}, 'effect': 2.5, 'intro': u'\ucf8c\uc18d \uc0ac\ub8cc\ub97c \uc0ac\uace0, \uc0ac\uc6a9\ud574\uba74  2.5\uc2dc\uac04 \ubb3c\uace0\uae30\uc758 \uc131\uc7a5 \uc2dc\uac04\uc744 \ub2e8\ucd95\ud560 \uc218 \uc788\uace0, \uc77c\ucc0c\uac10\uce58 \uc218\ud655\ud574\uc11c \ub2e4\ub978 \uc0ac\ub78c\uc774 \ub2f9\uc2e0\uc758 \ub178\ub3d9 \uc131\uacfc\ub97c \ub530 \uc7a1\ub294 \uac83\uc744 \ubc29\uc9c0\ud560 \uc218 \uc788\uc2b5\ub2c8\ub2e4'}}}, 'zh': {'cameo': {'greencameo': {'used': True, 'name': u'This is a example', 'point': 12, 'price': {'F_coin': 1, 'gold': 3}, 'effect': 30, 'intro': u'\u7eff\u5b9d\u77f3'}}, 'feedstuffs': {'high': {'used': True, 'name': u'This is a example', 'point': 40, 'price': {'F_coin': 4, 'gold': 0}, 'effect': 6, 'intro': u'\u4e2d\u7ea7\u9972\u6599'}, 'magic': {'used': True, 'name': u'This is a example', 'point': 60, 'price': {'F_coin': 8, 'gold': 0}, 'effect': 100, 'intro': u'\u4e2d\u7ea7\u9972\u6599'}, 'fast': {'used': True, 'name': u'\u8fd9\u662f\u4e00\u4e2a\u4f8b\u5b50', 'point': 20, 'price': {'F_coin': 2, 'gold': 0}, 'effect': 2.5, 'intro': u'\u4e2d\u7ea7\u9972\u6599'}}}}
#    print title_config_trans("en")
    print title_config_generate_config_value.get("en")
    item_list = manageDict(title_config_generate_config_value.get("en"),'item_list',[])
    print item_list
    item_list = manageList(item_list)
    print item_list
def sort_dict(d,reverse=False):
        return sorted(d.iteritems(), key=operator.itemgetter(1), reverse=False)
def test_order():
    sort_fish={}
    order_fish={}
    d={
       'common_fish':{
                      'yueguangdie':{
                          'name':unicode('%(common_fish_yueguangdie_name)s','utf-8'),#???ﾩV??
                          'used':False,
                          'shop_type':'fans',
                          'baby':{
                              'name':unicode('','utf-8')
                           },
              'need_level':0,
              'ocean_deep':'deep_1',
              'food_amount':100,
              'hour_food':10,
              'achieve_count':1,
              'grow_time':{
                    'infancyFish':0.2,
                    'smallFish':0.2,
                    'middleFish':0.2,
                    'bigFish':0.2,
                    'adultFish':1,
                    're_grow':0,
                     },
              'gold':{
                    'normal':420,
                    'max':504,
                    'min':294,
                },
             'point':60,
             'price':{
                    'gold':100,
                    'F_coin':0,
               }
              },
              'xiaoyiyu':{
                          'name':unicode('%(common_fish_yueguangdie_name)s','utf-8'),#???ﾩV??
                          'used':False,
                          'shop_type':'fans',
                          'baby':{
                              'name':unicode('','utf-8')
                           },
              'need_level':1,
              'ocean_deep':'deep_1',
              'food_amount':100,
              'hour_food':10,
              'achieve_count':1,
              'grow_time':{
                    'infancyFish':0.2,
                    'smallFish':0.2,
                    'middleFish':0.2,
                    'bigFish':0.2,
                    'adultFish':1,
                    're_grow':0,
                     },
              'gold':{
                    'normal':420,
                    'max':504,
                    'min':294,
                },
             'point':60,
             'price':{
                    'gold':100,
                    'F_coin':0,
               }
              },
                   }
       }
    for key,value in d['common_fish'].iteritems():
        #排序用
        sort_fish[key] = value['need_level']
        if d['common_fish'][key].get('order'):
            order_fish[key] = value['order']
    print "sort_fish:",sort_fish
    print "order_fish:",order_fish
    print 'sorted_fish',sort_dict(sort_fish)
    for key in sort_dict(sort_fish):
        print key[0]
def test_extend_append():
    print "start"
    a=[1,2,3,4]
    b=[5,6,7]
    c=[8,9,0]
    a.append(b)
    b.extend(c)
    print a
    print b
def manageDict(dicts,pre_value,zlist=[]):
    r_list = []
    if dicts and type(dicts) == type({}):
        if 'name' in dicts.keys():
            r_list.append(pre_value)
            r_list.append(dicts['name'])        
            zlist.append(r_list)
        else:
              for it in dicts.keys():
                  if type(dicts[it]) == type({}):
                    t_pre = pre_value + '|' + it
                    r_list += manageDict(dicts[it],t_pre,zlist)
               
    return zlist
def manageList(dlist):
    t_list = []
    if dlist:
        for tt in dlist:
            t_i = -1
            try:
                t_i = t_list.index(tt)
            except:
                t_i = -1
            if t_i == -1:
                t_list.append(tt)
    return t_list

if __name__ == '__main__':
    test_question()
#    test_order()
#    test_extend_append()