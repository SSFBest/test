#-*- coding: utf8 -*-

import xlrd,re,logging,sys

from yuelianglib.logics.jd_config import one,two,three

log_console = logging.StreamHandler(sys.stderr)
default_logger = logging.getLogger(__name__)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)

def test():
	word_long={
		u'充电式儿童理发器男人':1
	}
	word_short={
		u'充电式儿童':1,
		u'儿童':1,
		u'理发器':1,
	}
	word_long_final={}
	for sentence in word_long.iterkeys():
		sentence_arr=[]
		N = len(sentence)
		print N
		DAG = {}
		for k in xrange(N):
			tmplist = []
			i = k
			frag = sentence[k]
			while i < N :
				if word_short.has_key(frag):
					tmplist.append(i)
				i += 1
				frag = sentence[k:i + 1]
			if not tmplist:
				tmplist.append(k)
			DAG[k] = tmplist
		old_j = -1
		print DAG
		for k, L in DAG.items():
			if len(L) == 1 and k > old_j:
				# yield sentence[k:L[0] + 1]
				sentence_arr.append(sentence[k:L[0] + 1])
				old_j = L[0]
			elif k>old_j:
				for j in L[-1:]:
					if j > k:
						# yield sentence[k:j + 1]
						sentence_arr.append(sentence[k:j + 1])
						old_j = j
			else:
				pass
		print sentence_arr
		if sentence_arr:
			final=[]
			print sentence_arr[:1]
			print sentence_arr[-1:]
			if sentence_arr[:1]!=sentence_arr[-1:]:
				b=[]
				b[0:0]=sentence_arr[-1:]
				b[0:0]=sentence_arr[:1]
				final_str=''.join(b)
				if final_str not in final:
					final.append(final_str)
			if sentence_arr[:1]!=sentence_arr[-2:-1]:
				b=[]
				b[0:0]=sentence_arr[-2:-1]
				b[0:0]=sentence_arr[:1]
				final_str=''.join(b)
				if final_str not in final:
					final.append(final_str)
			if sentence_arr[1:2]!=sentence_arr[-2:-1]:
				b=[]
				b[0:0]=sentence_arr[-2:-1]
				b[0:0]=sentence_arr[1:2]
				final_str=''.join(b)
				if final_str not in final:
					final.append(final_str)	
			if sentence_arr[1:2]!=sentence_arr[-1:]:
				b=[]
				b[0:0]=sentence_arr[-1:]
				b[0:0]=sentence_arr[1:2]
				final_str=''.join(b)
				if final_str not in final:
					final.append(final_str)
			for f in final:
				print f.encode('utf8')

def remove_last(a):
	
	if a[-1:] in [u'女',u'男',u'春',u'夏',u'秋',u'冬']:
		return remove_last(a[0:-1])
	if a[-2:] in [u'女童',u'男童',u'女士',u'男士',u'女式',u'男式',u'女款',u'男款',u'春季',u'夏季',u'秋季',u'冬季',u'春夏',u'夏秋',u'秋冬',u'春天',u'夏天',u'秋天',u'冬天']:
		return remove_last(a[0:-2])
	else:
		return a

def read_ci(path,word,word_short,word_long):
	data = xlrd.open_workbook(path)  #打开文件
	table = data.sheets()[0] #通过索引顺序获取
	# table = data.sheet_by_index(0) #通过索引顺序获取
	# table = data.sheet_by_name(u'Sheet1')#通过名称获取
	# 获取整行和整列的值（数组）
	# table.row_values(i)
	# table.col_values(i)
	# 获取行数和列数
	nrows = table.nrows
	ncols = table.ncols

	# word={}
	# 循环行列表数据
	for r in xrange(1,nrows):
		for c in xrange(1,ncols):
			col=table.cell(r,c).value
			col_attr=re.split(u'[^\u4E00-\u9FD5a-zA-Z0-9]',col.strip())
			for w in col_attr:
				if not w:
					continue
				if len(w)>3:
					w=remove_last(w)
				if len(w)<2:
					# print w
					continue
				if len(w)>5:
					if w not in word_long:
						word_long.setdefault(w,1)
				else:
					m=re.search('([a-zA-Z0-9]{2,})',w)
					if m:
						s_w=m.group(1)
						if s_w not in word_short:
							word_short.setdefault(s_w,1)
					if w not in word_short:
						word_short.setdefault(w,1)
					# if w not in word:
					# 	word.setdefault(w,1)
				# else:
				# 	word_short[w]+=1

	
