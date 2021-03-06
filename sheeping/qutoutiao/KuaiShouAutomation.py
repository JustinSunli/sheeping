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

class  KuaiShouAutomation(BaseOperation):   
    def __init__(self, executionparam=None,timerange=(0,24)):
        super(KuaiShouAutomation,self).__init__(executionparam)
        self.stat.AppName = self.__class__.__name__
        self.gabageDict = {}#   
        self.basecount = 10+random.randint(0,10)   
        self.currentcount=0           

    def init_driver(self): 
        self.desired_caps['appPackage'] = 'com.kuaishou.nebula'        
        self.desired_caps['appActivity'] = 'com.yxcorp.gifshow.HomeActivity'
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)

        self.initAfterDriver()       
    def tearDown(self):
        super().tearDown() 
        self.driver.terminate_app('com.kuaishou.nebula')        
        self.driver.quit()
    def checkExecutionTime(self):
        if super().checkExecutionTime():
            if int(time.time()) - self.stat.lastExecutionTime >= 30*60: #30 minutes
                return True
        return False
    
    def doTasks(self): 
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        self.sleep(3)
        self.sleep(2)          
        element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='????????????']")
        if element:
            element.click()
            #if self.driver.back()
        #????????????   parent::   
        element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='????????????']/../preceding-sibling::android.view.View[1]")
        if element:
            element.click()
        self.sleep(1)
        self.driverSwipe.SwipeUp()
        self.sleep(1)
        
        element =  self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='?????????']")
        #self.find_element_by_id_without_exception(self.driver,'//android.view.View[contains(@text,"?????????")]')
        if element:
            element.click()              
            #if self.driver.back() 
            
        #open golden ball
        element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='??????????????????']")
        if element:
            element.click() 
            self.sleep(2)
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='????????????????????????']")
            if element:
                element.click()             
                self.watchAdsVedio() 
            
        if self.possibilityExecution(40):
            ##???????????????
            idx = random.randint(3,5)
            for iter in range(idx):  
                element=self.find_element_by_xpath_without_exception(self.driver,"//android.widget.Button[contains(@text,'??????')]")
                if element:
                    element.click() 
                    self.watchAdsVedio()  
                    self.sleep(2) 
                else:
                    break
                
        if self.possibilityExecution(40):                                           
            # ????????????
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.Button[contains(@text,'?????????')]")
            if element:
                element.click()             
                idx = random.randint(3,5)
                for iter in range(idx):
                    for iterb in range(5):
                        self.sleep(5)
                    self.driverSwipe.SwipeUp()
                
                self.driver.back()
                #?????????
                element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/exit_btn')
                if element:       
                    element.click()     
        
        
        #daily money
        self.driverSwipe.SwipeDown()
        element = self.find_element_by_xpath_without_exception(self.driver,"//*[@text='????????????']/../following-sibling::android.view.View[1]")
        if element:
            self.stat.dailyEndMoney = int(element.text)
        element = self.find_element_by_xpath_without_exception(self.driver,"//*[contains(@text,'???????????????')]/../following-sibling::android.view.View[1]")
        if element:
            self.stat.endMoney = float(element.text)
        if self.possibilityExecution(100):
            self.drawMoney()      
        #quit the page
        self.driver.back()
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))    
    def drawMoney(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                        
        if self.stat.endMoney and self.stat.endMoney > 5:
            element = self.find_element_by_xpath_without_exception(self.driver,"//*[contains(@text,'???????????????')]/../following-sibling::android.view.View[1]")
            if element:
                element.click()
                self.sleep(3)
                element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='?????????']")
                if element:
                    element.click()
                    self.sleep(3)
                    element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='3???']")
                    if element:
                        element.click()
                        self.sleep(1)
                        element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='????????????']")
                        if element:
                            element.click()                                             
                            self.sleep(1)
                            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.Button[@text='??????']")
                            if element:
                                element.click()                                             
                                self.sleep(1)                                
                                element = self.find_element_by_xpath_without_exception(self.driver,"//android.view.View[@text='????????????']")
                                if element:
                                    element.click()  
                                    self.sleep(5)
                                    #switch contexts
                                    element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='???????????????']/../..")
                                    if element:
                                        element.click()
                                        self.sleep(1)                                                                                                
                                        element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.Button[@text='??????']")
                                        if element:
                                            element.click()
                                            self.sleep(1)
                                            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.Button[@text='?????????????????????']")
                                            if element:
                                                element.click()
                                                self.sleep(5)
                                                #switch contexts
                                                element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.Button[@text='??????']")
                                                if element:
                                                    element.click()                                            
                                                                                                                               
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                    
    def mainAutomation(self,number):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                

        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                
        sleepseconds=5
        sleep(sleepseconds+15+random.randint(0,5000)/1000)     
        #????????????
        element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/positive')
        if element:
            element.click()   
        self.sleep(2)
        
        #???????????????
        element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/close')
        if element:
            element.click()          
               
        #????????????
        element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/close')
        if element:
            element.click()  
        
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.webkit.WebView[@text="????????????"]')
        if element:
            self.stat.godMonitored=True  
                    
        self.driverSwipe.SwipeUpALittle()
        self.sleep(5)
        element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/circular_progress_bar')
        if element:
            element.click() 
            self.doTasks()
        #self.keyboard.clickAPoint((248,534), (484,804))  
        sleepseconds = 5
        fixedcomments=['cool','????????????','????????????','?????????','very good','nice','????????????','???????????????','??????????????????','??????','???????????????','?????????????????????????????????']        
        for iter in range(number):
            self.driverSwipe.SwipeUpALittle()
            #Skip all online
            for iter in range(5):
                element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/like_icon')
                if not element:   
                    #??????
                    self.driverSwipe.SwipeUpALittle() 
                else:
                    break     
            #sometimes pause
            if random.randint(0,1024) % 17 ==0:
                sleep(sleepseconds+sleepseconds+random.randint(0,10000)/1000)
            else:
                sleep(sleepseconds+random.randint(0,5000)/1000)
            #?????????
            element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/close')
            if element:
                element.click()
                              
            #like the vedio
            if self.possibilityExecution(30):
                element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/like_icon')
                if element:
                    element.click()
                    self.sleep(1)
            #write the comments
            if self.possibilityExecution(15):
                element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/comment_icon')
                if element:
                    element.click()  
                    comments=[]
                    if self.possibilityExecution(50):
                        elements=self.find_elements_by_id_without_exception(self.driver, 'com.kuaishou.nebula:id/comment')
                        for ele in elements:
                            comments.append(ele.text)
                    self.sleep(1)
                    element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/comment_editor_holder_text')
                    if element:
                        element.click()
                        self.sleep(1)
                        element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/editor')
                        if element:
                            if len(comments) != 0:
                                idx = random.randint(0,len(comments)-1)
                                comment=comments[idx]+', ???????????????'
                            else:
                                idx = random.randint(0,len(fixedcomments)-1)
                                comment=fixedcomments[idx]                                
                            element.send_keys(comment)
                            self.sleep(1)
                            element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/finish_button')
                            if element:
                                element.click()
                                self.sleep(1)

                        self.driver.back()
            

            if self.possibilityExecution(20): 
                element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/circular_progress_bar')
                if element:
                    element.click() 
                    self.doTasks()
                                             
            self.currentcount+=1
            if(self.currentcount>self.basecount):
                break


            
        #sleep(sleepseconds+random.randint(0,10))        
        self.logger.info("-------"+self.deviceName+"------"+"GoOut--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))            
    def watchAdsVedio(self):
        self.logger.info("-------"+self.deviceName+"------"+"Enter--------"+sys._getframe().f_code.co_name+"-------"+time.asctime( time.localtime(time.time()) ))                        
        for iter in range(20):
            self.sleep(5)
            element = self.find_element_by_id_without_exception(self.driver,'com.kuaishou.nebula:id/video_close_icon')
            if element:
                element.click() 
                break           
        if self.driver.current_activity!='com.yxcorp.gifshow.webview.KwaiYodaWebViewActivity':    
            self.driver.back()           
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
        auto = KuaiShouAutomation(device,(0,24))  
        
        auto.stat.dailyFirstExecution = True
        auto.stat.dailyLastExecution = False 
          
        #toutiaoAuto.actAutomation()         
        t = threading.Thread(target=auto.actAutomation)
        t.start()
        sleep(random.randint(0, 10))