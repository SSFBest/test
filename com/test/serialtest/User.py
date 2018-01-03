#-*- coding: utf8 -*-
from com.test.serialtest.model import *
from com.test.serialtest.Roulette import *

class User(Serializer):
    #########################################
    seq_attrs = ['roulette']
    adv_seq_attrs=['roulette']
    obj_seq_attrs={'roulette':"roulette"}

    def __init__(self, uid=None):
        self.roulette ={}

    
    def test(self):
        print "----beford",self.roulette
        roul = self.roulette
        if not roul :
            roul = Roulette.install()
            self.roulette = roul
            print "----after",self.roulette
#            self.update(['roulette'])
        else:
            today = time.strftime('%Y-%m-%d')
            if roul.day_records['today'] != today:
                self.roulette.day_records.update({'refresh_times' : 0, 'roll_times' : 0, 'today' : time.strftime('%Y-%m-%d')})
                award = self.roulette.award
                self.roulette.award = [aw for aw in award if aw['invalidate_date'] > today]
                self.ext_info.update(['roulette'])
        temp_dic = {}
        leftNums = 3 - self.roulette.day_records['roll_times']
        temp_dic['state'] = roul.state
        temp_dic['leftNums'] = leftNums
#        temp_dic['refreshFlag'] = common_config.roulette['refreshFlag']
        return temp_dic
if __name__ == '__main__':
#    baseclass=derivedClass(1)
#    print "hello "
#    u=User()
#    print u.test()
    u=User()
    print u.get_adv_seq_attrs()
    print u.get_obj_seq_attrs()
    print u.get_seq_attrs()
