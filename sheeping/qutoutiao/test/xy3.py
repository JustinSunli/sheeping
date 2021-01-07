# coding: utf-8
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

def get_tracks(distance):
    """
    拿到移动轨迹，模仿人的滑动行为，先匀加速后均减速
    匀变速运动基本公式：
    ①：v=v0+at
    ②：s=v0t+½at²
    ③：v²-v0²=2as
    :param distance:需要移动的距离
    :return:存放每0.3秒移动的距离
    """
    distance += 20  # 先滑过一点，最后再反着滑动回来
    # 初速度
    v = 0
    # 单位时间为0.3s来统计轨迹，轨迹即0.3s内的位移
    t = 0.3
    # 位移/轨迹列表，列表内的一个元素代表0.3s的位移
    forward_tracks = []
    # 当前位移
    current = 0
    # 到达mid值开始减速
    mid = distance * 4 / 5
    while current < distance:
        if current < mid:
            # 加速度越小，单位时间的位移越小，模拟的轨迹就越多越详细
            a = 2
        else:
            a = -3
        # 初速度
        v0 = v
        # 0.3秒时间内的位移
        s = v0 * t + 0.5 * a * (t ** 2)
        # 当前的位置
        current += s
        # 添加到轨迹列表,round()为保留一位小数且该小数要进行四舍五入
        forward_tracks.append(round(s))
        # 速度已经达到v，该速度作为下次的初速度
        v = v0 + a * t

    # 反着滑动到准确位置
    back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]  # 总共等于-20
    return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks} 
      
def get_distance(image):
    """
    �õ�������֤����Ҫ�ƶ��ľ���
    :param image1: û��ȱ�ڵ�ͼƬ����
    :param image2: ��ȱ�ڵ�ͼƬ����
    :return: ��Ҫ�ƶ��ľ���
    """
    #490 520
    rankFirstHalfFrom = 0.198
    rankFirstHalfTo = 0.378
    
    rankSecondHalfFrom = 0.667
    rankSecondHalfTo = 0.847
    
#     top = 453
#     bottom = 630
#     left=72
#     right =249
    top = 432
    bottom = 621
    left=72
    right =249
        
    thresholdRange = 10
    
    fromFirstHalfX =math.floor(top+ (bottom - top)* rankFirstHalfFrom)
    toFirstHalfX   =math.floor(top+ (bottom - top)* rankFirstHalfTo)
    fromSecondHalfX =math.floor(top+ (bottom - top)* rankSecondHalfFrom)
    toSecondHalfX   =math.floor(top+ (bottom - top)* rankSecondHalfTo)
    
    i = 0
    #����ÿ�е����ص����Ȳ���

    previousArr=[]
    currentArr=[]
    positionRate=[]
    initialImageMatrix=image.load()
    ColumnSize = toFirstHalfX-fromFirstHalfX + toSecondHalfX-fromSecondHalfX
    #skip the first mix-picture area
    startPosition = right+2*thresholdRange
    for i in range(startPosition, image.size[0]):
        if len(currentArr)==(ColumnSize*thresholdRange):
            del currentArr[0:ColumnSize]
        if len(previousArr)==(ColumnSize*thresholdRange):
            del previousArr[0:ColumnSize]
                       
        for j in range(fromFirstHalfX, toFirstHalfX):
            rgb = initialImageMatrix[i, j]
            r,g,b = rgb[0],rgb[1],rgb[2]
            brightness = get_pixel_brightness(r,g,b)
            currentArr.append(brightness)    

        for j in range(fromSecondHalfX, toSecondHalfX):
            rgb = initialImageMatrix[i, j]
            r,g,b = rgb[0],rgb[1],rgb[2]
            brightness = get_pixel_brightness(r,g,b)
            currentArr.append(brightness) 
            
        if i-thresholdRange >= startPosition:
#                 rgb = initialImageMatrix[i-10, j]
#                 r,g,b = rgb[0],rgb[1],rgb[2]
#                 brightness = get_pixel_brightness(r,g,b)                
#                 previousArr.append(brightness)
            previousArr.extend(currentArr[0:ColumnSize])
        if len(previousArr)==len(currentArr) and len(currentArr)==thresholdRange*ColumnSize:
            rate = sum(currentArr) / sum(previousArr)
            positionRate.append((i,rate))
            
    positionRate.sort(key=lambda x:x[1])
    return positionRate[0][0] - right - thresholdRange
    
if __name__ == "__main__":
    #
    dst_src=r'C:\Users\wl\Desktop\20191028100842.jpg'
    #dst_src=r'C:\Users\wl\Desktop\20191026130323.jpg'
    image = Image.open(dst_src)
    distance=get_distance(image)
    get_tracks(distance)
    print