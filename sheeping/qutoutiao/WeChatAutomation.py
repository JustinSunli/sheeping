# coding: utf-8
from time import sleep
from appium import webdriver
import re
import time
import os
import sys
import math
import random
import threading
from qutoutiao import Key_Codes
from qutoutiao import DriverSwipe
from qutoutiao import Utils
from qutoutiao import KeyBoards
from selenium.common.exceptions import NoSuchElementException
import traceback
from qutoutiao.BaseOperation import BaseOperation 
from selenium.common.exceptions import WebDriverException
from multiprocessing import Pool




class  WeChatAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        super(WeChatAutomation,self).__init__()
        #�ռ����� ���ֻ�--����--������ѡ��---ָ��λ��-���������ֶ������Ǹ�webviewԪ�أ��ֻ����Ϸ�����ʾ��x��y������ 
        
        #adb not found
        #netstat -ano|findstr '5037'
        #tasklist |findstr '15828'
        
        # adb devices
        # adb shell pm list package
        # adb logcat -c // clear logs
        # adb logcat ActivityManager:I *:s
#         
#         self.username = username
#         self.password = password
        self.deviceName=deviceName
        self.version=version
        self.username=username
        self.password=password
        self.basecount = 10
        self.currentcount = 0  
        self.driver = None          
        
#         
#         self.username = username
#         self.password = password
    def init_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = self.version
        desired_caps['deviceName'] = self.deviceName
        desired_caps['appPackage'] = 'com.tencent.mm'
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = keyboards.KeyBoards(self.driver)
             
    def tearDown(self):
        self.driver.quit()


    def findWilliam(self):
        sleep(5+random.randint(0,5000)/1000)
#         # go to me
#         #work#opts={'command':'input','args':['swipe','100','100','500', '500', '300']}
#         sleep(random.randint(0,5000)/1000)
#         self.driver.execute_script("mobile:shell",opts)
#         sleep(random.randint(0,5000)/1000)

        #search button
        self.find_element_by_xpath_without_exception(self.driver,"//com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ImageView").click()
        #self.keyboard.clickAPoint((821,105), (885,169))
        sleep(5+random.randint(0,3000)/1000)
        
        self.find_element_by_xpath_without_exception(self.driver,"//android.support.v7.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.EditText").click()
        sleep(random.randint(0,2000)/1000/3)
        
        #switch Chinese to English
        self.keyboard.pressChineseEnglish()
        sleep(5+random.randint(0,3000)/1000)

        #input search keyword 'William'
        #self.driver.find_elements_by_xpath("//android.widget.EditText")[0].send_keys('William')