def process():
	word={}
	word_short={
		u'女童':1,
		u'男童':1,
		u'女士':1,
		u'男士':1,
		u'女式':1,
		u'男式':1,
		u'春季':1,
		u'夏季':1,
		u'秋季':1,
		u'冬季':1,
		u'春夏':1,
		u'夏秋':1,
		u'秋冬':1,
		u'春天':1,
		u'夏天':1,
		u'秋天':1,
		u'冬天':1,
		u'男款':1,
		u'女款':1,
		u'男用':1,
		u'女用':1,
		u'老年':1,
		u'爸爸':1,
		u'妈妈':1,
	}
	f = open('D:/projects/python_projects/pytest/src/excel/xlrd/1.txt', 'rb')
	for lineno, ln in enumerate(f, 1):
			line = ln.strip()
			if line not in word_short:
				# print type(line)
				if not isinstance(line, unicode):
					try:
						line = line.decode('utf-8').lstrip(u'\ufeff')
					except UnicodeDecodeError:
						raise ValueError('dictionary file %s must be utf-8' % f_name)
				if not line:
					continue
				# print type(line)
				word_short.setdefault(line,1)
	# print word_short
	word_long={}
	read_ci('D:/projects/python_projects/pytest/src/excel/word/top_20_wan_pc.xlsx',word,word_short,word_long)
	read_ci('D:/projects/python_projects/pytest/src/excel/word/top_20_wan_wl.xlsx',word,word_short,word_long)

	for sentence in word_long.iterkeys():
		m=re.search('([a-zA-Z0-9]{2,})',sentence)
		if m:
			s_w=m.group(1)
			# print s_w
			if s_w not in word_short:
				# print s_w
				word_short.setdefault(s_w,1)
		sentence_arr=[]
		N = len(sentence)
		DAG = {}
		for k in xrange(N):
			tmplist = []
			i = k
			frag = sentence[k]
			while i < N :
				if word_short.has_key(frag):
					tmplist.append(i)
				i += 1
				frag = sentence[k:i + 1]
			if not tmplist:
				tmplist.append(k)
			DAG[k] = tmplist
		old_j = -1

		for k, L in DAG.items():
			if len(L) == 1 and k > old_j:
				# yield sentence[k:L[0] + 1]
				# print sentence
				# if k == L[0]:
				# 	print sentence[k:L[0] + 1],sentence
				if sentence[k:L[0] + 1] in [u'女',u'男',u'春',u'夏',u'秋',u'冬',u'女童',u'男童',u'女士',u'男士',u'女式',u'男式',u'女款',u'男款',u'春季',u'夏季',u'秋季',u'冬季',u'春夏',u'夏秋',u'秋冬',u'春天',u'夏天',u'秋天',u'冬天']:
					if sentence[k:L[0] + 1] not in sentence_arr:
						sentence_arr.insert(0,u'%s'%sentence[k:L[0] + 1])
				else:
					sentence_arr.append(sentence[k:L[0] + 1])
				old_j = L[0]
			elif k>old_j:
				for j in L[-1:]:
					if j > k:
						# yield sentence[k:j + 1]
						sentence_arr.append(sentence[k:j + 1])
						old_j = j
			else:
				pass
		if sentence_arr and len(sentence_arr)>2:
			final=[]
			one=sentence_arr[:1][0]
			two=sentence_arr[1:2][0]
			last=sentence_arr[-1:][0]
			last_two=sentence_arr[-2:-1][0]
			for s in sentence_arr:
				default_logger.debug('h:%s'%(s))
			default_logger.debug('%s'%(''.join(sentence_arr)))
			default_logger.debug('%s,%s,%s,%s'%(one,two,last,last_two))


			if one!=last and 1<len(one)<5 and 1<len(last)<5 :
				b=[]
				b.append(one)
				b.append(last)
				final_str=''.join(b)
				if final_str not in final:
					final.append(final_str)
			if one!=last_two and 1<len(one)<5 and 1<len(last_two)<5:
				b=[]
				b.append(one)
				b.append(last_two)
				final_str=''.join(b)
				if final_str not in final:
					final.append(final_str)
			if two!=last_two and 1<len(two)<5 and 1<len(last_two)<5:
				b=[]
				b.append(two)
				b.append(last_two)
				final_str=''.join(b)
				if final_str not in final:
					final.append(final_str)	
			if two!=last and 1<len(two)<5 and 1<len(last)<5:
				b=[]
				b.append(two)
				b.append(last)
				final_str=''.join(b)
				if final_str not in final:
					final.append(final_str)	
			for f in final:
				if f not in word:
					word.setdefault(f,1)
		# elif sentence_arr and len(sentence_arr)==1:
		# 	print sentence_arr[0]
		else:
			# for s in sentence_arr:
			# 	print s
			# print ''.join(sentence_arr)
			word.setdefault(''.join(sentence_arr),1)
	for w,v in word_short.items():
		# print w
		if w not in word:
			word.setdefault(w,1)

	if 1 == 1:
		output = open('data.txt', 'w')
		for k,v in word.items():
			output.write('%s %s n\n'%(k.encode('utf8'),v))
		output.close( )
		idf={}
		word_str=''.join(word.keys())
		# print type(word_str),word_str
		for k,v in word.items():
			# print type(k),k
			if len(k) in [2,3,4]:
				# n=0
				k=re.sub(r'([\(\)\+\\])',r'\\\1',k)
				# print k
				gr=re.findall(u'(%s)'%k,word_str)
				# print gr
				n=len(gr)
				
				# for kk,vv in word.items():
				# 	if k in kk:
				# n+=1
				idf.setdefault(k,20.0 if n>20 else float(n))
			else:
				idf.setdefault(k,1.0)
		output = open('idf.txt', 'w')  
		for k,v in idf.items():
			output.write('%s %s\n'%(k.encode('utf8'),v))
		output.close()
			








	# 单元格
	# table.cell(rowx,colx)
	# cell_A1 = table.cell(0,0).value
	# cell_C4 = table.cell(3,2).value
	# 使用行列索引
	# cell_A1 = table.row(0)[0].value
	# cell_A2 = table.col(1)[0].value
		# print row_count,col_count
