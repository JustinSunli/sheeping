# -*- coding: utf-8 -*-

import math
from PIL import Image, ImageStat


def get_image_light_mean(dst_src=r'C:\Users\wl\Desktop\΢��ͼƬ_20191026130323.jpg'):
    im = Image.open(dst_src).convert('L')
    stat = ImageStat.Stat(im)
    return stat.mean[0]

def get_image_light_rms_sqrt(dst_src=r'C:\Users\wl\Desktop\΢��ͼƬ_20191026130323.jpg'):
    im = Image.open(dst_src)
    stat = ImageStat.Stat(im)
    r, g, b = stat.rms
    return math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))

def brightness( im_file=r'C:\Users\wl\Desktop\΢��ͼƬ_20191026130323.jpg' ):
   im = Image.open(im_file)
   stat = ImageStat.Stat(im)
   return [math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2)) for r,g,b in im.load()]
   
def get_pixel_brightness(r,g,b):
    return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
       
def get_distance(image):
    """
    �õ�������֤����Ҫ�ƶ��ľ���
    :param image1: û��ȱ�ڵ�ͼƬ����
    :param image2: ��ȱ�ڵ�ͼƬ����
    :return: ��Ҫ�ƶ��ľ���
    """
    #490 520
    rankFrom = 0.27
    rankTo = 0.35
    
    top = 453
    bottom = 630
    left=72
    right =249
    
    threshold = 0.6
    
    fromX =math.floor(top+ (bottom - top)* rankFrom)
    toX   =math.floor(top+ (bottom - top)* rankTo)
    
    i = 0
    #����ÿ�е����ص����Ȳ���

    previousArr=[]
    currentArr=[]
    previous=0
    current=0    
    for i in range(right, image.size[1]):
        if len(currentArr)==((toX-fromX)*10):
            del currentArr[0:(toX-fromX)]
           
        for j in range(fromX, toX):
            rgb = image.load()[i, j]
            r,g,b = rgb[0],rgb[1],rgb[2]
            brightness = get_pixel_brightness(r,g,b)
            currentArr.append(brightness)
            
        if len(previousArr)!=len(currentArr) and len(currentArr)==10*(toX-fromX):
            current = sum(previousArr)/sum(currentArr)
            if previous!=0:
                if current / previous < threshold:
                    return i - right
                
            
            previous = current
                
#                 if abs(sum(previousArr) - sum(currentArr)) > self.threshold:
#                     return i - self.left
        previousArr=[]
        previousArr.extend(currentArr)
        
    print('δʶ�����֤���еĲ�ͬλ�ã���ͼƬ��λ�����쳣')
    return i  # ���û��ʶ�����ͬλ�ã��������ԵĻ�������ˢ����һ����֤��
    
if __name__ == "__main__":
    #
    dst_src=r'C:\Users\wl\Desktop\微信图片_20191026130323.jpg'
    image = Image.open(dst_src)
    get_distance(image)
    print