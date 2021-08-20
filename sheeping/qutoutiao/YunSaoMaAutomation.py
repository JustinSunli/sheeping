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
#from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from appium.webdriver.common.touch_action import TouchAction

import threading
import time


#assii unicode
from urllib.request import quote

class  YunSaoMaAutomation(BaseOperation):   
    def __init__(self, executionparam=None,timerange=(0,24)):
        super(YunSaoMaAutomation,self).__init__(executionparam)
        self.stat.AppName = self.__class__.__name__
        self.gabageDict = {}#   
        self.basecount = 10+random.randint(0,10)   
        self.currentcount=0           

    def init_driver(self): 
        self.desired_caps['appPackage'] = 'com.tencent.mm'        
        self.desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        self.desired_caps['chromeOptions'] = { 
                                               # 'androidPackage': 'com.android.chrome',
                                                'androidProcess': 'com.tencent.mm:tools',
                                               'w3c': False
                                              } 
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)

        self.initAfterDriver()   
        self.driver.implicitly_wait(1)    
    def tearDown(self):
        super().tearDown() 
        self.driver.terminate_app('com.tencent.mm')        
        self.driver.quit()
    def checkExecutionTime(self):
        if super().checkExecutionTime():
            if int(time.time()) - self.stat.lastExecutionTime >= 90*60: #1.5hour minutes
                return True
        return False
    def drawMoney(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))  
#         element = self.find_element_by_xpath_without_exception(self.driver,"//*[@id='exchange_money']")
#         
#         if element:
#             money = float(element.text)
#             if money >= 0.3:
                #slider
        smallElement = self.find_element_by_xpath_without_exception(self.driver,"//span[@id='label']/img")
        backgroundElement=self.find_element_by_xpath_without_exception(self.driver,"//*[@id='labelTip']")
        
        location = backgroundElement.location
        size = backgroundElement.size
        toyL = location['y'] + size['height']
        toxL = location['x'] + size['width']
        
        fromXL=smallElement.location['x']
        fromYL=smallElement.location['y']
        
        TouchAction(self.driver).press(x=fromXL,y=fromYL).move_to(x=toxL,y=toyL).release().perform()
                    
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                        
    def doYunSaoMaTasks(self): 
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))          
        #pause read
        self.sleep(5)  
        #read articles, 26/hour,50-120/day
        randomCount = random.randint(12,18)
        for iter in range(randomCount):
            element = self.find_element_by_xpath_without_exception(self.driver,"//*[@id='task_load_read']")
            if self.ElementUsable(element):
                break  
            element = self.find_element_by_xpath_without_exception(self.driver,"//*[@id='task_none_read']")
            if self.ElementUsable(element):
                break                
            self.logger.info("-------"+self.deviceName+"------"+"Read the "+str(iter)+"th Article------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
            self.readArticle()
            self.currentcount+=1  
            self.driver.back()
            self.sleep(2) 
             
        self.sleep(5)  
        element = self.find_element_by_xpath_without_exception(self.driver,"//*[@id='sign_btn']")
        if not element:         
            self.driver.back()
            self.driver.implicitly_wait(0.05)  
            count=0
            for iter in range(50):
                try:
                    self.find_element_by_xpath_without_exception(self.driver,"//*[@id='task_btn_read']").click()
                    count+=1
                    break
                except Exception:
                    continue
                self.logger.info("-------"+str(count)+"------"+str(time.time())) 
                self.driver.implicitly_wait(3)
        
        if self.stat.dailyFirstExecution:
            #sign       
            element = self.find_element_by_xpath_without_exception(self.driver,"//*[@id='sign_btn']")
            if element:
                element.click()      
                self.sleep(2)
                element = self.find_element_by_xpath_without_exception(self.driver,"//*[@id='sign_first_close_btn']")
                if element:
                    element.click()     
        #draw money
        if self.possibilityExecution(0):
            element = self.find_element_by_xpath_without_exception(self.driver,"//img[@class='draw_btn']")
            if element:
                element.click()              
                self.drawMoney() 
        
        element = self.find_element_by_xpath_without_exception(self.driver,"//div[@class='num goldNum']")
        if element:
            try:
              self.stat.endMoney = int(element.text)
            except Exception:
                goldNum = ""
                elements = self.find_elements_by_xpath_without_exception(self.driver,"//div[@class='num goldNum']/div/div[@class='mt-number-animate-dom']")
                for element in elements:
                    goldNum+=element.get_attribute('data-num')
                self.stat.endMoney = int(goldNum)
        #continue read
#         element = self.find_element_by_xpath_without_exception(self.driver,"//*[@id='task_btn_read']")
#         if element:
#             element.click()                       
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        
    def mainAutomation(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        self.sleep(15)
        #find
        element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='发现']")
        if element:
            element.click()
            
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='扫一扫']")
            if element:
                element.click()
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@content-desc="相册"]')
                if element:                
                    element.click()
                    self.sleep(3)
                    element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='所有图片']")
                    if element:
                        element.click()
                        element = self.find_element_by_xpath_without_exception(self.driver,"//*[@text='微信']")
                        if element:
                            element.click()   
                            element = self.find_element_by_xpath_without_exception(self.driver,"//*[@resource-id='com.tencent.mm:id/fbp']/android.widget.RelativeLayout[1]")
                            if element:
                                element.click() 
                                self.sleep(10)
                                if len(self.driver.contexts)>=2:
                                    self.driver.switch_to.context(self.driver.contexts[1])
#                                     self.driver.switch_to.context('WEBVIEW_com.tencent.mm:tools')
#                                     self.driver.switch_to.context('WEBVIEW_com.tencent.mm:toolsmp')
                                    self.doYunSaoMaTasks()                            
                                

     
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
    def readArticle(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        #at least 6s
        for iter in range(7):
            self.sleep(2)
            if self.possibilityExecution(30):
                self.driverSwipe.SwipeUpALittle()
            else:
                self.driverSwipe.SwipeUp()
        if self.possibilityExecution(30):
            element =self.find_element_by_xpath_without_exception(self.driver,"//*[@id='js_parise_wording']") 
            if self.ElementUsable(element):
                element.click()               
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
                      
    def actAutomation(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                

        self.stat.startTime = time.time()

        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.mainAutomation()
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
             ExecutionParam(deviceName='UEU4C16B16004079',version='9',port='4725',bootstrapPort='4726',username='17131688728', password='Initial0')
             #,
             #ExecutionParam(deviceName='E4J4C17412001168',version='9',port='4727',bootstrapPort='4728',username='16536703898', password='Initial0')
             #,
             #ExecutionParam(deviceName='3LGDU17328005108',version='9',port='4729',bootstrapPort='4730',username='17132126387', password='Initial0')
             #,
             #ExecutionParam(deviceName='CXDDU16C07003822',version='9',port='4731',bootstrapPort='4732',username='15372499352', password='Initial0')
             #,
             #ExecutionParam(deviceName='E4JDU17506004553',version='9',port='4733',bootstrapPort='4734',username='17132126385', password='Initial0')
             #,
             #ExecutionParam(deviceName='SAL0217A28001753',version='9',port='4735',bootstrapPort='4736',username='15216706926', password='Initial0')            
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
        auto = YunSaoMaAutomation(device,(0,24))  
        
        auto.stat.dailyFirstExecution = True
        auto.stat.dailyLastExecution = False 
          
        #toutiaoAuto.actAutomation()         
        t = threading.Thread(target=auto.actAutomation)
        t.start()
        sleep(random.randint(0, 10))