re_userdict = re.compile('^(.+?)( [0-9]+)?( [a-z]+)?$', re.U)
def read():
	f = open('D:/mywork/lib/jieba/userdict.txt', 'rb')
	word_dic={}
	for lineno, ln in enumerate(f, 1):
			line = ln.strip()
			# print type(line)
			if not isinstance(line, unicode):
				try:
					line = line.decode('utf-8').lstrip(u'\ufeff')
				except UnicodeDecodeError:
					raise ValueError('dictionary file %s must be utf-8' % f_name)
			if not line:
				continue
			word, freq, tag = re_userdict.match(line).groups()
			if freq is not None:
				freq = freq.strip()
			if tag is not None:
				tag = tag.strip()
			word_dic.setdefault(word,1)
	output = open('D:/repository/ik-analyzer/src/main/yueliang/org/wltea/analyzer/dic/main2012.dic', 'w')  
	for k,v in word_dic.items():
		print k
		output.write('%s\n'%(k.encode('utf8')))
	output.close()
def read_jieba_big():
	f = open('D:/projects/python_projects/pytest/src/excel/xlrd/dict.txt.big.txt', 'rb')
	word_dic={}
	for lineno, ln in enumerate(f, 1):
			line = ln.strip()
			# print type(line)
			if not isinstance(line, unicode):
				try:
					line = line.decode('utf-8').lstrip(u'\ufeff')
				except UnicodeDecodeError:
					raise ValueError('dictionary file %s must be utf-8' % f_name)
			if not line:
				continue
			word, freq, tag = re_userdict.match(line).groups()
			if freq is not None:
				freq = freq.strip()
			if tag is not None:
				tag = tag.strip()
			word_dic.setdefault(word,tag)
	return word_dic
