#-*- coding: utf8 -*-

import xlrd,re,logging,sys

log_console = logging.StreamHandler(sys.stderr)
default_logger = logging.getLogger(__name__)
default_logger.setLevel(logging.DEBUG)
default_logger.addHandler(log_console)




def read_ci(path,word):
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
		for c in xrange(0,ncols):
			col=table.cell(r,c).value
			link=table.hyperlink_map.get((r, c))
			# link=table.cell(r,c).Hyperlinks.Item(1).Address
			print col,link.url_or_path if link else None

def process():
	word={}

	read_ci('D:/mywork/tmall/tmall_618_blog.xls',word)



re_userdict = re.compile('^(.+?)( [0-9]+)?( [a-z]+)?$', re.U)
def read():
    f = open('D:/projects/python_projects/pytest/src/excel/xlrd/data.txt', 'rb')
    word_dic={}
    for lineno, ln in enumerate(f, 1):
            line = ln.strip()
            # print type(line)
            if not isinstance(line, unicode):
                try:
                    line = line.decode('utf-8').lstrip('\ufeff')
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
    output = open('ik_word.txt', 'w')
    for k,v in word_dic.items():
        output.write('%s\n'%(k.encode('utf8')))
    output.close()

if __name__ == '__main__':
    # read()
	process()
	# test()