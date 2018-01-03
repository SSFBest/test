#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import Image
from yuelianglib.common.image import Graphics

if __name__ == '__main__':    
    # make_thumb(r"D:/projects/python_projects/yueliang_pc/static/images/ad2.jpg")
    # make_thumb2(r"D:/projects/python_projects/yueliang_pc/static/images/ad2.jpg")
    # make_thumb3(r"http://zxpic.gtimg.com/infonew/0/sports_pics_109862036.jpg/800")
    # make_thumb3(r"d:/test/test.jpg",sizes=(350*4,340*4))
    g=Graphics(None,'C:/Users/LENOVO/Pictures/test/','tt',local_img='C:/Users/LENOVO/Pictures/test/newpic.png')
    g.run_cut(90,(200,200))