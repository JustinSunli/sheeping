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

class  AiQiyiAutomation(BaseOperation):   
    def __init__(self, executionparam=None,timerange=(0,24)):
        super(AiQiyiAutomation,self).__init__(executionparam)
        self.stat.AppName = self.__class__.__name__
        self.gabageDict = {}#   
        self.basecount = 10+random.randint(0,10)   
        self.currentcount=0  
        self.onceAdsCount=0                 

    def init_driver(self): 
        self.desired_caps['appPackage'] = 'com.qiyi.video.lite'        
        self.desired_caps['appActivity'] = 'com.qiyi.video.lite.homepage.HomeActivity'
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)

        self.initAfterDriver()       
    def tearDown(self):
        super().tearDown() 
        self.driver.terminate_app('com.qiyi.video.lite')        
        self.driver.quit()
    def checkExecutionTime(self):
        if super().checkExecutionTime():
            if int(time.time()) - self.stat.lastExecutionTime >= 30*60: #30 minutes
                return True
        return False
    
    def watchAdsVedio(self,originalActivity):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
        self.onceAdsCount+=1
        if self.onceAdsCount>=10:
            self.logger.info("-------"+self.deviceName+"------"+"Strange work--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
            return
            
        self.sleep(20, 5)
        
        for iter in range(20): 
            self.driver.back()
            if self.driver.current_activity == originalActivity:
                break
            element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@text='继续观看']")
            if element:
                element.click()
                self.sleep(5) 
            else:
                break   
        if self.driver.current_activity != originalActivity:
            self.logger.info("-------"+self.deviceName+"------"+"Close Ads Failed--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
        self.sleep(3, 3)
        #watch another ads
        element =  self.find_element_by_xpath_without_exception(self.driver,"//*[contains(@text,'再赚')]")
        if element:
            if self.possibilityExecution(75):
                element.click()
                self.onceAdsCount=0
                self.watchAdsVedio(originalActivity)                              
            else:
                element =  self.find_element_by_xpath_without_exception(self.driver,"//android.view.ViewGroup/android.widget.ImageView[3]")
                if element:
                    element.click()  
        
        
        self.onceAdsCount=0  
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))      
    
    def watchTV(self,count=15):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))  
        #Home Page
        element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@resource-id='android:id/content']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]")
        if element:
            element.click() 
            
        self.sleep(5)          
        element1 = self.find_element_by_xpath_without_exception(self.driver,"//androidx.viewpager.widget.ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout/android.widget.ImageView") 
        element2 = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='观看历史']/../following-sibling::android.widget.ImageView[1]")
        if element1 and element2:
            if self.possibilityExecution(40):
                element1.click()
            else:
                element2.click()            
                      
        for iter in range(count*10): 
            self.sleep(2,2)
            element =  self.find_element_by_xpath_without_exception(self.driver,"//android.widget.Button[@text='开通会员']")
            if element:            
                break
            element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@content-desc='看视频领100金币']")
            if element:
                originalActivity=self.driver.current_activity
                element.click()
                self.watchAdsVedio(originalActivity)
                
