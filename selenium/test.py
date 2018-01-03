# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
 
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
# DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.resourceTimeout'] = 5000
DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.loadImages'] = True
# DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.webSecurityEnabled"] = True
# DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.javascriptCanOpenWindows"] = True
# DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.javascriptCanCloseWindows"] = True
# DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.javascriptEnabled"] = True
# DesiredCapabilities.PHANTOMJS["phantomjs.page.settings.XSSAuditingEnabled"] = True
# DesiredCapabilities.PHANTOMJS["takesScreenshot"] = False
dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
# 	"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
# )
service_args = [#phantomjs -h查看参数
    '--debug=false',
    '--webdriver-loglevel=DEBUG',
    '--load-images=true',
    '--local-url-access=false',
    '--ignore-ssl-errors=true',
    ]
print dcap
driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=service_args)
#--------
 
# driver = webdriver.PhantomJS( desired_capabilities=dcap)

# driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()
# driver.get("http://www.smzdm.com/gourl/DD714917912662A2/AA_YH_95")
driver.get("http://go.smzdm.com/3dda1b125280206f/ca_aa_yh_75_6659867_159_0_0")
# driver.get("http://s.click.taobao.com/t?e=m%3D2%26s%3D%2BcJyNyH2ZxAcQipKwQzePOeEDrYVVa64K7Vc7tFgwiFRAdhuF14FMa%2B9fIVmPbYNJ1gyddu7kN%2FGxx3oxEROVsiG%2B3kNBU6dsSABaZwf8HSVbDBXX%2FLDVE2srC8Mk09eWUzjwUEDHCkJtywMAn1xiQgeJNyHp0J1LqumWsRRT48OeWxEamLZB9PZ4DpQRxeqcSpj5qSCmbA%3D")
print driver.title.encode('utf-8')
print driver.current_url
now_handle = driver.current_window_handle #获取当前窗口句柄
print now_handle   #输出当前获取的窗口句柄
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# print driver.page_source.encode('utf-8')
# driver.implicitly_wait(3)
time.sleep(4)
print '000'
for handle in driver.window_handles:
	driver.switch_to_window(handle)
	print '444'
	print driver.current_url
	print driver.title
# String currentWindow = driver.getWindowHandle()
# Set<String> handles = driver.getWindowHandles();//获取所有窗口句柄
# Iterator<String> it = handles.iterator();
# while (it.hasNext()) {
# if (currentWindow == it.next()) {
# continue;
# }
# WebDriver window = driver.switchTo().window(it.next());//切换到新窗口
# System.out.println(“New page title is:” + window.getTitle());
# window.close();//关闭新窗口
# }
# driver.switchTo().window(currentWindow);//回到原来页面
# assert "No results found." not in driver.page_source

driver.get("http://1212.ip138.com/ic.asp")
print dir(driver)

print driver.page_source
element=driver.find_element_by_id('myagent')
print dir(element)
print element.text
driver.close()
print 'end'