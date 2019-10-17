# coding: utf-8
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
from qutoutiao import key_codes
from qutoutiao import DriverSwipe
from qutoutiao import Utils
from qutoutiao import keyboards
import traceback
from qutoutiao.baseoperation import BaseOperation 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException

#assii unicode
from urllib.request import quote

class  KuaiKanDianAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        super(KuaiKanDianAutomation,self).__init__()
        #�ռ����� ���ֻ�--����--������ѡ��---ָ��λ��-���������ֶ������Ǹ�webviewԪ�أ��ֻ����Ϸ�����ʾ��x��y������ 
        
        #adb not found
        #netstat -ano|findstr '5037'
        #tasklist |findstr '15828'
        
        # adb devices
        # adb shell pm list package # adb shell pm list package -3 -f 
        # adb logcat -c // clear logs
        # adb logcat ActivityManager:I *:s
        
#

        self.deviceName=deviceName
        self.version=version
        self.username=username
        self.password=password
        self.driver = None
          
        self.basecount = 5
        self.currentcount = 0              
#         
#         self.username = username
#         self.password = password
    def init_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = self.version
        desired_caps['deviceName'] = self.deviceName
        desired_caps['appPackage'] = 'com.yuncheapp.android.pearl'
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.kuaishou.athena.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = keyboards.KeyBoards(self.driver)
     
    def tearDown(self):
        self.driver.quit()    
        
    def pullMoney(self):
        sleep(15+random.randint(0,2000)/1000)
        self.driver.back()
        sleep(15+random.randint(0,2000)/1000)
        self.driver.back()
        sleep(15+random.randint(0,2000)/1000)                        
        self.find_element_by_xpath_without_exception(self.driver, "//android.widget.LinearLayout[@resource-id='com.yuncheapp.android.pearl:id/home_page_tab_bar']/android.widget.RelativeLayout[5]").click()
        self.driver.back()
        sleep(10+random.randint(0,5000)/1000)
        self.find_element_by_xpath_without_exception(self.driver, "//android.support.v7.widget.RecyclerView[@resource-id='com.yuncheapp.android.pearl:id/rv_card']/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView").click()
        # 5 yuan
        print(self.driver.contexts)
        #self.keyboard.clickAPoint((45,1455), (531,1611))
        #self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@resource-id='square1001']").click()
        self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Button").click()
        element = self.find_element_by_id_without_exception(self.driver,'com.yuncheapp.android.pearl:id/pay_web_view')
        if element:
            #success
            self.keyboard.clickAPoint((0,205), (531,1661))
            #get message code
        
        
    def clickMe(self):

        
        sleep(1+random.randint(0,3000)/1000)   
        #like the vedio
        if random.randint(0,125) % 5 ==0: 
            self.keyboard.clickAPoint((910,1075), (1000,1170))
            sleep(3+random.randint(0,3000)/1000)
            self.driver.back()
            sleep(1+random.randint(0,3000)/1000)
                
#         element = self.find_element_by_id_without_exception(self.driver,'com.yuncheapp.android.pearl:id/timer_anchor')
#         if element:
#             element.click()
#             sleep(3+random.randint(0,3000)/1000)
#             self.driver.back()
#             sleep(1+random.randint(0,3000)/1000)  
        #like the vedio
        if random.randint(0,125) % 3 ==0:
#             element = self.find_element_by_id_without_exception(self.driver,'com.yuncheapp.android.pearl:id/like_icon')
#             if element:
#                 element.click()
            self.keyboard.clickAPoint((927,1750), (985,1782))
            sleep(random.randint(0,5000)/1000)            
              
            
    def watchvedios(self,number):
        sleepseconds = 5
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        
        #go to mini vedio
        self.find_element_by_xpath_without_exception(self.driver, "//android.widget.LinearLayout[@resource-id='com.yuncheapp.android.pearl:id/home_page_tab_bar']/android.widget.RelativeLayout[4]").click()

        #choose one
        #sleep(10+random.randint(0,5000)/1000)
        self.keyboard.clickAPoint((0,205), (537,1159))
        
        sleepseconds = 10
        sleep(sleepseconds+random.randint(0,10000)/1000)
        for iter in range(number):
            self.driverSwipe.SwipeUp()
            #sometimes pause
            if random.randint(0,1024) % 17 ==0:
                sleep(sleepseconds+80+random.randint(0,15000)/1000)
            else:
                sleep(sleepseconds+random.randint(0,15000)/1000)             
            self.clickMe()
            
            self.currentcount+=1
            if(self.currentcount>self.basecount):
                break
            
        #sleep(sleepseconds+random.randint(0,10000)/1000)        
        print()
        
    def actAutomation(self):
        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.watchvedios(self.basecount)
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
    devices = [('SAL0217A28001753','9.1')]
    devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X     
    #devices = [('A7QDU18420000828','9')]  
    #devices = [('SAL0217A28001753','9.1')]     
    for (deviceName,version) in devices:
        kuaidiankan = KuaiKanDianAutomation(deviceName,version)
        t = threading.Thread(target=kuaidiankan.actAutomation(), args=(deviceName,version,))
        t.start()
        sleep(random.randint(0, 10000)/1000)