#                 #Progess bar
#                 element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@resource-id='android:id/content']/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.View[1]")
#                 if element:
#                     element.click()              
#                     self.driverSwipe.SwipeUpALittle()
#                     #if self.driver.back()                             
            
        #watch TV Like the vedio
        if self.possibilityExecution(10):
            element =  self.find_element_by_xpath_without_exception(self.driver,"//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.widget.LinearLayout[2]/android.widget.RelativeLayout[1]/android.widget.ImageView[1]")
            if element:
                element.click()  
        
        #To Home Page
        self.driver.back()
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                                   
    def earnMoney(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
        #Earn Money Page
        element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@resource-id='android:id/content']/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]/android.widget.RelativeLayout[1]")
        if element:
            element.click() 
            self.sleep(5,5)
            #签到
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[contains(@text,'已累计签到')]/following-sibling::android.widget.ImageView[3]")
            if element:
                element.click()
            #恭喜获得邀请好友奖励
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[contains(@text,'恭喜获得邀请好友奖励')]/following-sibling::android.widget.ImageView[2]")
            if element:
                element.click()  
                          
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[contains(@text,'看视频再赚')]")
            if element:
                originalActivity=self.driver.current_activity
                element.click()
                self.watchAdsVedio(originalActivity) 
                   
            self.driverSwipe.SwipeUpALittle()
            #Open Box  "//android.view.View[contains(@content-desc,'开宝箱领金币')]"
            element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@resource-id='android:id/content']/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.widget.ImageView[1]")
            if element:
                element.click() 
                #邀请，No Ads
                element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[contains(@text,'邀请好友赚')]/../../following-sibling::android.widget.ImageView[1]")
                if element:
                    element.click()
                # Open Ads
                element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[contains(@text,'看视频再赚')]")
                if element:
                    originalActivity=self.driver.current_activity
                    element.click()
                    self.watchAdsVedio(originalActivity) 
            #Get watch tv time Money
            element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@content-desc='领取']")
            if element:
                element.click()
                
            #self.driverSwipe.SwipeUpALittle()
            #1000金币，10个广告
            if self.possibilityExecution(70):
                for iter in range(random.randint(3,6)):
                    #
                    element =  self.find_element_by_xpath_without_exception(self.driver,"//*[contains(@content-desc,'1000金币轻松赚')]")
                    if element:
                        originalActivity=self.driver.current_activity
                        element.click()
                        element =  self.find_element_by_xpath_without_exception(self.driver,"//*[@text='我知道了']")
                        if not element:
                            if self.driver.current_activity!=originalActivity:
                                self.watchAdsVedio(originalActivity)
                            else:
                                break
                        else:
                            #finished 10 ads,close the window
                            element =  self.find_element_by_xpath_without_exception(self.driver,"//android.view.ViewGroup/android.widget.ImageView[3]")
                            if element:
                                element.click()                                        
            self.driverSwipe.SwipeDown()              
            element =  self.find_element_by_xpath_without_exception(self.driver,"//android.widget.ImageView[contains(@content-desc,'金币明细')]/preceding-sibling::android.view.View[2]")
            if element:
                self.stat.endMoney = float(element.get_attribute("content-desc"))
            if self.possibilityExecution(100):
                self.drawMoney()                
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                                   
    def drawMoney(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
        if self.stat.endMoney and self.stat.endMoney > 1:
            element =  self.find_element_by_xpath_without_exception(self.driver,"//android.widget.ImageView[contains(@content-desc,'金币明细')]")
            if element:
                self.keyboard.clickAPoint((850,345), (970,360))
                self.sleep(2)
                element =  self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='提现']")
                if element:
                    element.click()                 
                    self.sleep(2)
                    element =  self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='连续签到3天']/..")
                    if element:
                        element.click()
                        element =  self.find_element_by_xpath_without_exception(self.driver,"//android.widget.Button[@text='立即提现']")
                        if element:
                            element.click()  
                            #not enough 3 days
                            if not element:
                                self.driver.back()
                                self.driver.back()
                                return                             
                            self.sleep(5)  
                            element =  self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='确认提现']")
                            if element:
                                element.click()
                                self.sleep(2)  
                                element =  self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='确认提现']")
                                if element: 
                                    element.click()
                                else:                               
                                    code=None 
                                    #验证码
                                    try:
                                        self.driver.start_activity('com.android.mms', '.ui.ConversationList')
                                    except Exception:
                                        pass
                                    self.sleep(20)
                                    element=self.find_element_by_xpath_without_exception(self.driver,"//android.widget.ListView/android.widget.FrameLayout")
                                    if element:
                                        element.click()
                                        element=self.find_element_by_xpath_without_exception(self.driver,"//android.widget.ListView/android.widget.FrameLayout")
                                        if element:
                                            element.click()  
                                            element=self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[contains(@text,'验证码')]")
                                            msg = element.text
                                            idx = msg.find('验证码')
                                            code=msg[idx+len('验证码'):len(msg)]
                                            self.driver.back()
                                            self.sleep(1)
                                            self.driver.back()
                                            self.sleep(1)
                                            self.driver.back()
                            
                                            element =  self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='验证手机号']/following-sibling::android.view.View[3]/android.widget.EditText")
                                            if element:
                                                element.send_keys(code)                                        
                                    if code:
                                        pass
                
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
    def doTasks(self): 
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        self.sleep(10, 5)
        for iter in range(random.randint(1,3)):
            #self.watchTV(random.randint(10,15))
            if self.possibilityExecution(100):
                self.earnMoney()        

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
        auto = AiQiyiAutomation(device,(0,24))  
        
        auto.stat.dailyFirstExecution = True
        auto.stat.dailyLastExecution = False 
          
        #toutiaoAuto.actAutomation()         
        t = threading.Thread(target=auto.actAutomation)
        t.start()
        sleep(random.randint(0, 10))