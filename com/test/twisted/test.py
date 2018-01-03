#-*- coding: utf-8 -*-

from twisted.internet import reactor
from twisted.enterprise import adbapi
dbpool=adbapi.ConnectionPool('MySQLdb',
            host='182.254.153.144',
            db='gameapps',
            user = 'developer',
            passwd = '12345678',
            charset='utf8',
            use_unicode=True
)
# 等同于cursor.execute(statement)，返回cursor.fetchall()：
def _getData(txn,user):
    print '1111'
    # 这将在一个线程中跑，所以我们可以使用阻塞方式的调用
    txn.execute('SELECT 1 ')
    # ……把txn当作游标来用吧……
    # result=txn.fetchall()
    # if result:
    #     return result
    # else:
    #     return None
    return None
def getData(user):
    print '55555555555555555555555555555555555555555555555555555555'
    try:
        d=dbpool.runInteraction(_getData,user)
    except Exception,e:
        print '111111111'
        print e
    return d
def printResult(data):
    if data!=None:
        print "：\n", data
    else:
        print "ddd"
getData("crackpot").addCallback(printResult)
# reactor.callLater(1,reactor.stop)
# reactor.run()