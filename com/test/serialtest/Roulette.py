#-*- coding: utf8 -*-
import random, time, datetime
from com.test.serialtest.model import *
from com.test.util.utils import *

class Roulette(Serializer):
    seq_attrs = ['award', 'state', 'day_records']
    
    def __init__(self):
        self.state = self.refresh()
        self.day_records = {'refresh_times' : 0, 'roll_times' : 0, 'today' : time.strftime('%Y-%m-%d')}
        self.award = []

    @staticmethod
    def install():
        return Roulette()
        
    @staticmethod
    def refresh():
        data = [
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
        ]
        state = list()
        for panel in data:
            award = dict()
            if panel.has_key('gold'):
                gold = random.randint(panel['gold'][0], panel['gold'][1])
                award.update({'gold':gold})
            if panel.has_key('F_coin'):
                F_coin = random.randint(panel['F_coin'][0], panel['F_coin'][1])
                award.update({'F_coin':F_coin})
            if panel.has_key('gift'):
                gift = random_choice(panel['gift'])
                if isinstance(gift, list):
                    gift = random_choice(gift)
                award.update({'gift':gift})
            state.append(award)
        return state
    
    
    
    