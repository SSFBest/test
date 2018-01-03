#-*- coding: utf-8 -*-
import re,json

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
def test_with():
    try:
        with open('D:/mywork/spider/yueliang/data.json','w') as f:
            print 'aa'
            f.write('[5]')
            return 4
    except IOError,e:
        print 'bb'
    finally:
        print 66
def test_with2():
    import os,json
    jsonpath= 'D:/mywork/spider/yueliang/fenlei_data.json' 
    dirname = os.path.dirname(jsonpath)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname)
    # try:
    with open(jsonpath,'w+') as f:
        datajson = json.load(f)
        if not datajson:
            datajson={}
            # done=datajson.get('done') if datajson.get('done') else []
            # if item['pid'] in done:
            #     return
            # todo=datajson.get('todo') if datajson.get('todo') else []
            # todo.append((item['pid'],item['cid']))
            # datajson.update(todo=todo)

            
    # except IOError,e:
    #     datajson=None
        # print '3'

if __name__ == '__main__':
    # read()
    # print test_with()
    test_with2()