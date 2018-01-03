#-*- coding: utf-8 -*-
from PIL import Image,ImageFile,ImageEnhance, ImageDraw, ImageFont



def img_mark(path):
    im = Image.open(path)
    return im

def text2img(text, font_color="RED", font_size=25):
    """生成内容为 TEXT 的水印"""

    font = ImageFont.truetype('MFLiHei_Noncommercial-Regular.otf', font_size)
    #多行文字处理
    text = text.split('\n')
    mark_width = 0
    for  i in range(len(text)):
        (width, height) = font.getsize(text[i])
        if mark_width < width:
            mark_width = width
    mark_height = height * len(text)

    #生成水印图片
    mark = Image.new('RGBA', (mark_width,mark_height))
    draw = ImageDraw.ImageDraw(mark, "RGBA")
    draw.setfont(font)
    for i in range(len(text)):
        (width, height) = font.getsize(text[i])
        draw.text((0, i*height), text[i], fill=font_color)
    return mark

def set_opacity(im, opacity):
    """设置透明度"""

    assert opacity >=0 and opacity < 1
    print im.mode
    if im.mode != "RGBA":
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im
def watermark(im, mark, position):
    """添加水印"""

    try:
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        if im.size[0] < mark.size[0] or im.size[1] < mark.size[1]:
            print "The mark image size is larger size than original image file."
            return False

        #设置水印位置
        layer = Image.new('RGBA', im.size, (0,0,0,0))
        if position == 'tile':
            for y in range(0, im.size[1], mark.size[1]):
                for x in range(0, im.size[0], mark.size[0]):
                    layer.paste(mark, (x, y))
        elif position == 'scale':
         # scale, but preserve the aspect ratio
            ratio = min(
                float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
            w = int(mark.size[0] * ratio)
            h = int(mark.size[1] * ratio)
            mark = mark.resize((w, h))
            layer.paste(mark, ((im.size[0] - w) / 2, (im.size[1] - h) / 2))
        elif position == 'left_top':
            x = 0
            y = 0
            layer.paste(mark,(x,y))
        elif position == 'left_bottom':
            x = 0
            y = im.size[1] - mark.size[1]
            layer.paste(mark,(x,y))
        elif position == 'right_top':
            x = im.size[0] - mark.size[0]
            y = 0
            layer.paste(mark,(x,y))
        elif position == 'right_bottom':
            x = im.size[0] - mark.size[0]
            y = im.size[1] - mark.size[1]
            layer.paste(mark,(x,y))
        else:
            x = (im.size[0] - mark.size[0]) / 2
            y = (im.size[1] - mark.size[1]) / 2
            layer.paste(mark,(x,y))

        
        return Image.composite(layer, im, layer)
    except Exception as e:
        print ">>>>>>>>>>> WaterMark EXCEPTION:  " + str(e)
        return False

def main():
    img_watermark=set_opacity(img_mark('D:/test/youxi1(121x65).png'),0.3)
    img_watermark.save('D:/test/youxi1(121x65).jpg')
    text_watermark=set_opacity(text2img(u'游戏十六\nyouxi16.com'),0.9)
    postion='right_bottom'
    im = Image.open('D:/test/water.jpg')
    image = watermark(im, text_watermark, postion)
    if image:
        image.save('d:/test/water2.jpg')
        image.show()
    else:
        print "Sorry, Failed."


if __name__ == '__main__':
    main()