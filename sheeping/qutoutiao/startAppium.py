# coding: utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from time import sleep
from appium import webdriver
import re
import time
import os
import sys
import math
import string
import json
import random
import threading
import urllib
import urllib.request 
from qutoutiao import Key_Codes
from qutoutiao import DriverSwipe
from qutoutiao import Utils
from qutoutiao import KeyBoards
from qutoutiao.BaseOperation import ExecutionParam
from qutoutiao.BaseOperation import BaseOperation
import traceback
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from multiprocessing import Pool

import threading
import time


if __name__ == '__main__':    

    readDeviceId = list(os.popen('adb devices').readlines())
    deviceIds=[]
    for outputline in readDeviceId:
        codes = re.findall(r'(^\w*)\t', outputline)
        if len(codes)!=0:
            deviceName=codes[0]
                   
#             versionoutput=list(os.popen('adb -s %s shell  getprop ro.build.version.release' % (deviceName)).readlines())
#             version = re.findall(r'(^.*)\n', versionoutput[0])[0]
#             devices.append((deviceName,version))
            deviceIds.append(deviceName)
    
    print('Parent process %s.' % os.getpid())    
    
    devices=[
             ExecutionParam(deviceName='A7QDU18420000828',version='9',port='4723',bootstrapPort='4724',username='18601793121', password='Initial0')
             ,
             ExecutionParam(deviceName='UEU4C16B16004079',version='9',port='4725',bootstrapPort='4726',username='17131688728', password='Initial0')
             ,
             ExecutionParam(deviceName='E4J4C17412001168',version='9',port='4727',bootstrapPort='4728',username='16536703898', password='Initial0')
             ,
             ExecutionParam(deviceName='3LGDU17328005108',version='9',port='4729',bootstrapPort='4730',username='17132126387', password='Initial0')
             ,
             ExecutionParam(deviceName='CXDDU16C07003822',version='9',port='4731',bootstrapPort='4732',username='15372499352', password='Initial0')
             ,
             ExecutionParam(deviceName='E4JDU17506004553',version='9',port='4733',bootstrapPort='4734',username='17132126385', password='Initial0')
             ,
             ExecutionParam(deviceName='SAL0217A28001753',version='9',port='4735',bootstrapPort='4736',username='15216706926', password='Initial0')            
             ]
        
    for device in devices[::-1]:
        if not device.deviceName in deviceIds:
            devices.remove(device)
    #close all appium exe
    os.system("start /b taskkill /F /t /IM node.exe")
    for device in devices:
        os.system("adb -s %s uninstall io.appium.settings" % device.deviceName)
        os.system("adb -s %s uninstall io.appium.uiautomator2.server.test" % device.deviceName)
        os.system("start /b appium -a 127.0.0.1 -p %s -bp %s --session-override --relaxed-security" % (device.port, device.bootstrapPort))
        time.sleep(10)        
                
    print('Waiting for all subprocesses done...')