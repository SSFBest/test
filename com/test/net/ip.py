import re,urllib2
class Getmyip:
    def getip(self):
        try:
            myip = self.visit("http://1212.ip138.com/ic.asp")
        except:
            try:
                myip = self.visit("http://www.bliao.com/ip.phtml")
            except:
                try:
                    myip = self.visit("http://www.whereismyip.com/")
                except:
                    myip = "So sorry!!!"
        return myip
    def visit(self,url):
        opener = urllib2.urlopen(url)
        if url == opener.geturl():
            str = opener.read()
            print str
        return re.search('d+.d+.d+.d+',str).group(0)
getmyip = Getmyip()
localip = getmyip.getip()
print localip