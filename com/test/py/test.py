def test(a):
	if a==5:
		a=6
	else:
		a=7
	return None
if __name__ == '__main__':
	
	item={
		'r':5
	}
	print test(item['r'])
	print item['r']