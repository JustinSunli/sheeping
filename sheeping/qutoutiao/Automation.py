# coding: utf-8
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

from qutoutiao.quanminautomation import QuanMinAutomation
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from qutoutiao.baseoperation import BaseOperation
        
def SheepingDevices(device):
    (deviceName,version) = device
    while(True):
        try:
            kuaishoucount  =   100+random.randint(0,50)
            shuabaocount   =   2#+random.randint(0,10)
            kuaikandiancount = 100+random.randint(0,20)
            qutoutiaocount =   20+random.randint(0,10)
            quanmincount =     10+random.randint(0,10)
            wechatcount =      20+random.randint(0,10)            
            
            execs = []
            
            auto=KuaiShouAutomation(deviceName,version)
            auto.basecount = kuaishoucount
            execs.append(auto)

            auto=KuaiKanDianAutomation(deviceName,version)
            auto.basecount = kuaikandiancount
            execs.append(auto)
            
            auto=ShuabaoAutomation(deviceName,version)
            auto.basecount = shuabaocount
            execs.append(auto)
            
            auto=QutoutiaoAutomation(deviceName,version)
            auto.basecount = qutoutiaocount
            execs.append(auto)
            
            auto=QuanMinAutomation(deviceName,version)
            auto.basecount = quanmincount
            execs.append(auto)
            
            auto=QujianpanAutomation(deviceName,version)
            execs.append(auto)

            auto=WeChatAutomation(deviceName,version)
            auto.basecount = wechatcount
            execs.append(auto)
            
            np.random.shuffle(execs)
            for auto in execs:
                auto.actAutomation() 
                                              
            #Always execution 
            break  
        except Exception:    
            print('phone session terminated!')
            print(sys.exc_info())
            
if __name__ == '__main__':   
#     #('DU2YYB14CL003271','4.4.2'),
#     devices = [('A7QDU18420000828','9'),('SAL0217A28001753','9.1')]
#     for device in devices:
#         t = threading.Thread(target=SheepingDevices(device), args=())
#         t.start()
#         sleep(random.randint(0, 10))
         
     

         
    devices = [('ORL1193020723','9.1.1')]#Cupai 9
    devices = [('PBV0216C02008555','8.0')] #huawei P9
    devices = [('UEUDU17919005255','8.1.1')] #huawei Honor 6X
    devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X 
    

#     
# 
    devices = [('A7QDU18420000828','9.0')]  
    devices = [('SAL0217A28001753','9.1')]       
    device=(deviceName,version) = devices[0]
    SheepingDevices(device)
    
#     while(True):
#         try:
#             #actAutomation(deviceName,version)     
#             actAutomation(deviceName,version)
#             actShuabao(deviceName,version)
#             actAutomation(deviceName,version)
#                                           
#                     
#              #actWechating(deviceName,version)
#             break
#                                                    
#         except Exception:    
#             print('phone session terminated!')
#             print(sys.exc_info())
        