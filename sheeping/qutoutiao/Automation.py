# coding: utf-8
from multiprocessing import Pool
from time import sleep
from appium import webdriver
import json
import re
import time
import os
import sys
import random
import threading
import traceback
import numpy as np
from queue import PriorityQueue
from qutoutiao import DriverSwipe, WeChatAutomation
from qutoutiao.QutoutiaoAutomation import QutoutiaoAutomation 
from qutoutiao.QujianpanAutomation import QujianpanAutomation
from qutoutiao.ShuabaoAutomation import ShuabaoAutomation
from qutoutiao.KuaiShouAutomation import KuaiShouAutomation
from qutoutiao.WeChatAutomation import WeChatAutomation
from qutoutiao.KuaiKanDianAutomation import KuaiKanDianAutomation
from qutoutiao.MiduAutomation import MiduAutomation
from qutoutiao.HuoShanAutomation import HuoShanAutomation
from qutoutiao.XiangKanAutomation import XiangKanAutomation

from qutoutiao.quanminautomation import QuanMinAutomation
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from qutoutiao.baseoperation import BaseOperation

class Automation():
    def __init__(self, deviceName='A7QDU18420000828',version='9',timerange=(0,24),username='18601793121', password='Initial0'):
        self.deviceName=deviceName
        self.version=version
            
    def stringToTimeData(self,str_data):
        # 格式时间成毫秒
        strptime = time.strptime(str_data,"%Y-%m-%d %H:%M:%S")
        #print("strptime",strptime)
        mktime = int(time.mktime(strptime)*1000)
        #print("mktime",mktime)
        return mktime      
    def getLastExecution(self,executedList):
        if not executedList:
            return None
        if len(executedList)==0:
            return None
        sortedList = sorted(executedList, key=lambda x:x['stat']['lastExecutionTime'],reverse = True)
        return sortedList[0]
    
    def writeDictionary(self,dict,fileName):
        with open(fileName,'w',encoding='utf-8') as file: 
            json.dump(dict, file, ensure_ascii=False)   
            file.close()
    def readDictionary(self,fileName):
        try:
            with open(fileName,'r',encoding='utf-8') as fileR:   
                newdict = json.load(fileR)
                fileR.close()
                return newdict
        except Exception:    
            print(sys.exc_info())              
        return None
    
    def SheepingDevices(self):
        (deviceName,version) = (self.deviceName,self.version)
        print('Run task %s (%s)...' % (deviceName, os.getpid()))
        start = time.time() 
         
        todayDate = time.localtime(time.time())
        todayString = str(todayDate.tm_year)+'-'+str(todayDate.tm_mon)+'-'+str(todayDate.tm_mday)
        dictFileName = 'executionrecord/'+deviceName+'-'+todayString+'.txt'
        executionDictionary = self.readDictionary(dictFileName)
        if not executionDictionary: 
            executionDictionary = {}
        
        kuaishoucount  =   100
        shuabaocount   =   2#+random.randint(0,10)
        kuaikandiancount = 50
        qutoutiaocount =   5#-4
        quanmincount =     5#-3
        wechatcount =      5
        miducount=         80
        huoshancount=      50
        xiangkancount=     30         
                    
    
        executionList = []
        executionQueue = PriorityQueue()
        
        
