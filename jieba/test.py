#-*- coding: utf8 -*-

import jieba
import jieba.analyse
jieba.load_userdict("D:/mywork/lib/jieba/userdict.txt")
seg_list = jieba.cut("我来到北京清华大学", cut_all=True,HMM=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False,HMM=True)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("生日礼物满天星", cut_all=True,HMM=True)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("中老年连衣裙",cut_all=False,HMM=True)  # 默认是精确模式
print(", ".join(seg_list))
seg_list = jieba.cut("加绒儿童打底裤女童冬季加厚裤子纯棉韩版公主童裤外穿打底裤",cut_all=True,HMM=True)  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("中老年连衣裙")  # 搜索引擎模式
print(", ".join(seg_list))

print('__'*10)
jieba.load_userdict("D:/mywork/lib/jieba/userdict.txt")
jieba.analyse.set_idf_path("D:/mywork/lib/jieba/idf.txt");
content='天干物燥 冬季低温爱车也要防自燃'

tags = jieba.analyse.extract_tags(content,topK=20,withWeight=False,HMM=False,allowPOS=('n','nz','nr'))
for tag in tags:
	# print('%s:%s'%(tag[0],tag[1]))
	print tag