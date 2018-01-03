# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time,random,socket,json
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuelianglib.common.utils import print_err,get_time_str
 
# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
# )

#--------------
headers = { 
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate, sdch',#有时间研究一下。好象不支持GZIP
    'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
}
# for key, value in headers.items():
#     DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value
# print DesiredCapabilities.PHANTOMJS
DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.userAgent"] = headers.get("User-Agent")
DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.resourceTimeout'] = 5000
DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.loadImages'] = False
DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.webSecurityEnabled"] = True
DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.javascriptCanOpenWindows"] = True
DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.javascriptCanCloseWindows"] = True
# DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.javascriptEnabled"] = False
DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.XSSAuditingEnabled"] = True
DesiredCapabilities.PHANTOMJS["takesScreenshot"] = False
dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
# 	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
# )
service_args = [#phantomjs -h查看参数
    '--debug=false',
    '--webdriver-loglevel=DEBUG',
    '--load-images=false',
    '--local-url-access=false',
    '--ignore-ssl-errors=true',
    ]
print dcap
# driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)
#--------
 
# driver = webdriver.PhantomJS( desired_capabilities=dcap)

# driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()
# driver.get("http://www.smzdm.com/gourl/DD714917912662A2/AA_YH_95")
# driver.get("http://go.smzdm.com/3dda1b125280206f/ca_aa_yh_75_6659867_159_0_0")
ua_list=[
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 ',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
]
sleep_time=[4,5,6,7,8,9,10]
# go_link='http://blog.sina.com.cn/s/blog_1389608980102wqwa.html'
# user=['1032027180','5244323992','5995025174','5796716770']
user=['1032027180','5244323992','5796716770']
# socket.setdefaulttimeout(50)
for i in range(1000):
    DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = random.choice(ua_list)
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)
    try:
        assoc_article = json.load(open('D:/mywork/tmall/assoc_user_%s.json'%random.choice(user), 'r'),strict=False)
        # assoc_article = json.load(open('D:/mywork/tmall/assoc_user_5244323992.json', 'r'),strict=False)
    except:
        assoc_article=None
    go_link='http://blog.sina.com.cn/s/blog_%s.html'%random.choice(assoc_article)
    # print go_link
    driver.get(go_link)
    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "comp_901_pv"))
        )
        # print element
        # print element.text
        time.sleep(2)
        # print i
        print element.text,get_time_str()
    except:
        pass
    finally:
        sleep_time=[1,2,3,4,5,6]
        time.sleep(random.choice(sleep_time))

        driver.quit()
        # now_handle = driver.current_window_handle #获取当前窗口句柄
        # print now_handle   #输出当前获取的窗口句柄
    
    
    # driver.quit()