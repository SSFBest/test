#-*- coding: utf-8 -*-

#import operator

def test():
    print "test is running"

if __name__ == "__main__":#自运行时调用该程序块
    print "test main is working"
    print "a","b",True
    ck='title_config'
    title_config_isinstance_config_value={
#####################################################################
  'configs':{
      'fertilizer': {
            'common': {
                'name': unicode('%(fertilizer_common_name)s', 'utf-8'),
                'intro': unicode('', 'utf-8'),
                'used':False,
                'price': {'gold':30,'F_coin':10},
                'effect': 30,
            },
         },
     },
   
   'trans':{
       'en':{
             'fertilizer_common_name': unicode('This is a example', 'utf-8'),
            },
       'zh':{
             'fertilizer_common_name': unicode('这是一个例子', 'utf-8'),
            },
     },
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
    print title_config_trans("en")
    print '---'
    print float(0.0)

if __name__ == "test":#import时调用该程序块
    print "test is invoked"
    print "a","b",True
    
    
    