def again_process():
	f = open('D:/projects/python_projects/pytest/src/excel/xlrd/data.txt', 'rb')
	word_dic={}
	big_word_dic=read_jieba_big()
	for lineno, ln in enumerate(f, 1):
		line = ln.strip()
		# print type(line)
		if not isinstance(line, unicode):
			try:
				line = line.decode('utf-8').lstrip(u'\ufeff')
			except UnicodeDecodeError:
				raise ValueError('dictionary file %s must be utf-8' % f_name)
		if not line:
			continue
		word, freq, tag = re_userdict.match(line).groups()
		if freq is not None:
			freq = freq.strip()
		if tag is not None:
			tag = tag.strip()
		if big_word_dic.get(word):
			print big_word_dic.get(word)
			tag=big_word_dic.get(word)
		word_dic.setdefault(word,tag)
	output = open('data_final.txt', 'w')  
	for k,v in word_dic.items():
		print k,type(k),v,type(v)
		output.write('%s 1 %s\n'%(k.encode('utf-8'),v.encode('utf-8')))
	output.close()
def read_diff_from_config():
	f = open('D:/mywork/lib/jieba/idf.txt', 'rb')
	word_dic={}
	for lineno, ln in enumerate(f, 1):
			line = ln.strip()
			# print type(line)
			if not isinstance(line, unicode):
				try:
					line = line.decode('utf-8').lstrip(u'\ufeff')
				except UnicodeDecodeError:
					raise ValueError('dictionary file %s must be utf-8' % f_name)
			if not line:
				continue
			word, freq, tag = re_userdict.match(line).groups()
			if freq is not None:
				freq = freq.strip()
			if tag is not None:
				tag = tag.strip()
			word_dic.setdefault(word,1)
	i=0
	output = open('D:/mywork/lib/jieba/idf.txt', 'a')  
	for k,v in one.items():
		s=re.split(u'[/、与]',v['name'].decode('utf-8'))
		for ss in s:
			if ss not in word_dic:
				if len(ss)<2:
					continue
				print ss
				output.write('%s 1.0\n'%(ss.encode('utf8')))
				i+=1
	# print 'q'*20
	for k,v in two.items():
		s=re.split(u'[/、与]',v['name'].decode('utf-8'))
		for ss in s:
			if len(ss)<2:
					continue
			if ss not in word_dic:
				print ss
				output.write('%s 1.0\n'%(ss.encode('utf8')))
				i+=1
	# print 'q'*20
	for k,v in three.items():
		s=re.split(u'[/、与]',v['name'].decode('utf-8'))
		for ss in s:
			if len(ss)<2:
					continue
			if ss not in word_dic:
				print ss
				output.write('%s 1.0\n'%(ss.encode('utf8')))
				i+=1
	print i
	output.close()

		
	# output = open('D:/repository/ik-analyzer/src/main/yueliang/org/wltea/analyzer/dic/main2012.dic', 'w')  
	# for k,v in word_dic.items():
	# 	print k
	# 	output.write('%s\n'%(k.encode('utf8')))
	# output.close()

if __name__ == '__main__':
	read()
	# process()
	# test()
	# again_process()
	# read_diff_from_config()