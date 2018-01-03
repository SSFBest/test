#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import Image
from PIL import Image
import os

def make_thumb(path, sizes=(75, 32, 16,750,1100)):
    """
    缩略图生成程序 by Neil Chen
    sizes 参数传递要生成的尺寸，可以生成多种尺寸
    """    
    base, ext = os.path.splitext(path)
    try:
        im = Image.open(path)
    except IOError:
        return
    mode = im.mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            # 透明图片需要加白色底
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255-x)
            im = im.convert('RGB')
            # paste(color, box, mask)
            im.paste((255,255,255), None, bgmask)
        else:
            im = im.convert('RGB')
            
    width, height = im.size
    if width == height:
        region = im
    else:
        if width > height:
            delta = (width - height)/2
            box = (delta, 0, delta+height, height)
        else:
            delta = (height - width)/2
            box = (0, delta, width, delta+width)            
        region = im.crop(box)
            
    for size in sizes:
        filename = base + "_" + "%sx%s" % (str(size), str(size)) + ".jpg"
        thumb = region.resize((size,size), Image.ANTIALIAS)
        thumb.save(filename, quality=100) # 默认 JPEG 保存质量是 75, 不太清楚。可选值(0~100)
def make_thumb2(path):
    base, ext = os.path.splitext(path)
    im = Image.open(path)
    size = im.size
    if size[0] > size[1]:
        rate = float(120) / float(size[0])
    else:
        rate = float(90) / float(size[1])
    new_size = (int(size[0] * rate), int(size[1] * rate))
    new = im.resize(new_size, Image.BILINEAR)
    filename = base + "_new" + ".jpg"
    new.save(filename)
def make_thumb3(path, sizes=(149, 149)):
    """
    缩略图生成程序 by Neil Chen
    sizes 参数传递要生成的尺寸，可以生成多种尺寸
    """    
    base, ext = os.path.splitext(path)
    print base,ext
    try:
        im = Image.open(path)
    except IOError, e:
        print e
        return
    mode = im.mode
    print mode
    if mode not in ('L', 'RGB'):
        if mode == 'RGBA':
            # 透明图片需要加白色底
            alpha = im.split()[3]
            bgmask = alpha.point(lambda x: 255-x)
            im = im.convert('RGB')
            # paste(color, box, mask)
            # im.paste((255,255,255), None, bgmask)
            print 'x'
        else:
            im = im.convert('RGB')
            print 'y'
            
    width, height = im.size
    if width == height:
        delta=(float(height)-(height*float(sizes[1])/float(sizes[0])))/2
        box = (0, int(delta), width, int(delta+height*float(sizes[1])/float(sizes[0])))
        print 1,box
    else:
        if float(width) > float(height)*float(sizes[0])/float(sizes[1]):
            delta = (width - height*float(sizes[0])/float(sizes[1]))/2

            print 'delta',delta
            box = (int(delta), 0, int(delta+height*float(sizes[0])/float(sizes[1])), height)
            print 2, box
        else:
            delta = (height - width*float(sizes[1])/float(sizes[0]))/2
            print 'delta',delta
            box = (0, int(delta), width, int(delta+width*float(sizes[1])/float(sizes[0])))     
            print 3,box       
    region = im.crop(box)
            
    filename = base + "_" + "%sx%s" % (str(sizes[0]), str(sizes[1])) + ".jpg"
    thumb = region.resize((sizes[0],sizes[1]), Image.ANTIALIAS)
    thumb.save(filename, quality=100) # 默认 JPEG 保存质量是 75, 不太清楚。可选值(0~100)

if __name__ == '__main__':    
    # make_thumb(r"D:/projects/python_projects/yueliang_pc/static/images/ad2.jpg")
    # make_thumb2(r"D:/projects/python_projects/yueliang_pc/static/images/ad2.jpg")
    # make_thumb3(r"http://zxpic.gtimg.com/infonew/0/sports_pics_109862036.jpg/800")
    make_thumb3(r"d:/test/test.jpg",sizes=(350*4,340*4))