#         auto=WeChatAutomation(deviceName,version)
#         auto.basecount = wechatcount+random.randint(0,10)
#     
#         auto=ShuabaoAutomation(deviceName,version)
#         auto.basecount = shuabaocount
#         executionList.append(auto)     
    
    
        QuanjianpanExecutionPlan = [(7,23),(7,9),(12,14),(8,23),(18,20),(7,23),(7,23),(7,23)]
        for (fromTime,toTime) in QuanjianpanExecutionPlan:
            try:
                auto=QujianpanAutomation(deviceName,version,(fromTime,toTime))
                auto.stat.lastExecutionTime = self.stringToTimeData(todayString+" 0:0:0")
                executionList.append(auto)                       
            except Exception:    
                print(sys.exc_info())  
    
    
        np.random.shuffle(executionList)     
        
        for iter in range(1000):
            #
            #sheduling the execution
            for auto in executionList:
                if not auto.stat.executed:
                    if auto.checkExecutionTime():
                        executedList = executionDictionary.get(auto.stat.AppName);
                        lastExecution = self.getLastExecution(executedList)
                        if lastExecution:
                            auto.stat.lastExecutionTime = lastExecution.stat.lastExecutionTime
                        executionQueue.put(auto)
            
            if executionQueue.empty():
                break
            
            #execution
            auto = executionQueue.get()
            executedList = executionDictionary.get(auto.stat.AppName);
            lastExecution = self.getLastExecution(executedList)
            if lastExecution:
                auto.stat.lastExecutionTime = lastExecution.stat.lastExecutionTime
                auto.stat.dailyFirstExecution = False
            else:
                auto.stat.dailyFirstExecution = True
                
            auto.actAutomation()
            
            executionQueue.queue.clear()

        end = time.time()
        print('Task %s runs %0.2f seconds.' % (deviceName, (end - start)))             
        
    #     for iter in range(3):
    #         try:
    #             auto=WeChatAutomation(deviceName,version)
    #             auto.basecount = wechatcount+random.randint(0,5)
    #             executionList.append(auto)                          
    #         except Exception:    
    #             print(sys.exc_info())    
    # #     for iter in range(4):
    # #         try:
    # #             auto=KuaiShouAutomation(deviceName,version)
    # #             auto.basecount = kuaishoucount+random.randint(0,50)
    # #             executionList.append(auto)                          
    # #         except Exception:    
    # #             print(sys.exc_info())
    #  
    #     for iter in range(4):
    #         try:
    #             
    #             auto=KuaiKanDianAutomation(deviceName,version)
    #             auto.basecount = kuaikandiancount+random.randint(0,20)
    #             executionList.append(auto)                           
    #         except Exception:    
    #             print(sys.exc_info())             
    #     for iter in range(4):
    #         try:
    #             auto=QutoutiaoAutomation(deviceName,version)
    #             auto.basecount = qutoutiaocount+random.randint(0,5)
    #             executionList.append(auto)                         
    #         except Exception:    
    #             print(sys.exc_info()) 
    #     for iter in range(4):
    #         try:
    #             auto=QuanMinAutomation(deviceName,version)
    #             auto.basecount = quanmincount+random.randint(0,5)
    #             executionList.append(auto)                         
    #         except Exception:    
    #             print(sys.exc_info())     
    #     for iter in range(4):
    #         try:
    #             auto=QujianpanAutomation(deviceName,version)
    #             executionList.append(auto)                       
    #         except Exception:    
    #             print(sys.exc_info())  
    #     for iter in range(4):
    #         try:
    #             auto=MiduAutomation(deviceName,version)
    #             auto.basecount = miducount+random.randint(0,50)            
    #             executionList.append(auto)                       
    #         except Exception:    
    #             print(sys.exc_info())   
    #     for iter in range(4):
    #         try:
    #             auto=HuoShanAutomation(deviceName,version)
    #             auto.basecount = huoshancount+random.randint(0,50)            
    #             executionList.append(auto)                       
    #         except Exception:    
    #             print(sys.exc_info())  
    #     for iter in range(4):
    #         try:
    #             auto=XiangKanAutomation(deviceName,version)
    #             auto.basecount = xiangkancount+random.randint(0,25)            
    #             executionList.append(auto)                       
    #         except Exception:    
    #             print(sys.exc_info())  
    
                                                         
              
            
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
    for (deviceName,version) in devices:
        automation = Automation(deviceName,version)
        t = threading.Thread(target=automation.SheepingDevices)
        t.start()
        
        time.sleep(30)        
    print('Waiting for all subprocesses done...')
    
    
    
#from appium.webdriver.common.touch_action import TouchAction
#TouchAction(self.driver).press(x=228,y=647).move_to(x=228,y=647).wait(100).move_to(x=812,y=647).wait(100).move_to(x=812,y=940).wait(100).move_to(x=812,y=1241).release().perform()
        