'''
Created on 2020年2月4日

@author: huang
'''
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
from multiprocessing import Pool
from airtest.core.api import *
from airtest.cli.parser import cli_setup


#assii unicode
from urllib.request import quote

class  XimalayaAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        super(XimalayaAutomation,self).__init__()
        #�ռ����� ���ֻ�--����--������ѡ��---ָ��λ��-���������ֶ������Ǹ�webviewԪ�أ��ֻ����Ϸ�����ʾ��x��y������ 
        
        #adb not found
        #netstat -ano|findstr '5037'
        #tasklist |findstr '15828'
        
        # adb devices
        # adb shell pm list package # adb shell pm list package -3 -f 
        # adb logcat -c // clear logs
        # adb logcat ActivityManager:I *:s
        
        #driver.startActivity("com.kuaihuoyun.freight", ".KDLaunch");
#

        self.deviceName=deviceName
        self.version=version
        self.username=username
        self.password=password
        self.driver = None
          
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
        
        desired_caps['appPackage'] = 'com.ximalaya.ting.lite'
        
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        
        desired_caps['appActivity'] = 'com.ximalaya.ting.android.host.activity.WelComeActivity'
        
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = keyboards.KeyBoards(self.driver)
        
#         if not cli_setup():
#             auto_setup(__file__, logdir=True, devices=[
#                     "Android://127.0.0.1:5037/"+self.deviceName,
#             ])
     
    def tearDown(self):
        self.driver.quit()    
    
    def watchVedio(self):
        point = exists(Template(r"..\imagesrc\tpl1580798064597.png",threshold=0.8))
        if point: 
            touch(point)
            sleep(15 +random.randint(0,5000)/1000)
            
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@text='关闭广告']")
            if element:
                element.click()
            else:
                self.driver.back()        
       
    def doTask(self):
        #keyevent("BACK")
        sleepseconds = 5    
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        
        
        #go to fuli
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.RadioButton[@text='福利']")
        if element:
            element.click()#else: return            
        
        #double sign on bonus    
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@resource-id='com.ximalaya.ting.lite:id/main_tv_coin_earn_more']")
        if element:
            element.click()
            sleep(30+random.randint(0,3000)/1000)
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.ImageView[@resource-id='com.ximalaya.ting.lite:id/tt_video_ad_close']")
            if element:
                element.click()
                sleep(3+random.randint(0,2000)/1000)
                self.driver.back()
        #领取金币                    
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Button[@text='领取金币']")
        if element:
            element.click()
            sleep(5+random.randint(0,3000)/1000)
            self.driver.back()
        
        #bubbles money
        elements = self.find_elements_by_xpath_without_exception(self.driver,"//android.webkit.WebView[@text='福利中心']/android.view.View/android.view.View[2]/*")  
        number=len(elements)
        for iter in range(number-4):             
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.webkit.WebView[@text='福利中心']/android.view.View/android.view.View[2]/android.view.View[3]")
            if element:
                element.click()
                sleep(5+random.randint(0,2000)/1000)
                self.driver.back()    
            
            
        self.driverSwipe.SwipeUp()
        
        #to my tab
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.RadioButton[@text='我的']")
        if element:
            element.click()
            sleep(1)
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.RadioButton[@text='福利']")
            if element:
                element.click()
        
        #interesting vedio
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Button[@text='去完成']")
        if element:
            element.click()
            sleep(30+random.randint(0,3000)/1000)
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.ImageView[@resource-id='com.ximalaya.ting.lite:id/tt_video_ad_close']")
            if element:
                element.click()
                sleep(4+random.randint(0,2000)/1000)
                self.driver.back()
        
       
        #aapt dump badging
        #choose one
        #sleep(10+random.randint(0,5000)/1000)
        #self.keyboard.clickAPoint((0,205), (537,1159))
        
                  
#     def closeAddsWindow(self):
#         element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'关闭广告')]")
#         if element:
#             element.click()
#             return
#         
#         element = self.find_element_by_id_without_exception(self.driver, 'com.yuncheapp.android.pearl:id/tt_video_ad_close_layout')
#         if element:
#             element.click()
#         else:
#             self.driver.back()
#             return   
                       
    def actAutomation(self):
        self.stat.startTime = time.time()

        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.doTask()
#                 self.GotoMeAndView()
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
        self.stat.endTime = time.time()
                                                      
                      
def SheepingDevices(device):
    (deviceName,version) = device    
    print('Run task %s (%s)...' % (deviceName, os.getpid()))
    start = time.time()
    while(True):
        try:
            object = XimalayaAutomation(deviceName,version)
            object.actAutomation()
            #Always execution 
            break  
        except Exception:    
            print('phone session terminated!')
            print(sys.exc_info()) 

    end = time.time()
    print('Task %s runs %0.2f seconds.' % (deviceName, (end - start)))  
    
if __name__ == '__main__':    

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    devices = [('DU2YYB14CL003271','4.4.2')]
    devices = [('SAL0217A28001753','9.1')]
    devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X  
    devices = [('ORL1193020723','9.1.1')]#Cupai 9
       
    devices = [('A7QDU18420000828','9')]  
    devices = [('SAL0217A28001753','9.1')] 
    devices = [('TUKDU18108020017','9')]     
#     readDeviceId = list(os.popen('adb devices').readlines())
#     devices=[]
#     for outputline in readDeviceId:
#         codes = re.findall(r'(^\w*)\t', outputline)
#         if len(codes)!=0:
#             deviceName=codes[0]
#              
# #             versionoutput=list(os.popen('adb -s %s shell  getprop ro.build.version.release' % (deviceName)).readlines())
# #             version = re.findall(r'(^.*)\n', versionoutput[0])[0]
# #             devices.append((deviceName,version))
#             devices.append((deviceName,""))
#             
#     print('Parent process %s.' % os.getpid())
    p = Pool(len(devices))
    for device in devices:
        p.apply_async(SheepingDevices, args=(device,))
        time.sleep(50)                
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
