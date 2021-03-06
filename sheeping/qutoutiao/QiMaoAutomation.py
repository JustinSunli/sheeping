# coding: utf-8
import sys
import os
from bokeh.themes import default
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

class  QiMaoAutomation(BaseOperation):   
    def __init__(self, executionparam=None,timerange=(0,24)):
        super(QiMaoAutomation,self).__init__(executionparam)
        
        self.stat.AppName = self.__class__.__name__
        self.basecount = 50 + random.randint(0,10)
        self.gabageDict = {}#   
        self.onceAdsCount = 0      

    def init_driver(self): 
        self.desired_caps['appPackage'] = 'com.kmxs.reader'        
        self.desired_caps['appActivity'] = 'com.km.app.home.view.LoadingActivity'
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)

        self.initAfterDriver()       
    def tearDown(self):
        super().tearDown() 
        self.driver.terminate_app('com.kmxs.reader')        
        self.driver.quit()
    def checkExecutionTime(self):
        if super().checkExecutionTime():
            if int(time.time()) - self.stat.lastExecutionTime >= 30*60: #30 minutes
                return True
        return False          
    
    def watchAdsVedio(self,defaultActivity):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        
        if self.driver.current_activity == defaultActivity:
            return
        if self.onceAdsCount >=10:
            self.logger.info("-------"+self.deviceName+"------"+"Reach Max Count--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
            return
        self.onceAdsCount+=1
        self.sleep(5,5)
        if self.driver.current_activity!=defaultActivity:
            #close ads window
            self.driver.back()
        self.sleep(2)
        if self.driver.current_activity!=defaultActivity:
            #
            element = self.find_element_by_id_without_exception(self.driver,'com.kmxs.reader:id/tt_video_ad_close_layout')
            if element:       
                element.click()  
            
            self.sleep(2)
            if self.onceAdsCount>=6:#exceed 60s
                element = self.find_elements_by_xpath_without_exception(self.driver,'//android.webkit.WebView/following-sibling::android.widget.ImageView[1]')
                if element:
                    element.click()
            
            if self.driver.current_activity!=defaultActivity:
                self.watchAdsVedio(defaultActivity)     
        self.onceAdsCount=0
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        
    def goToGetReadMoney(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        
        elements=self.find_elements_by_xpath_without_exception(self.driver,'//android.view.View[@text="?????????"]')
        for ele in elements:
            ele.click()
            self.sleep(2)
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[contains(@text,'??????????????????')]")
            if element:
                currentActivity=self.driver.current_activity
                element.click() 
                self.sleep(3)
                self.watchAdsVedio(currentActivity)  

        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                        
    def watchNovels(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
           
        #random choose novels
        elements=self.find_elements_by_id_without_exception(self.driver, 'com.kmxs.reader:id/bookshelf_book_item_image')
        randomelement = None
        if len(elements)!=0:
            idx = random.randint(1,len(elements)-1)
            randomelement = elements[idx]
        else:
            self.logger.info("-------"+self.deviceName+"------"+"Don't have novels--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
            return
        if self.possibilityExecution(50):
            randomelement.click()
        else:
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="????????????"]')
            if element:
                element.click() 
            else:
                randomelement.click()  
        self.sleep(1)                 
            
        sleepseconds = 9
        for iter in range(self.basecount):
            #sometimes pause
            if self.possibilityExecution(15):
                sleep(sleepseconds+20)
            else:
                self.sleep(sleepseconds,3)
            #??????????????????
            if self.possibilityExecution(20):
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="?????????"]')
                if element:
                    element.click()
                    sleep(2)
                    self.goToGetReadMoney()
                    self.driver.back()
                 
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="?????????????????????"]')
            if element:
                self.keyboard.clickAPoint((945,1900), (1045,1950))
                self.sleep(1)               
            else:                    
                if self.possibilityExecution(50):
                    self.keyboard.clickAPoint((945,174), (1045,206))  
                else:
                    self.keyboard.clickAPoint((945,1900), (1045,1950))

        self.driver.back()
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="????????????"]')
        if element:
            element.click()              

        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) )) 
    def drawMoney(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) )) 

        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[contains(@text,"????????????")]')
        if element:        
            txt = element.text
            goldNumber = int(txt[txt.find('???')+1:txt.find('(')])
            if goldNumber < 100000:
                return
        element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@resource-id='app']/android.widget.ListView/android.view.View[2]")
        if element:
            element.click()   
            self.sleep(2)
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[contains(@text,"????????????")]')
            if element:              
                currentActivity=self.driver.current_activity
                element.click() 
                self.sleep(4)
                self.watchAdsVedio(currentActivity) 
                self.driver.back()
                           
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                       
    def doTask(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        
        sleepseconds = 20    
        sleep(sleepseconds+random.randint(0,5000)/1000)
        
        self.watchNovels()
        
        #go to Me
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@text='??????']")
        if element:
            element.click()   
            self.sleep(3)
            self.driverSwipe.SwipeUpALittle()
            if self.possibilityExecution(0):
                element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='????????????']")
                if element:
                    element.click() 
                    self.drawMoney()           
            #????????????
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@text='????????????']")
            if element:
                element.click() 
                self.sleep(3) 
                
                #??????
                #??????50??????
                element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[contains(@text,'??????????????????')]")
                if element:
                    currentActivity=self.driver.current_activity
                    element.click() 
                    self.watchAdsVedio(currentActivity) 
                #????????? 
                element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[contains(@text,'?????????')]")
                if element:
                    element.click() 
                    self.sleep(1)
                    element = self.find_element_by_xpath_without_exception(self.driver,"//*[@text='????????????']/../following-sibling::android.view.View[1]")
                    if element:
                        element.click() 
                    
                    
                self.driverSwipe.SwipeUp()
                self.driverSwipe.SwipeUpALittle()
                #watch a ads
                element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[contains(@text,'?????????')]")
                if element:
                    currentActivity=self.driver.current_activity
                    element.click()  
                    self.sleep(2)
                    self.watchAdsVedio(currentActivity) 
                    element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[contains(@text,'?????????')]")
                    if element:
                        element.click()
            
                #???????????????
                self.goToGetReadMoney()  
                self.driver.back()
                            
            #???????????????
            if self.stat.dailyFirstExecution:
                element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='???????????????']")
                if element:
                    element.click()
                    self.sleep(1)
                    count=5
                    #ads number
                    element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[contains(@text,'????????????????????????')]")
                    if element:
                        txt = element.text
                        count = int( txt[len(txt)-1:len(txt)] )
                    for iter in range(count): 
                        #element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[contains(@text,'javascript')]")
                        element = self.find_element_by_xpath_without_exception(self.driver,"//*[@resource-id='app']/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[3]")                        
                        if element:
                            currentActivity=self.driver.current_activity
                            element.click()
                            self.sleep(5)                                                     
                            if self.driver.current_activity != currentActivity:
                                self.watchAdsVedio(currentActivity)
                                
                            element = self.find_element_by_xpath_without_exception(self.driver,"//*[@text='??????']")
                            if element:                        
                                element.click() 
                                self.sleep(3)
                                continue                                
                    self.driver.back()

            
            self.driverSwipe.SwipeDownALittle()
            #today money, total money
            element=self.find_element_by_id_without_exception(self.driver, "com.kmxs.reader:id/user_fragment_coin")
            if element:
                self.stat.endMoney = int(element.text)
            element=self.find_element_by_id_without_exception(self.driver, "com.kmxs.reader:id/user_fragment_coin_today")
            if element:
                self.stat.dailyEndMoney = int(element.text)                                
        
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        
      
                   
    def actAutomation(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                

        self.stat.startTime = time.time()

        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.doTask()
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
             ExecutionParam(deviceName='E4JDU17506004553',version='9',port='4733',bootstrapPort='4734',username='17132126385', password='Initial0')
             #,
             #ExecutionParam(deviceName='SAL0217A28001753',version='9',port='4735',bootstrapPort='4736',username='15216706926', password='Initial0')            
             ]
    
    #devices = [('UEU4C16B16004079','9.1')]       
    #devices = [('192.168.0.106:5555','9.1')]

    #close existed appium processes
    #os.system("start /b taskkill /F /t /IM node.exe")
    for device in devices:
        #start appium.exe
#         os.system("start /b appium -a 127.0.0.1 -p %s -bp %s --session-override --relaxed-security" % (device.port, device.bootstrapPort))
#         sleep(10)
        #xp=ExecutionParam(deviceName='A7QDU18420000828',version='9',port='4723',bootstrapPort='4723',username='18601793121', password='Initial0')
        qimao = QiMaoAutomation(device,(0,24))  
        
        qimao.stat.dailyFirstExecution = True
        qimao.stat.dailyLastExecution = False 
          
        #qimao.actAutomation()         
        t = threading.Thread(target=qimao.actAutomation)
        t.start()
        sleep(random.randint(0, 10))