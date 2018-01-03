#-*- coding: utf8 -*-
'''
Created on 2010-7-28

@author: Administrator
'''

class MyClass(object):
    #调入用户全局信息
    '''
    @staticmethod
    def get_config(rk_user, params):
        data = {}
        aquarium = MAquarium.get(rk_user.uid)
        aquarium.correct_common_fish_state()
        #水族馆
        data['fishs'] = aquarium.fishs
        for key,value in data['fishs']['common_fish'].iteritems():
            value['hungry'] = value['food']/load_config.fish_config_trans(rk_user.locale)['common_fish'][value['name']]['food_amount']*100
        #用户
        data['user'] = rk_user.dumps()
        data['user']['game_info'] = None
        #用户配置信息
        settings = MUserSetting.get(rk_user.uid)
        if settings:
            data['user_setting'] = settings.personal_msg
        else:
            data['user_setting'] = None
        #商店包裹
        data['store'] = load_config.store_trans(rk_user.locale)
        #泡泡鱼
        data['bubble'] = {'open':load_config.bubble_config_trans(rk_user.locale)['open'],'day_max':load_config.bubble_config_trans(rk_user.locale)['day_max']}
        return 0,data
    '''


    def __init__(self,params):
        '''
        Constructor
        '''
if __name__ == '__main__':
    print "hi"
    
        