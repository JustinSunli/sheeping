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

class  TouTiaoAutomation(BaseOperation):   
    def __init__(self, executionparam=None,timerange=(0,24)):
        super(TouTiaoAutomation,self).__init__(executionparam)
        
        self.stat.AppName = self.__class__.__name__
        
        self.gabageDict = {}#         

    def init_driver(self): 
        self.desired_caps['appPackage'] = 'com.ss.android.article.lite'        
        self.desired_caps['appActivity'] = 'com.ss.android.article.lite.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)

        self.initAfterDriver()       
    def tearDown(self):
        super().tearDown() 
        self.driver.terminate_app('com.ss.android.article.lite')        
        self.driver.quit()
    def checkExecutionTime(self):
        if super().checkExecutionTime():
            if int(time.time()) - self.stat.lastExecutionTime >= 30*60: #30 minutes
                return True
        return False          
    
    def watchAdsVedio(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        
        
        #point = exists(Template(r"..\imagesrc\tpl1580907022260.png",threshold=0.8))
        sleep(22 +random.randint(0,5000)/1000)
#         element = self.find_element_by_xpath_without_exception(self.driver, "//com.lynx.tasm.behavior.ui.text.UIText[@text='关闭']")
#         if element:
#             element.click()
#         else:
#             self.driver.back()
        
        self.driver.back()
        #driver.find_element_by_xpath("//*[contains(@content-desc, '再看一个获得')]")
        self.sleep(3)
        element = self.find_element_by_xpath_without_exception(self.driver, "//*[contains(@content-desc, '再看一个获得')]")
        if element:
            #
            text = element.text#再看一个获得1200金币
            text=text[6:len(text)-2]
            goldnumber = int(text)
            if goldnumber > 1000:
                element.click()
                self.watchAdsVedio()
            else:
                element = self.find_element_by_accessibility_id_without_exception(self.driver, "坚持退出")
                if element:
                    element.click()
                    return
        else:
            element = self.find_element_by_accessibility_id_without_exception(self.driver, "坚持退出")
            if element:
                element.click()
        
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        
                
#         element=self.find_element_by_xpath_without_exception(self.driver, "//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View[3]")
#         if not element:
#             element=self.find_element_by_xpath_without_exception(self.driver, "//android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View[3]")
#         if element: 
#             element.click()
#             sleep(15 +random.randint(0,5000)/1000)
#             
#             element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@text='关闭广告']")
#             if element:
#                 element.click()
#             else:
#                 self.driver.back()        
#         else:
#             print()
#             #self.driver.back() 
    def doTask(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        

        #keyevent("BACK")
        sleepseconds = 5    
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        
        self.logger.info("-------"+self.deviceName+"------"+"------Watch Vedio--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
        times = random.randint(1,1)
        for iter in range(times):
            self.watchVedio()
        #可能横屏了
        self.driver.back()

        self.logger.info("-------"+self.deviceName+"------"+"------Go to Task--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))
        #go to task
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TabWidget/android.widget.RelativeLayout[3]/android.widget.ImageView")
        if element:
            element.click()
            sleep(5+random.randint(0,3000)/1000)
            #unknow temp pop activity
            self.driver.back()
            sleep(5+random.randint(0,3000)/1000)
            #guan bi
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='关闭']")
            if element:
                element.click()            
            #签到
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'签到成功')]/following-sibling::android.view.View[4]")
            if element:
                element.click()
                
            
        self.logger.info("-------"+self.deviceName+"------"+"------open golden ball--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))      
        #open golden ball
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='开宝箱得金币']")
        if element:
            element.click()
            sleep(2+random.randint(0,2000)/1000)
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='看完视频再领']")
            if element:
                element.click()
                sleep(2 +random.randint(0,2000)/1000)            
                self.watchAdsVedio()
        #element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='treasure-box-enable-1.da338c08']")
        #x1 = element.location['x']
        #y1 = element.location['y'] 
        #action=TouchAction(self.driver).long_press(element)
        
        self.logger.info("-------"+self.deviceName+"------"+"------走路--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))      
       ##走路
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='走路赚钱']/../following-sibling::android.view.View[1]")
        if element:       
            sleep(1+random.randint(0,1000)/1000)
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='走路赚钱']/../android.view.View[@text='走路赚钱']")
            if element:
                element.click()
                sleep(1 +random.randint(0,1000)/1000)
                element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'领取')]")
                if element:
                    element.click()
                    
                    element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='开心收下']")
                    if element: 
                        element.click()  
                                            
                    element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='看视频再领']")
                    if element:
                        element.click()
                        sleep(2 +random.randint(0,2000)/1000)            
                        self.watchAdsVedio()
                    self.driver.back()                        

        self.logger.info("-------"+self.deviceName+"------"+"------吃饭--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))      
        ##吃饭
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='吃饭补贴']/../following-sibling::android.view.View[1]")
        if element:
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='吃饭补贴']/../android.view.View[@text='吃饭补贴']")
            if element:
                element.click()
                sleep(1 +random.randint(0,1000)/1000)
                element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'领取')]")
                if element:
                    element.click()
                            
                    element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='开心收下']")
                    if element: 
                        element.click()                           
                                                
                    element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='看视频再领']")
                    if element:
                        element.click()
                        sleep(2 +random.randint(0,2000)/1000)            
                        self.watchAdsVedio() 
                    self.driver.back()
                    
        self.logger.info("-------"+self.deviceName+"------"+"------睡觉赚钱--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))              
         ##睡觉赚钱
        timeStruct = time.localtime(time.time())
        if timeStruct.tm_hour > 8 and timeStruct.tm_hour < 20:
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='睡觉赚钱']/../following-sibling::android.view.View[1]")
            if element:
                element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='睡觉赚钱']/../android.view.View[@text='睡觉赚钱']")
                if element:
                    element.click()
                    sleep(1+random.randint(0,1000)/1000)
                    element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='我睡醒了']")
                    if element:
                        element.click()
                        sleep(1+random.randint(0,1000)/1000)
                        element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'领取')]")
                        if element:
                            element.click()
                            
                            element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='开心收下']")
                            if element: 
                                element.click()                           
                            
                            
                            element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='看视频再领']")
                            if element:
                                element.click()
                                sleep(2 +random.randint(0,2000)/1000)            
                                self.watchAdsVedio() 
                            self.driver.back()#开心收下

        self.logger.info("-------"+self.deviceName+"------"+"------去睡觉--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))              

        timeStruct = time.localtime(time.time())
        if timeStruct.tm_hour > 20 or timeStruct.tm_hour < 2:            
            #go to sleep
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='睡觉赚钱']/../android.view.View[@text='睡觉赚钱']")
            if element:
                element.click()
                sleep(2+random.randint(0,2000)/1000)
                element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='我要睡了']")
                if element:
                    element.click()  
                self.driver.back()          
        
