# -*- coding: utf-8 -*-

from datetime import datetime


def testGetRequest():
	publishtime='2015年3月25日 21:15'
	s=datetime.strptime(publishtime,'%Y年%m月%d日 %H:%M')
	print s


if __name__ == '__main__':
    testGetRequest()
#    testJson()
#    testGetRequest()