'''
Created on 2010-9-14

@author: Administrator
'''
import urllib

def test_conn():
    pagehandler = urllib.urlopen("http://staging.igaworks.com/AdPOPcorn/Media/MediaService.svc/GetPopicon?mc=1&usn=kim&gusn=1&age=30&birthdate=19810123&gender=Male&ip=121.1.1.1&country=kr")
    data = pagehandler.read()
    print data
    pagehandler.close()
if __name__ == '__main__':
    test_conn()