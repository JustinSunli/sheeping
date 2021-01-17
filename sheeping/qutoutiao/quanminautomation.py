# coding: utf-8
# 验证身份证
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
import traceback
from qutoutiao.BaseOperation import BaseOperation 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from multiprocessing import Pool


#assii unicode
from urllib.request import quote

class  QuanMinAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        super(QuanMinAutomation,self).__init__()
        #�ռ����� ���ֻ�--����--������ѡ��---ָ��λ��-���������ֶ������Ǹ�webviewԪ�أ��ֻ����Ϸ�����ʾ��x��y������ 
        
        #adb not found
        #netstat -ano|findstr '5037'
        #tasklist |findstr '15828'
        
        # adb devices
        # adb shell pm list package # adb shell pm list package -3 -f 
        # adb logcat -c // clear logs
        # adb logcat ActivityManager:I *:s
        
        #aapt dump badging C:\Users\Administrator\Desktop\api\ff0602.apk
        
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
        desired_caps['appPackage'] = 'com.baidu.minivideo'
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'app.activity.splash.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = KeyBoards.KeyBoards(self.driver)
     
     
    def tearDown(self):
        self.driver.quit()        
 
    def watchvedios(self,number):
        sleepseconds = 10
        sleep(sleepseconds+random.randint(0,10000)/1000)
        self.driver.back()        
        sleep(sleepseconds+random.randint(0,10000)/1000)
        self.driver.back()
        sleep(sleepseconds+random.randint(0,10000)/1000)
        self.driver.back()
        

        self.keyboard.clickAPoint((3,198), (537,1047))  
        
        sleepseconds = 5
        sleep(sleepseconds+random.randint(0,10000)/1000)
        for iter in range(number):
            self.driverSwipe.SwipeUp()
            #sometimes pause
            if random.randint(0,1024) % 11 ==0:
                sleep(sleepseconds+80+random.randint(0,5000)/1000)
            else:
                sleep(sleepseconds+random.randint(0,5000)/1000)            
            
            #like the vedio
            if random.randint(0,125) % 3 ==0:
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.FrameLayout[@resource-id="com.baidu.minivideo:id/detail_praise_lottie"]/android.widget.ImageView')
                if element:
                    element.click()            
                    sleep(random.randint(0,15000)/1000)            
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
                if self.driver:
                    self.tearDown()  
                crashCount+=1                    
                if crashCount > 5:
                    break                          

if __name__ == '__main__':    

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    devices = [('DU2YYB14CL003271','4.4.2')]
    #devices = [('SAL0217A28001753','9')]
    devices = [('A7QDU18420000828','9')]  
    #devices = [('SAL0217A28001753','9.1')]     
    for (deviceName,version) in devices:
        quanmin = QuanMinAutomation(deviceName,version)
        t = threading.Thread(target=quanmin.actAutomation(), args=(deviceName,version,))
        t.start()
        sleep(random.randint(0, 10000)/1000)