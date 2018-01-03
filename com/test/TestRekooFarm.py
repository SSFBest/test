#-*- coding: utf-8 -*-
'''
Created on 2010-9-8

@author: Administrator
'''
def testpopularizeTask():
    popularizeTask={
   'test3':{
         "icon":{
            "image":"assets/images/yunying/laba4.swf",
            "tip":"毎日ログインプレゼントのお知らせ"
        },
        "window":{
            "clazz":"feedYellowWindow",
            "title":"毎日ログインプレゼントのお知らせ",
            "content":"<font color='#FF0000'>トライアル肥料、飼料</font>は毎日ログインするだけでもらえます！<br /><br /><b>【キャンペーン期間】</b><br />　開始時間：　8月9日～<br />　終了時間：　改めてお知らせいたします。<br />　ご&nbsp;注&nbsp;意&nbsp;：　月曜日の受け取り時間は12時から24時の間と</br>　　　　  　　　　　させていただきます、ご了承ください。<br /><br /><b>【キャンペーン内容】</b><br /><font color='#FF0000'><b>毎日</b>、一回だけログインする</font>と以下のアイテムがもらえます。<br />　・トライアル肥料　×　5個　　　　※土日は　10　個<br />　・トライアル飼料　×　5個　　　　※土日は　10　個<br /><br /><font color='#FF0000'><b>さらに</b>、月曜日から日曜日まで毎日ログインしていただく</font>と、<br/>日曜日にて以下のアイテムがもらえます！<br />　・トライアル肥料　×　20個<br />　・トライアル飼料　×　20個",
            "image":"assets/images/yunying/laba4.swf",
            "color":"0xFF6600",
            "width":"400",
            "height":"480"
        },
        "close":{
            "clazz":"feedYellowClose"
        },
        "submit":{
            "clazz":"buttonYellow"
        }
    },
}
    popularizeTask = [popularizeTask[item] for item in popularizeTask]
    print popularizeTask

if __name__ == '__main__':
    testpopularizeTask()