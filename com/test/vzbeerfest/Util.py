#-*- coding: utf-8 -*-
'''
Created on 2010-9-26

@author: Administrator
'''
def test1():
    dic={}
    if(dic.get("abc")):
        print "ok"
    dic["abc"]["def"]["md"]="yes"
    print dic
def test2():
    dic={}
    dic.update({"1":1})
    dic.update({"2":5})
    dic["1"]=4
    print dic
    dic.update({"abc":{"def":4}})
    print dic
    dic["abc"].update({"def2":5})
    print dic
def test3():
    if True:
        scene="abc"
    elif 4==4:
        scene="def"
    if scene:
        print scene
def test4():
    dic={"goods_type":{"farm":{"seeds":{"beer":68}}}}
    print dic["goods_type"]["farm"]["seeds"].keys()[0]
def processDic():
    exchangeInfo={
               "1":{
                   "farm":{
                        "seeds":{
                            "ziwu1":300
                         },
                         'properties': {
                                  'feedstuffs': {
                                       'common': 600,
                                   },
                        },
                    },
               },
              "2":{
                  "ranch":{
                       "babies":{
                             "heixing":300
                        },
                        'properties': {
                                  'feedstuffs': {
                                       'common': 600,
                                   },
                        },
                  }
              },
              "3":{
                  'common' : { 
                        'gift_bags' : { 
                                'zhongqiujielibao': 300,
                         }
                  }
               }
          }
    statInfo={"farm.seeds.ziwu1":30}   
    for exchange_id in exchangeInfo:
        for scene_type in exchangeInfo[exchange_id]:
            if scene_type=="farm":
                for type in exchangeInfo[exchange_id][scene_type]:
                    if(type=="seeds"):
                        for crops in exchangeInfo[exchange_id][scene_type][type]:
                            total=statInfo.get("%s.%s.%s"%(scene_type,type,crops),0)
                            exchangeInfo[exchange_id][scene_type][type][crops]={"num":exchangeInfo[exchange_id][scene_type][type][crops],"total":total}
                    if(type=="properties" or type=="decorations"):
                            for subtype in exchangeInfo[exchange_id][scene_type][type]:
                                for sub_subtype in exchangeInfo[exchange_id][scene_type][type][subtype]:
                                    total=statInfo.get("%s.%s.%s.%s"%(scene_type,type,subtype,sub_subtype),0)
                                    exchangeInfo[exchange_id][scene_type][type][subtype][sub_subtype]={"num":exchangeInfo[exchange_id][scene_type][type][subtype][sub_subtype],"total":total}
            if scene_type=="ranch":
                for type in exchangeInfo[exchange_id][scene_type]:
                    if type=="babies":
                        for babys in exchangeInfo[exchange_id][scene_type][type]:
                            total=statInfo.get("%s.%s.%s"%(scene_type,type,babys),0)
                            exchangeInfo[exchange_id][scene_type][type][babys]={"num":exchangeInfo[exchange_id][scene_type][type][babys],"total":total}
                    if(type=="properties" or type=="decorations"):
                            for subtype in exchangeInfo[exchange_id][scene_type][type]:
                                for sub_subtype in exchangeInfo[exchange_id][scene_type][type][subtype]:
                                    total=statInfo.get("%s.%s.%s.%s"%(scene_type,type,subtype,sub_subtype),0)
                                    exchangeInfo[exchange_id][scene_type][type][subtype][sub_subtype]={"num":exchangeInfo[exchange_id][scene_type][type][subtype][sub_subtype],"total":total}
            if(scene_type=="common"):
                    for type in exchangeInfo[exchange_id][scene_type]:
                        for bags in exchangeInfo[exchange_id][scene_type][type]:
                            total=statInfo.get("%s.%s.%s"%(scene_type,type,bags),0)
                            exchangeInfo[exchange_id][scene_type][type][bags]={"num":exchangeInfo[exchange_id][scene_type][type][bags],"total":total}
    print exchangeInfo
def test5():
    dic={"exchaged":[{"":{"a":1}}]}
    dic.get("exchanged",[])
if __name__ == '__main__':
    award={
           "farm":{"seeds":{"grapes":5,"putao":10}},
             "ranch":{"babies":{"dog":12,"pig":10}}
}
#    testCollect(award,"a_type")
#    testdicone()
#    testNullDic()
    test2()
#    test_dic2()
#    test3()
#    test4()
#    processDic()