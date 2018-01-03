import traceback
from yuelianglib.common.error.exceptions import NotJdThreeConfig
try:  
    # 1/0  
    raise
except ZeroDivisionError,e:  
    print traceback.format_exc()
    # traceback.print_exc()
except Exception,e:
	print traceback.format_exc()	

def a():
	raise NotJdThreeConfig
def b():
	raise NotJdThreeConfig()
if __name__ == '__main__':
	try:
		a()	
	except NotJdThreeConfig,e:
		print 'ddd'
	try:
		b()	
	except ZeroDivisionError,e:
		print 'bbb'