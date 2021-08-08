# coding: utf-8
#import os
#import sys
#rootpath=str("D://git//sheeping//sheeping")
#syspath=sys.path
#sys.path=[]
#sys.path.append(rootpath)
##将工程根目录加入到python搜索路径中
#sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])
#sys.path.extend(syspath)



#adb connect连接设备很慢，需要用以下命令

#adb usb
#adb tcpip 5555
#adb connect 192.168.0.106:5555
#adb disconnect 192.168.0.106:5555