#         for letter in '0123456789abcdefghijklmnopqrstuvwxyz'.upper():
#             self.keyboard.preAKey(letter)
        sleep(5+random.randint(0,3000)/1000)        
        for letter in 'william'.upper():
            self.keyboard.preAKey(letter)
        sleep(5+random.randint(0,3000)/1000)
        
        #find the first one
        self.find_element_by_xpath_without_exception(self.driver,"//android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.LinearLayout").click()
        #self.keyboard.clickAPoint((43,350), (1050,460))
        sleep(5+random.randint(0,3000)/1000)
        
        self.clickInputboxAndSwithLanguage()
        
        #record correct input box position
        element=self.find_element_by_xpath_without_exception(self.driver,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.EditText")
        if element:
            self.inputBoxLocationY = element.location['y']
        
    def clickInputboxAndSwithLanguage(self):
        #click input box
        self.find_element_by_xpath_without_exception(self.driver,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.EditText").click()
        #self.keyboard.clickAPoint((150,2040), (830,2130))
        sleep(5+random.randint(0,3000)/1000)
        
        #switch Chinese to English
        self.keyboard.pressChineseEnglish()
        sleep(5+random.randint(0,3000)/1000)
    def getTheMoney(self):
        self.width=self.driver.get_window_size().get('width')
        self.height=self.driver.get_window_size().get('height')
        #honor V9
        if self.width == 1080 and self.height==1920 : 
            self.keyboard.clickAAbsolutePoint((894,981), (936,1029))
        #coolpad 9
        elif self.width ==720 and self.height==1366:
            self.keyboard.clickAAbsolutePoint((596,772), (626,801)) 
        #Honor 6X
        elif self.width ==1080 and self.height==1800:
            self.keyboard.clickAAbsolutePoint((894,869), (936,903)) 
        #Honor P9 
        elif self.width ==1080 and self.height==1792:
            self.keyboard.clickAAbsolutePoint((894,864), (936,889)) 
        #Honor V10
        else:#self.width ==1080 and self.height==2160:
            self.keyboard.clickAPoint((810,1234), (835,1257))                                            
       
    def chatWithWilliam(self,limits):
        #in case there exists words
        element=self.find_element_by_xpath_without_exception(self.driver,"//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Button")
        if element:
            element.click()  
                  
        novellines = self.util.watchvedios('LesMiserables.txt')
        lettercount = 0
        batch = 120
        hongbaocount=0
        for line in novellines:
            pattern = re.compile('[^A-Za-z0-9_ ]')
            line = pattern.sub(' ',line)
            for letter in line.upper():
                lettercount+=1
                self.keyboard.preAKey(letter)
                
                if lettercount // batch:
                    #get the money
                    #self.keyboard.clickAPoint((810,1234), (835,1257))
                    self.getTheMoney()
                    sleep(1+random.randint(0,2000)/1000/4)
                    
#                     #double the money
#                     self.keyboard.clickAPoint((405,697), (645,741))
#                     sleep(3+random.randint(0,2000)/1000/4)
#                     
#                     #wait the ads end
#                     sleep(40+random.randint(0,10000)/1000)
#                     
#                     #close the ads window
#                     self.keyboard.clickAPoint((972,77), (1004,104))
#                     sleep(3+random.randint(0,2000)/1000/4)
#                     
#                     #close the double bonus window
#                     self.keyboard.clickAPoint((906,469), (925,491))
#                     sleep(3+random.randint(0,2000)/1000/4)                    
                                        
#                     #close the window without double
#                     self.keyboard.clickAPoint((910,689), (920,735))
#                     sleep(3+random.randint(0,2000)/1000/4) 
                    
                    #back to wechat                     
                    self.driver.back()
                                             
                    #send the message
                    if self.width ==720 and self.height==1366:
                        self.keyboard.clickAAbsolutePoint((610,682), (700,727))
                    else:
                        element=self.find_element_by_xpath_without_exception(self.driver,"//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.Button")
                        if element:
                            element.click()
                    
                    sleep(5+random.randint(0,2000)/1000/4)
            
                    #switch Chinese to English
                    #self.keyboard.pressChineseEnglish()
                    #sleep(3+random.randint(0,3000)/1000)

                    lettercount%=batch  
                    hongbaocount+=1
                    if hongbaocount > limits:
                        return
                    
                    #prevent do too many during crash and crash again
                    self.currentcount+=1
                    if(self.currentcount>self.basecount):
                        return
                    
                    #sometimes lose focus
                    element=self.find_element_by_xpath_without_exception(self.driver,"//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.EditText")
                    if element:
                        inputboxy = element.location['y']
                        if(inputboxy>self.inputBoxLocationY):
                            self.clickInputboxAndSwithLanguage()


            sleep(random.randint(0,3000)/1000)
        print("the whole novels is typed in! Wonderfull work!")
        
    def actAutomation(self):
        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.findWilliam()
                self.chatWithWilliam(self.basecount)
                self.tearDown()
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


if __name__ == '__main__':   
    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    devices = [('DU2YYB14CL003271','4.4.2')]
    devices = [('SAL0217A28001753','9')]
    #devices = [('A7QDU18420000828','9')]  
    devices = [('PBV0216C02008555','8.0')] #huawei P9
    devices = [('ORL1193020723','9.1.1')]#Cupai 9
    #devices = [('UEUDU17919005255','8.1.1')] #huawei Honor 6X 

    #devices = [('SAL0217A28001753','9')]     
    for (deviceName,version) in devices:
        wechat = WeChatAutomation(deviceName,version)
        wechat.basecount = 10
        t = threading.Thread(target=wechat.actAutomation(), args=(deviceName,version,))
        t.start()
        sleep(random.randint(0, 10))
        