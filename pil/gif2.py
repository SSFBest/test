#-*- coding: utf8 -*-

import PIL
from PIL import ImageGrab # from PIL  
import time  
import string  
from PIL import Image, ImageChops  
from PIL import GifImagePlugin
from PIL.GifImagePlugin import getheader, getdata,_get_used_palette_colors
import os  
  
def intToBin(i):
    """ Integer to two bytes """
    # devide in two parts (bytes)
    i1 = i % 256
    i2 = int( i/256)
    # make string (little endian)
    return chr(i1) + chr(i2)


def getheaderAnim(im):
    """ Animation header. To replace the getheader()[0] """
    bb = "GIF89a"
    bb += intToBin(im.size[0])
    bb += intToBin(im.size[1])
    bb += "\x87\x00\x00"
    return bb


def getImageDescriptor(im):
    """ Used for the local color table properties per image.
    Otherwise global color table applies to all frames irrespective of
    wether additional colours comes in play that require a redefined palette
    Still a maximum of 256 color per frame, obviously.
    
    Written by Ant1 on 2010-08-22
    """
    bb = '\x2C' # Image separator,
    bb += intToBin( 0 ) # Left position
    bb += intToBin( 0 ) # Top position
    bb += intToBin( im.size[0] ) # image width
    bb += intToBin( im.size[1] ) # image height
    bb += '\x87' # packed field : local color table flag1, interlace0, sorted table0, reserved00, lct size111=7=2^(7+1)=256.
    # LZW minimum size code now comes later, begining of [image data] blocks
    return bb


def getAppExt(loops=float('inf')):
    """ Application extention. Part that specifies amount of loops. 
    If loops is inf, it goes on infinitely.
    """
    if loops == 0:
        bb = "" # application extension should not be used
                # (the extension interprets zero loops
                # to mean an infinite number of loops)
    else:
        bb = "\x21\xFF\x0B"  # application extension
        bb += "NETSCAPE2.0"
        bb += "\x03\x01"
        if loops == float('inf'):
            loops = 2**16-1
        bb += intToBin(loops)
        bb += '\x00'  # end
    return bb


def getGraphicsControlExt(duration=0.1):
    """ Graphics Control Extension. A sort of header at the start of
    each image. Specifies transparancy and duration. """
    bb = '\x21\xF9\x04'
    bb += '\x08'  # no transparancy
    bb += intToBin( int(duration*100) ) # in 100th of seconds
    bb += '\x00'  # no transparant color
    bb += '\x00'  # end
    return bb
  
  
  
def _writeGifToFile(fp, images, durations, loops):
    frames = 0

    previous = None

    for im in images:

        #
        # FIXME: write graphics control block before each frame

        if not previous:

            # global header
            for s in getheader(im)[0] + getdata(im):
                fp.write(s)

        else:

            # delta frame
            delta = ImageChops.subtract_modulo(im, previous)

            bbox = delta.getbbox()

            if bbox:

                # compress difference
                for s in getdata(im.crop(bbox), offset = bbox[:2]):
                    fp.write(s)

            else:
                # FIXME: what should we do in this case?
                pass

        previous = im.copy()

        frames = frames + 1

    fp.write(";")

    return frames
  
## Exposed functions 

def writeGif(filename, images, duration=0.1, loops=0, dither=1):
    """ writeGif(filename, images, duration=0.1, loops=0, dither=1)
    Write an animated gif from the specified images. 
    images should be a list of numpy arrays of PIL images.
    Numpy images of type float should have pixels between 0 and 1.
    Numpy images of other types are expected to have values between 0 and 255.
    """
    
    if PIL is None:
        raise RuntimeError("Need PIL to write animated gif files.")
    
    AD = Image.ADAPTIVE
    images2 = []
    
    # convert to PIL
    for im in images:
        
        if isinstance(im,Image.Image):
            # print im.mode
            images2.append( im.convert('P', palette=AD, dither=dither) )
            # images2.append( im )
            print 'ddd'
            print im.mode
            
        elif np and isinstance(im, np.ndarray):
            if im.dtype == np.uint8:
                pass
            elif im.dtype in [np.float32, np.float64]:
                im = (im*255).astype(np.uint8)
            else:
                im = im.astype(np.uint8)
            # convert
            if len(im.shape)==3 and im.shape[2]==3:
                im = Image.fromarray(im,'RGB').convert('P', palette=AD, dither=dither)
            elif len(im.shape)==2:
                im = Image.fromarray(im,'L').convert('P', palette=AD, dither=dither)
            else:
                raise ValueError("Array has invalid shape to be an image.")
            images2.append(im)
            
        else:
            raise ValueError("Unknown image type.")
    
    # check duration
    if hasattr(duration, '__len__'):
        if len(duration) == len(images2):
            durations = [d for d in duration]
        else:
            raise ValueError("len(duration) doesn't match amount of images.")
    else:
        durations = [duration for im in images2]
        
    
    # open file
    fp = open(filename, 'wb')
    
    # write
    try:
        n = _writeGifToFile(fp, images2, durations, loops)
        print n, 'frames written'
    finally:
        fp.close()
  
############################################################  
## 将多帧位图合成为一幅gif图像  
def images2gif( images, giffile, durations=0.05, loops = 1):  
    seq = []  
    for i in range(len(images)):  
        im = Image.open(images[i])  
        # print im.mode
        # im = im.convert('RGB').convert('P', palette=Image.ADAPTIVE)
        seq.append(im)  
    frames = writeGif( giffile, seq, durations, loops)  
    print frames, 'images has been merged to', giffile  
  
## 将gif图像每一帧拆成独立的位图   
def gif2images( filename, distDir = '.', type = 'bmp' ):  
    if not os.path.exists(distDir):  
        os.mkdir(distDir)  
    print 'spliting', filename,  
    im  = Image.open( filename )  
    im.seek(0)  # skip to the second frame  
    cnt = 0  
    type = string.lower(type)  
    mode = 'RGB'  # image modea  
    if type == 'bmp' or type == 'png':  
        mode = 'P'    # image mode   
    im.convert(mode).save(distDir+'/%d.'%cnt+type )  
    cnt = cnt+1  
    try:  
        while 1:  
            im.seek(im.tell()+1)  
            im.convert(mode).save(distDir+'/%d.'%cnt+type)  
            cnt = cnt+1  
    except EOFError:  
        pass # end of sequence  
    white = (255,255,255)  
    preIm = Image.open(distDir+'/%d.'%0+type).convert('RGB')  
    size = preIm.size  
    prePixs = preIm.load()  
    for k in range (1,cnt):  
        print '.',  
        im = Image.open(distDir+'/%d.'%k+type).convert('RGB')  
        pixs = im.load()  
        for i in range(size[0]):  
            for j in range(size[1]):  
                if pixs[i,j] == white:  
                    pixs[i,j] = prePixs[i,j]  
        preIm = im  
        prePixs = preIm.load()  
        im.convert(mode,palette=Image.ADAPTIVE).save(distDir+'/%d.'%k+type)  
    print '\n', filename, 'has been splited to directory: [',distDir,']'  
    return cnt      # 总帧数  
  
##############################################################  
if __name__ == '__main__':  
    frames = gif2images('test_gif.gif',distDir='tmp',type='png')  
    images = []  
    for i in range(frames-1,-1,-1):  
        images.append('tmp/%d.png'%i)  
    # images=['tmp/None_danger.png','tmp/15yueliang_info.png','tmp/None_primary.png']
    images2gif(images,'save.gif', durations = 0.5)  