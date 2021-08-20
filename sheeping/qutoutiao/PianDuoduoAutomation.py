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
# from airtest.core.api import *
# from airtest.cli.parser import cli_setup
from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

import threading
import time


#assii unicode
from urllib.request import quote

class  PianDuoduoAutomation(BaseOperation):   
    def __init__(self, executionparam=None,timerange=(0,24)):
        super(PianDuoduoAutomation,self).__init__(executionparam)
        self.stat.AppName = self.__class__.__name__
        self.gabageDict = {}#   
        self.basecount = 10+random.randint(0,10)   
        self.currentcount=0           

    def init_driver(self): 
        self.desired_caps['appPackage'] = 'com.tencent.submarine'        
        self.desired_caps['appActivity'] = 'com.tencent.submarine.ui.HomeActivity'
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)

        self.initAfterDriver()       
    def tearDown(self):
        super().tearDown() 
        self.driver.terminate_app('com.tencent.submarine')        
        self.driver.quit()
    def checkExecutionTime(self):
        if super().checkExecutionTime():
            if int(time.time()) - self.stat.lastExecutionTime >= 30*60: #30 minutes
                return True
        return False
    
    def watchAdsVedio(self,originalActivity):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))    
        self.sleep(12, 5)
        for iter in range(10): 
            self.driver.back()
            if self.driver.current_activity == originalActivity:
                break
            element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@text='继续观看']")
            if element:
                element.click()
                self.sleep(5) 
            else:
                break           

        #watch another ads
        element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@text='看广告再赚100金币']")
        if element:
            if self.possibilityExecution(95):
                element.click()
                self.watchAdsVedio(originalActivity)
            else:
                #Back to watch tv
                self.driver.back()
                               
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))      
    
    def watchTV(self,count=15):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
        self.sleep(10)
        element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@resource-id='com.tencent.submarine:id/ge']")
        if element:
            element.click()
            self.earnMoney()         
        for iter in range(count): 
            self.logger.info("-------"+self.deviceName+"------"+"Watch TV 45 Second--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
            self.sleep(30,30)
                
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                                   
    def earnMoney(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
        #Earn Money Page
        self.driverSwipe.SwipeUpALittle()
        element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@text='签到']")
        if element:
            element.click() 
            element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@text='看广告再赚100金币']")
            if element:
                originalActivity=self.driver.current_activity
                element.click()
                self.watchAdsVedio(originalActivity) 
                return          
                
        self.driverSwipe.SwipeUp()
        #领取时间奖励
        elements =  self.find_elements_by_xpath_without_exception(self.driver,"//*[@text='领取']")
        for element in elements:
            element.click() 
            element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@text='看广告再赚100金币']")
            if element:
                originalActivity=self.driver.current_activity
                element.click()
                self.watchAdsVedio(originalActivity) 
                return
    
        self.driverSwipe.SwipeUp()
        #领取时间奖励
        elements =  self.find_elements_by_xpath_without_exception(self.driver,"//*[@text='看广告']")
        for element in elements:
            element.click() 
            element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@text='看广告再赚100金币']")
            if element:
                originalActivity=self.driver.current_activity
                element.click()
                self.watchAdsVedio(originalActivity)  
                return   
                             
                    
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                                   
                                    
    def doTasks(self): 
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                

        self.watchTV(random.randint(10,15))

        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                    
    def mainAutomation(self,number):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        self.doTasks()        
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
         
    def actAutomation(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                

        self.stat.startTime = time.time()

        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.mainAutomation(self.basecount)
                try:
                    self.tearDown()
                except Exception:
                    traceback.print_exc()    
                break
            except WebDriverException:
                traceback.print_exc()
                break        
            except Exception:
                traceback.print_exc()  
                if self.driver :
                    self.tearDown() 
                crashCount+=1                    
                if crashCount > 5:
                    break  
        self.stat.endTime = time.time()
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        
    
if __name__ == '__main__':    

    devices=[
             #ExecutionParam(deviceName='A7QDU18420000828',version='9',port='4723',bootstrapPort='4724',username='18601793121', password='Initial0')
             #,
             #ExecutionParam(deviceName='UEU4C16B16004079',version='9',port='4725',bootstrapPort='4726',username='17131688728', password='Initial0')
             #,
             #ExecutionParam(deviceName='E4J4C17412001168',version='9',port='4727',bootstrapPort='4728',username='16536703898', password='Initial0')
             #,
             #ExecutionParam(deviceName='3LGDU17328005108',version='9',port='4729',bootstrapPort='4730',username='17132126387', password='Initial0')
             #,
             #ExecutionParam(deviceName='CXDDU16C07003822',version='9',port='4731',bootstrapPort='4732',username='15372499352', password='Initial0')
             #,
             #ExecutionParam(deviceName='E4JDU17506004553',version='9',port='4733',bootstrapPort='4734',username='17132126385', password='Initial0')
             #,
             ExecutionParam(deviceName='SAL0217A28001753',version='9',port='4735',bootstrapPort='4736',username='15216706926', password='Initial0')            
             ]
    #devices = [('UEU4C16B16004079','9.1')]   
    
    #devices = [('192.168.0.106:5555','9.1')]
    
    #close existed appium processes
#     os.system("start /b taskkill /F /t /IM node.exe")
    for device in devices:
        #start appium.exe
#         os.system("start /b appium -a 127.0.0.1 -p %s -bp %s --session-override --relaxed-security" % (device.port, device.bootstrapPort))
#         sleep(10)
        #
        auto = PianDuoduoAutomation(device,(0,24))  
        
        auto.stat.dailyFirstExecution = True
        auto.stat.dailyLastExecution = False 
          
        #toutiaoAuto.actAutomation()         
        t = threading.Thread(target=auto.actAutomation)
        t.start()
        sleep(random.randint(0, 10))