#         self.driverSwipe.SwipeUp()
#         sleep(1+random.randint(0,1000)/1000)
#         self.driverSwipe.SwipeUp()
#         element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View/android.view.View[13]/android.widget.Button[3]")
#         if element:
#             element.click()
#             for i in range(5) :
#                 element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@text='搜索']")
#                 if element:
#                     element.click()
#                     sleep(2+random.randint(0,3000)/1000)
#                     self.driver.back()  
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        

    def watchVedio(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        #    
        #go to vedio
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TabWidget/android.widget.RelativeLayout[2]/android.widget.ImageView")
        if element:
            element.click()    
            sleep(2+random.randint(0,3000)/1000)
            element.click() 
            sleep(2+random.randint(0,3000)/1000)
            elements = self.find_elements_by_xpath_without_exception(self.driver, "//android.widget.ImageView[contains(@content-desc, '播放视频')]")  
            if len(elements) !=0 :
                element = elements[random.randint(0,len(elements)-1)]
                element.click()
                ra =random.randint(5,10)
                for iter in range(ra):
                    element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@resource-id='com.bytedance.article.lite.plugin.xigua.shortvideo.player:id/video_complete_finish_replay']")
                    if element:
                        break
                    else:
                        if self.driver.current_activity != '.activity.SplashActivity':
                            break
                        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Button[contains(@text, '立即')]")
                        if element:
                            break
                        else:
                            sleep(60)
                    
                #sleep(random.randint(5*1000*60,10*1000*60)/1000)
        #element = self.find_element_by_xpath_without_exception(element, "../following-sibling::android.view.View[1]")
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))        
         
                   
    def actAutomation(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                

        self.stat.startTime = time.time()

        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.doTask()
#                 self.GotoMeAndView()
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
    os.system("start /b taskkill /F /t /IM node.exe")
    for device in devices:
        #start appium.exe
        os.system("start /b appium -a 127.0.0.1 -p %s -bp %s --session-override --relaxed-security" % (device.port, device.bootstrapPort))
        sleep(10)
        #xp=ExecutionParam(deviceName='A7QDU18420000828',version='9',port='4723',bootstrapPort='4723',username='18601793121', password='Initial0')
        toutiaoAuto = TouTiaoAutomation(device,(0,24))  
        
        toutiaoAuto.stat.dailyFirstExecution = True
        toutiaoAuto.stat.dailyLastExecution = False 
          
        #toutiaoAuto.actAutomation()         
        t = threading.Thread(target=toutiaoAuto.actAutomation)
        t.start()
        sleep(random.randint(0, 10))