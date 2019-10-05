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
#assii unicode
from urllib.request import quote

class  QuanMinAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
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
        self.keyboard = keyboards.KeyBoards(self.driver)
     
     
    def tearDown(self):
        self.driver.quit()        
 
    def watchvedios(self,number):
        sleep(15+random.randint(0,10000)/1000)
        self.driver.back()
        sleep(15+random.randint(0,10000)/1000)

        self.keyboard.clickAPoint((3,198), (537,1047))  
        
        sleepseconds = 20
        sleep(sleepseconds+random.randint(0,10000)/1000)
        for iter in range(number):
            self.driverSwipe.SwipeUp()
            sleep(sleepseconds+random.randint(0,5000)/1000)
            self.currentcount+=1
            if(self.currentcount>self.basecount):
                break
            
        #sleep(sleepseconds+random.randint(0,10000)/1000)        
        print()
        

        
    def actAutomation(self):
        while(True):
            try:
                self.init_driver()
                self.watchvedios(self.basecount)
                self.tearDown()
                break
            except Exception:
                print('phone session terminated!')
                traceback.print_exc()  
                if not self.driver :
                    self.tearDown()  
                #qutoutiao.tearDown()        

if __name__ == '__main__':    

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    devices = [('DU2YYB14CL003271','4.4.2')]
    #devices = [('SAL0217A28001753','9')]
    #devices = [('A7QDU18420000828','9')]  
    devices = [('SAL0217A28001753','9.1')]     
    for (deviceName,version) in devices:
        quanmin = QuanMinAutomation(deviceName,version)
        t = threading.Thread(target=quanmin.actAutomation(), args=(deviceName,version,))
        t.start()
        sleep(random.randint(0, 10000)/1000)