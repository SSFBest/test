# -*- coding: utf-8 -*-

from datetime import datetime
from md5 import md5
import hashlib,re,simplejson

from yuelianglib.common.httprequest import http

from yuelianglib.common.utils import print_err,get_err

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
}
def process_item():
  try:
    cookie='OZ_1U_2061=vid=v84a8a99a17f61.0&ctime=1481280351&ltime=1481280207; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; mbk=5dd5b762527e7c53; _tb_token_=ee737183193e6; ck1=; uc1=cookie14=UoW%2BuvgMtNhjKA%3D%3D&lng=zh_CN&cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&existShop=false&cookie21=URm48syIYn73&tag=3&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0; uc3=sg2=Wqbxb6LyHC3oJzu6qXhfKTl7%2FAp31ETbn2A2Kj%2FuE90%3D&nk2=F5NO4MKvNg%3D%3D&id2=UNGQXF%2FfFY8%3D&vt3=F8dARVK2A0Q653XIlwM%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D; lgc=teemimi; tracknick=teemimi; cookie2=1c98dde86727cf811a84e96da0b57801; cookie1=UNICLQDxGeiUdu2e8mzQbAdAJ72nNq7WNSx7YehUHhE%3D; unb=31634811; t=c1a07a395b20ebf0a0e52a6d601ffb71; skt=a7ef272f517551b6; _nk_=teemimi; _l_g_=Ug%3D%3D; cookie17=UNGQXF%2FfFY8%3D; hng=; uss=B0E3dfs1Nf2o7S9bOHn9v86329LgubJG5ximIyCeMFRZ%2Bv0IqJTrCxIsuZc%3D; login=true; cna=EbDKEIIrPBcCAXhVUl24UDEN; isg=AiQkkA1jIGPJ81R1qn75z7u09SIjs1NNPRl-0T5Fj--y6cazZs0Yt1of3_aL; l=AuHh2Murc/6E3948EdyV7MR4caf7sVWA'
    headers.update(Referer='https://detail.tmall.com/item.htm?id=522189908497')
    headers.update(cookie=cookie)
    resp=http('GET','https://bar.tmall.com/cueAssetMsg.htm?sellerId=515369883&itemId=522189908497&callback=jsonp692&_input_charset=UTF-8',headers)
    # resp,num=re.subn(r'(process_comment\()({.*})(\));',r'\1%s\2%s\3'%('\'','\''),resp)
    print resp
    
  except Exception as e:
    print_err()


if __name__ == '__main__':
  process_item()