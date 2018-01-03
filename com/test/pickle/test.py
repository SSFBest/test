import cPickle as pickle
def test():
	a=[1,2,3]
	b=pickle.dumps(a)
	c=pickle.loads(str(b))
	print a
	d=[]
	e=pickle.dumps(d)
	print e,len(e)
	f=pickle.loads(e)
	print f

if __name__ == '__main__':
	test()