# coding: utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from time import sleep
import logging
from appium import webdriver
import re
import time
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
import traceback
from qutoutiao.BaseOperation import BaseOperation
from qutoutiao.BaseOperation import AutomationException 
from qutoutiao.BaseOperation import ExecutionParam
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#assii unicode
from urllib.request import quote
from _ast import Raise

class  QujianpanAutomation(BaseOperation):
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################        
#####################################################################################################################################                
    def __init__(self, executionparam=None,timerange=(0,24)):
        super(QujianpanAutomation,self).__init__(executionparam)
        
        self.stat.AppName = self.__class__.__name__
        
        self.gabageDict = {}#         

    def init_driver(self): 
        self.desired_caps['appPackage'] = 'com.qujianpan.client'        
        self.desired_caps['appActivity'] = 'com.qujianpan.client.ui.GuideActivity'
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)

        self.initAfterDriver()       
    def tearDown(self):
        super().tearDown() 
        self.driver.terminate_app('com.qujianpan.client')        
        self.driver.quit()
    def checkExecutionTime(self):
        if super().checkExecutionTime():
            if int(time.time()) - self.stat.lastExecutionTime >= 30*60: #30 minutes
                return True
        return False        
    def watchQuJianPanSmallAdsAndClose(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")        
        for iter in range(10):
            if self.driver.current_activity == "com.qujianpan.adlib.adcontent.view.patchad.AdPatchBaseActivity":
                break
            else:
                self.sleep()
        self.sleep(6)
        self.driver.back()
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")        

    def MoneyBoxn(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")                
        self.logger.info("-------"+self.deviceName+"------"+"--------go to 储蓄罐-------")#go to me tab
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[1]")
        if element:      
            element.click()         

        if self.stat.dailyFirstExecution:
            self.logger.info("-------"+self.deviceName+"------"+"--------7 日礼包-------")#7 日礼包
            element=self.find_element_by_xpath_without_exception(self.driver, '//android.view.View/android.view.View/android.view.View[5]/android.view.View')
            if element:      
                element.click()                      
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="观看视频签到"]')
                if element:
                    current_activity = self.driver.current_activity
                    element.click()
                    self.logger.info("-------"+self.deviceName+"------"+"--------watch ads-------") 
                    self.watchAdsAndCloseWindow(current_activity) 
                    self.sleep(1)
                    element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="收下了"]')
                    if element:
                        element.click() 
                        
                                          
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="明天再来吧"]')
                if element:
                    self.logger.info("-------"+self.deviceName+"------"+"--------not first time in a day-------") #not first time in a day
                    element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.Image[contains(@text,"model_close")]')
                    if element:
                        element.click()                                          
        
        self.sleep(6)
        self.logger.info("-------"+self.deviceName+"------"+"--------collect money-------")#collect money
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View/android.view.View/android.view.View[8]')
        if element:
            element.click() 
        self.sleep(6)
        self.logger.info("-------"+self.deviceName+"------"+"--------兑换-------")#兑换
        element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="兑换"]')
        if element:
            element.click()   
            element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="立即兑换"]')
            if element:
                element.click()                       
                self.sleep(1)
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="知道了"]')
                if element:
                    element.click()  
                    self.sleep(4)
                    self.watchQuJianPanSmallAdsAndClose()
        self.sleep(6)
        self.logger.info("-------"+self.deviceName+"------"+"--------领取奖励-------")#领取奖励
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View/android.view.View/android.view.View[9]')
        if element:
            element.click() 
            element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="幸运翻倍"] ')
            if element:
                current_activity = self.driver.current_activity
                element.click()   
                self.watchAdsAndCloseWindow(current_activity) 
            element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="知道了"]')
            if element:
                element.click()   
        self.sleep(6)                        
        self.logger.info("-------"+self.deviceName+"------"+"--------每日任务------")#每日任务
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[1]/android.view.View[1]/android.view.View[5]/android.view.View[2]')
        if element:
            element.click() 
            self.sleep(1)        
            
            while(True):
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="领取奖励"]')
                if element:
                    current_activity = self.driver.current_activity
                    element.click() 
                    self.sleep(3)
                    if self.driver.current_activity != '.ui.MainActivity':
                        self.sleep(6)
                        self.watchAdsAndCloseWindow(current_activity)        
                else:
                    break
            
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.Image[contains(@text,"model_close")]')
            if element:
                element.click()
        
        self.sleep(6)   
        self.logger.info("-------"+self.deviceName+"------"+"--------小猪转盘------")#小猪转盘
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[1]/android.view.View[1]/android.view.View[5]/android.view.View[3]')
        if element:
            element.click() 
            self.sleep(1)        
            for iter in range(15): 
                self.logger.info("-------"+self.deviceName+"------"+"........."+str(iter)+".........")          
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[1]/android.view.View[5]/android.view.View[2]')
                if element:
                    current_activity = self.driver.current_activity
                    element.click()
                    element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="放弃"]')
                    if element:
                        element.click()
                        self.sleep(2)
                        self.logger.info("-------"+self.deviceName+"------"+"--------finished 小猪转盘 , back to main window------")
                        self.driver.back()
                        break 
                    self.sleep(3)
                    #direct money
                    if self.driver.current_activity == 'com.innotech.jb.combusiness.web.SignDetailWebActivity':
                        self.logger.info("-------"+self.deviceName+"------"+"--------direct money------")
                        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="恭喜抽中"]/../android.view.View')
                        if element:
                            element.click()
                            
                        continue
                    #3 seconds ads
                    elif self.driver.current_activity == 'com.qujianpan.adlib.adcontent.view.patchad.AdPatchBaseActivity':
                        self.logger.info("-------"+self.deviceName+"------"+"--------3 seconds ads------")
                        self.watchQuJianPanSmallAdsAndClose()
                        continue
                    else:
                        #long ads
                        self.logger.info("-------"+self.deviceName+"------"+"--------long ads------")
                        self.watchAdsAndCloseWindow(current_activity)
                        continue
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")        
    
    def closeNormalWindow(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")        
        #close window if it exists
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close')                                   
        if element:
            element.click()  
        else:
            self.driver.back()   
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")
         
    def preExecution(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")
        self.sleep(10)
        self.logger.info("-------"+self.deviceName+"------"+"--------refuse to update------")#refuse to update
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivClose')
        if element:
            element.click()
        
        self.logger.info("-------"+self.deviceName+"------"+"--------close 提现 ads------")#close 提现 ads
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/new_red_close')
        if element:
            element.click()
        
        self.logger.info("-------"+self.deviceName+"------"+"--------refuse to install ------")#refuse to install 
        #self.sleep(5)
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivChaiClose')
        if element:
            element.click() 
            
        self.logger.info("-------"+self.deviceName+"------"+"--------close home tab show------")#close home tab show
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/home_bottom_close')
        if element:
            element.click()               
            
        self.logger.info("-------"+self.deviceName+"------"+"--------go to me tab------")#           #go to me tab
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[4]")
        if element:      
            element.click() 
        
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/mainCardGoldTotal')
        if element:
            self.stat.startMoney=int(element.text.split()[0].strip())
            if self.stat.dailyFirstExecution:
                self.stat.dailyStartMoney = self.stat.startMoney                                    
        
        #watch a ads             
        #element=self.find_element_by_xpath_without_exception(self.driver, "//android.support.v7.widget.RecyclerView[@resource-id='com.qujianpan.client:id/jiliTaskrecyclerView']/android.widget.LinearLayout[2]")
        #if element:      
        #    element.click()
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")
       
    def afterExecution(self): 
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")               
#           #go to me tab
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[4]")
        if element:      
            element.click() 
        
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/mainCardGoldTotal')
        if element:
            self.stat.endMoney=int(element.text.split()[0].strip())
            if self.stat.dailyLastExecution:
                self.stat.dailyEndMoney = self.stat.endMoney
            
            #提现
            if self.stat.startMoney > 1000000:
                element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/mainCardCatchGlod')
                element.click()
                self.sleep(1)
                    #10 元
                element=self.find_element_by_xpath_without_exception(self.driver, "//android.support.v7.widget.RecyclerView[@resource-id='com.qujianpan.client:id/withdrawalAmountRecyView']/android.view.ViewGroup[2]")
                if element:      
                    element.click()
                    self.sleep(1)
                    #提现
                    element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/cashSubmit')
                    if element:
                        element.click()
                        self.sleep(1)   
                        self.driver.back()
                        self.sleep(1)
                        self.driver.back()                 
        #finish the task
        super().afterExecution()                
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")
                
    def sign(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")

        try:
#           #go to zhuan qian tab
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[3]")
            if element:      
                element.click()
            self.sleep(10)
            element = self.find_element_by_xpath_without_exception(self.driver, '//*[@resource-id="signUpAddBtn"]')
            if element:
                element.click()
                self.sleep(3)
                element = self.find_element_by_xpath_without_exception(self.driver, '//*[@resource-id="signUpAddBtn"]')
                if element:
                    current_activity = self.driver.current_activity
                    element.click()
                    #wait ads pop up 
                    self.sleep(3)
                    self.watchAdsAndCloseWindow(current_activity)
                    self.sleep(3)
                    self.closeNormalWindow()
                            
            #self.driver.switch_to.context('WEBVIEW_com.qujianpan.client')                
#                               
        except Exception:
            self.logger.info("-------"+self.deviceName+"------"+'sigin except!')
            traceback.print_exc()              
        
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")
    def watchAdsAndCloseWindow(self, activity):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")                
        ads_activity = None
        #wait for the ads pop up
        for iter in range(60):
            if self.driver.current_activity !=activity:
                ads_activity = self.driver.current_activity
                break
            self.sleep()
        #watch ads until it finished
        for iter in range(60):
            #if self.driver.current_activity== 'com.qujianpan.adlib.adcontent.view.video.AdInVideoBaseActivity':
            self.logger.info("-------"+self.deviceName+"------"+self.driver.current_activity+'out')
            if self.driver.current_activity in set(['com.bytedance.sdk.openadsdk.activity.TTRewardVideoActivity','com.innotech.jb.combusiness.web.SignDetailWebActivity']):
                if self.closeAdsDetails():
                    break
            elif self.driver.current_activity=='com.iclicash.advlib.ui.front.InciteADActivity':
                self.sleep(1)
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="点击重播"]')
                if element:
                    if self.closeAdsDetails():
                        break                            
            else: #com.iclicash.advlib.ui.front.ADBrowser
                self.logger.info("-------"+self.deviceName+"------"+self.driver.current_activity)
                self.driver.back()
                self.sleep(3)
                if self.closeAdsDetails():
                    break                
                if self.driver.current_activity == activity:
                    break

        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")        
        
    def closeAddsWindow(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")                
        for iter in range(2):
            if self.closeAdsDetails():
                self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------") 
                break
        
    def closeAdsDetails(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")                        
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/tt_video_ad_close')
        if element:
            element.click()
            self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------1")           
            return True    
        
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.LinearLayout[@resource-id='com.qujianpan.client:id/action_bar_root']/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.View")
        if element and element.is_enabled() and element.is_displayed():
           element.click()
           self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------2")           
           return True
        
        return False
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")           
                    
    def actAutomation(self):
        super().actAutomation()
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------")                
        self.stat.startTime = time.time()
        crashCount=0
        while(True):
            try:
                super().preExecution()
                self.init_driver()
                #self.unlockTheScreen()
                self.preExecution()
                if self.stat.dailyFirstExecution:
                    self.sign()
                self.MoneyBoxn()
                self.afterExecution()
                self.tearDown()
                break
#             except WebDriverException:
#                 traceback.print_exc()
#                 if self.driver:
#                     self.tearDown()                  
#                 break        
            except Exception:
                traceback.print_exc()         
                if self.driver:
                    try:
                        self.tearDown()  
                    except Exception:
                        pass
                crashCount+=1                    
                if crashCount > 3:
                    break                             

        self.stat.endTime = time.time()
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------")        
        
if __name__ == '__main__':    

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    #devices = [('DU2YYB14CL003271','4.4.2')]
    devices = [('PBV0216C02008555','8.0')] #huawei P9 
    #devices = [('ORL1193020723','9.1.1')]#Cupai 9
    devices = [('UEUDU17919005255','8.0.0')] #huawei Honor 6X 
    #devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X 
    
    
       

    #devices = [('A7QDU18420000828','9'),('SAL0217A28001753','9.1'),('UEUDU17919005255','8.0.0')]  
    devices = [('SAL0217A28001753','9.1')]     
    for (deviceName,version) in devices:
        xp=ExecutionParam(deviceName,version,username='18601793121', password='Initial0')
        qujianpan = QujianpanAutomation(xp,(0,24))  
        
        qujianpan.stat.dailyFirstExecution = True
        qujianpan.stat.dailyLastExecution = False 
          
        t = threading.Thread(target=qujianpan.actAutomation)
        t.start()
        sleep(random.randint(0, 10))
        



        