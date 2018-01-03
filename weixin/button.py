# -*- coding: utf-8 -*-
# filename: menu.py
import urllib
# from basic import Basic

class Menu(object):
    def __init__(self):
        pass
    def create(self, postData, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
        if isinstance(postData, unicode):
            postData = postData.encode('utf-8')
        urlResp = urllib.urlopen(url=postUrl, data=postData)
        print urlResp.read()

    def query(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    def delete(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

    #获取自定义菜单配置接口
    def get_current_selfmenu_info(self, accessToken):
        postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
        urlResp = urllib.urlopen(url=postUrl)
        print urlResp.read()

if __name__ == '__main__':
    myMenu = Menu()
    postJson = """
    {
        "button":
        [

            {
                "name": "大家最爱",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "品牌特卖",
                        "url": "http://m.tduoduo.com/temai"
                    },
                    {
                        "type": "view",
                        "name": "限时抢购",
                        "url": "http://m.tduoduo.com/qianggou"
                    },
                    {
                        "type": "view",
                        "name": "电商导航",
                        "url": "http://m.tduoduo.com/mall"
                    }
                ]
            },
            {
                "name": "精选",
                "sub_button":
                [
                    {
                        "type": "view",
                        "name": "精选活动",
                        "url": "http://m.tduoduo.com/mall/act"
                    },
                    {
                        "type": "view",
                        "name": "商品精选",
                        "url": "http://m.tduoduo.com/tao/guonei"
                    },
                    {
                        "type": "view",
                        "name": "优惠券",
                        "url": "http://m.tduoduo.com/quan"
                    }
                ]
            },
            {
                "type": "click",
                "name": "帮助说明",
                "key":  "help"
            },
          ]
    }
    """
    # accessToken = Basic().get_access_token()
    #myMenu.delete(accessToken)
    accessToken='Gtw3g1ttLYcfqw9D0YIJ2QF4B6tyBaCG2dfn4rp9WuEC0MLQDRTWh_Swyabxf2pLGdRk4HmpjCDKtpg9lcue8IP55VydZdOEdXnQN6mZ1HYVVReAAAMMI'
    myMenu.create(postJson, accessToken)
