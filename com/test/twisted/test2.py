#-*- coding: utf-8 -*-
import time
def largeFibonnaciNumber():
    """
    耗时的事
    """
    TARGET = 10000

    first = 0
    second = 1
    
    for i in xrange(TARGET - 1):
        new = first + second
        first = second
        second = new
    time.sleep(3)
    return second

from twisted.internet import threads, reactor

def fibonacciCallback(result):
    """
    回调函数
    打印耗时函数的返回结果
    """
    print "largeFibonnaciNumber result =", result

def run():
    """
    主函数
    """
    # 将耗时函数放入另一个线程执行，返回一个deferred对象
    d = threads.deferToThread(largeFibonnaciNumber)
    # 添加回调函数
    d.addCallback(fibonacciCallback)
    print "1st line after the addition of the callback"
    print "2nd line after the addition of the callback"

if __name__ == '__main__':
    run()
    reactor.run()
