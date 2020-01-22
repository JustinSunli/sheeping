# coding: utf-8
from multiprocessing import Pool
from time import sleep
from appium import webdriver
import re
import time
import os
import sys
import random
import threading
import traceback
import numpy as np
from qutoutiao import DriverSwipe, wechatautomation
from qutoutiao.qutoutiaoautomation import QutoutiaoAutomation 
from qutoutiao.qujianpanautomation import QujianpanAutomation
from qutoutiao.shuabaoautomation import ShuabaoAutomation
from qutoutiao.kuaishouautomation import KuaiShouAutomation
from qutoutiao.wechatautomation import WeChatAutomation
from qutoutiao.kuaikandianautomation import KuaiKanDianAutomation
from qutoutiao.miduautomation import MiduAutomation
from qutoutiao.huoshanautomation import HuoShanAutomation
from qutoutiao.xiangkanautomation import XiangKanAutomation

from qutoutiao.quanminautomation import QuanMinAutomation
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from qutoutiao.baseoperation import BaseOperation
        
def SheepingDevices(device):
    (deviceName,version) = device
    print('Run task %s (%s)...' % (deviceName, os.getpid()))
    start = time.time()    
    
    execs = []
    kuaishoucount  =   100
    shuabaocount   =   2#+random.randint(0,10)
    kuaikandiancount = 50
    qutoutiaocount =   5#-4
    quanmincount =     5#-3
    wechatcount =      5
    miducount=         80
    huoshancount=      50
    xiangkancount=     30         
                
    overexecs = []

    auto=WeChatAutomation(deviceName,version)
    auto.basecount = wechatcount+random.randint(0,10)
    execs.append(auto)      

    auto=ShuabaoAutomation(deviceName,version)
    auto.basecount = shuabaocount
    overexecs.append(auto)     

    for iter in range(3):
        try:
            auto=WeChatAutomation(deviceName,version)
            auto.basecount = wechatcount+random.randint(0,5)
            overexecs.append(auto)                          
        except Exception:    
            print(sys.exc_info())    
#     for iter in range(4):
#         try:
#             auto=KuaiShouAutomation(deviceName,version)
#             auto.basecount = kuaishoucount+random.randint(0,50)
#             overexecs.append(auto)                          
#         except Exception:    
#             print(sys.exc_info())
 
    for iter in range(4):
        try:
            
            auto=KuaiKanDianAutomation(deviceName,version)
            auto.basecount = kuaikandiancount+random.randint(0,20)
            overexecs.append(auto)                           
        except Exception:    
            print(sys.exc_info())             
    for iter in range(4):
        try:
            auto=QutoutiaoAutomation(deviceName,version)
            auto.basecount = qutoutiaocount+random.randint(0,5)
            overexecs.append(auto)                         
        except Exception:    
            print(sys.exc_info()) 
    for iter in range(4):
        try:
            auto=QuanMinAutomation(deviceName,version)
            auto.basecount = quanmincount+random.randint(0,5)
            overexecs.append(auto)                         
        except Exception:    
            print(sys.exc_info())     
    for iter in range(4):
        try:
            auto=QujianpanAutomation(deviceName,version)
            overexecs.append(auto)                       
        except Exception:    
            print(sys.exc_info())  
    for iter in range(4):
        try:
            auto=MiduAutomation(deviceName,version)
            auto.basecount = miducount+random.randint(0,50)            
            overexecs.append(auto)                       
        except Exception:    
            print(sys.exc_info())   
    for iter in range(4):
        try:
            auto=HuoShanAutomation(deviceName,version)
            auto.basecount = huoshancount+random.randint(0,50)            
            overexecs.append(auto)                       
        except Exception:    
            print(sys.exc_info())  
    for iter in range(4):
        try:
            auto=XiangKanAutomation(deviceName,version)
            auto.basecount = xiangkancount+random.randint(0,25)            
            overexecs.append(auto)                       
        except Exception:    
            print(sys.exc_info())  

                                                         
    np.random.shuffle(overexecs)
    
    execs.extend(overexecs)
    while True:
        for ex in execs:
            ex.actAutomation()             
        
        break
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (deviceName, (end - start)))               
            
if __name__ == '__main__':   
        

         
    devices = [('ORL1193020723','9.1.1'),('PBV0216C02008555','8.0'),('UEUDU17919005255','8.1.1'),('UEU4C16B16004079','8.1.1.1'),('A7QDU18420000828','9.0'),('SAL0217A28001753','9.1')]
         
    devices = [('ORL1193020723','9.1.1')]#Cupai 9
    #devices = [('PBV0216C02008555','8.0')] #huawei P9
    #devices = [('UEUDU17919005255','8.1.1')] #huawei Honor 6X
    devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X 
#   #  
#   #
    #devices = [('A7QDU18420000828','9.0')]  
    #devices = [('SAL0217A28001753','9.1')]       
    #device=(deviceName,version) = devices[0]
    #SheepingDevices(device)
    #devices = [('ORL1193020723','9.1.1'),('PBV0216C02008555','8.0'),('UEUDU17919005255','8.1.1'),('UEU4C16B16004079','8.1.1.1'),('A7QDU18420000828','9.0'),('SAL0217A28001753','9.1')]
    devices = [('ORL1193020723','9.1.1'),('PBV0216C02008555','8.0'),('UEUDU17919005255','8.1.1'),('UEU4C16B16004079','8.1.1.1')]
    devices = [('UEUDU16B18012018', '7.0'), ('A7QDU18420000828', '9'), ('PBV0216C02008555', '8.0.0'), ('UEUDU17919005255', '8.0.0'), ('ORL1193020723', '9')]
     
    readDeviceId = list(os.popen('adb devices').readlines())
    devices=[]
    for outputline in readDeviceId:
        codes = re.findall(r'(^\w*)\t', outputline)
        if len(codes)!=0:
            deviceName=codes[0]
               
#             versionoutput=list(os.popen('adb -s %s shell  getprop ro.build.version.release' % (deviceName)).readlines())
#             version = re.findall(r'(^.*)\n', versionoutput[0])[0]
#             devices.append((deviceName,version))
            devices.append((deviceName,""))
                 
    print('Parent process %s.' % os.getpid())
    p = Pool(len(devices))
    for device in devices:
        p.apply_async(SheepingDevices, args=(device,))
        time.sleep(30)        
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    
    
    
#from appium.webdriver.common.touch_action import TouchAction
#TouchAction(self.driver).press(x=228,y=647).move_to(x=228,y=647).wait(100).move_to(x=812,y=647).wait(100).move_to(x=812,y=940).wait(100).move_to(x=812,y=1241).release().perform()
        