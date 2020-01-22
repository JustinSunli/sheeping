# coding: utf-8
from multiprocessing import Pool
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

class  MiduAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        super(MiduAutomation,self).__init__()
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
        self.basecount = 20
        self.currentcount = 0  
        self.driver = None   
        
        self.luckyDrawed = False     
        
#         
#         self.username = username
#         self.password = password
    def init_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = self.version
        desired_caps['deviceName'] = self.deviceName
        desired_caps['appPackage'] = 'com.lechuan.mdwz'
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.lechuan.mdwz.ui.activity.WelcomeActivity'
        #desired_caps['appActivity'] = 'com.squareup.leakcanary.internal.DisplayLeakActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = keyboards.KeyBoards(self.driver)
     
     
    def tearDown(self):
        self.driver.quit()        
    def sign(self):        
        #if self.isFirst:
        sleep(self.sleepseconds+random.randint(0,10000)/1000)
        self.driver.back()   
        sleep(self.sleepseconds+random.randint(0,10000)/1000)
        self.driver.back()             
        sleep(self.sleepseconds+random.randint(0,10000)/1000)
        self.driver.back()
        #    self.isFirst = False
        self.crack()
        #福利
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.RadioGroup/android.widget.RadioButton[4]')
        if element:
            element.click()
        else:
            self.driver.back()
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="确认退出"]')
            if element:
                element.click() 
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.RadioGroup/android.widget.RadioButton[4]')
                if element:
                    element.click()
                else:
                    return   
        if self.isFirst:                             
            sleep(self.sleepseconds+random.randint(0,10000)/1000)
            self.driver.back()
            sleep(self.sleepseconds+random.randint(0,10000)/1000)
            self.driver.back()   
            self.isFirst=False                 
        #sign                    
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="签到"]')
        if element:
            element.click()   
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.Button[@text="看视频领金币"]')
            if element:
                element.click() 
                #watch ads
                sleep(35+random.randint(0,5000)/1000)  
                self.closeAddsWindow()   
            else:
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="放弃额外奖励"]')
                if element:
                    element.click() 
                  
        if self.luckyDrawed:
            return                                
        #lucky draw
        self.driverSwipe.SwipeUp() 
        sleep(1+random.randint(0,10000)/1000)
        self.driverSwipe.SwipeUp() 
        sleep(1+random.randint(0,10000)/1000)        
        self.driverSwipe.SwipeUp() 
        sleep(1+random.randint(0,10000)/1000)         
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="幸运大转盘"]')
        if element:
            element.click()  
            for iter in range(7):
#                 if random.randint(0,100) % 5 ==0:
#                     self.driver.back()
#                     break      
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="明天再来"]')
                if element:
                    self.luckyDrawed = True
                    self.driver.back()
                    break                          
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="开始抽奖"]')
                if element:
                    element.click()  
                    sleep(3+random.randint(0,2000)/1000) 
                    #close
                    element = self.find_element_by_xpath_without_exception(self.driver,'//android.webkit.WebView/android.view.View[7]/android.view.View[2]/android.view.View/android.view.View')   
                    if element:
                        element.click()
                        continue                        
                    
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="看视频抽大奖"]')
                if element:
                    element.click() 
                    #watch ads
                    sleep(35+random.randint(0,5000)/1000) 
                    self.closeAddsWindow() 
                    sleep(3+random.randint(0,2000)/1000)
#                     for i in range(30):
#                         element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="点击重播"]')
#                         if element:
#                             self.driver.back()
#                             break
#                         sleep(3+random.randint(0,2000)/1000)                     
                    #close
                    element = self.find_element_by_xpath_without_exception(self.driver,'//android.webkit.WebView/android.view.View[7]/android.view.View[2]/android.view.View/android.view.View')   
                    if element:
                        element.click()
                        continue   
                                     

                        
    def closeAddsWindow(self):
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'关闭广告')]")
        if element:
            element.click()
            return
        element = self.find_element_by_id_without_exception(self.driver, 'com.lechuan.mdwz:id/tt_video_ad_close')
        if element:
            element.click()
        else:
            #do not know how long the ads
            for i in range(20):
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="点击重播"]')
                if element:
                    self.driver.back()
                    return
                sleep(3+random.randint(0,2000)/1000)
            
            
            #
            self.width=self.driver.get_window_size().get('width')
            self.height=self.driver.get_window_size().get('height')
            if self.width ==720 and self.height==1366:
                #coolpad
                self.keyboard.clickAAbsolutePoint((45,95),(94,141))
            else:
                #Tencent ads union
                self.keyboard.clickAPoint((60,45), (150,135))                      
            
            #the last try
            self.driver.back()   
    def watchvedios(self,number):  
        #if self.isFirst:
        sleep(self.sleepseconds+random.randint(0,10000)/1000)
        self.driver.back()        
        sleep(self.sleepseconds+random.randint(0,10000)/1000)
        self.driver.back()
        #self.isFirst = False            
        
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.RadioGroup/android.widget.RadioButton[3]')
        if element:
            element.click()
        else:
            return
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="继续阅读"]')
        if element:
            element.click() 
        else:
            return  
        
        #erase menu page
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="夜间"]')
        if element:
            element.click() 
            self.driver.back()
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="白天"]')
        if element: 
            self.driver.back()                     
            
        sleepseconds = 9
        for iter in range(number):
            #sometimes pause
            if random.randint(0,1024) % 7 ==0:
                sleep(sleepseconds+30+random.randint(0,5000)/1000)
            else:
                sleep(sleepseconds+random.randint(0,3000)/1000)
               
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="立即翻倍"]')
            if element:
                element.click() 
                #watch ads
                sleep(40+random.randint(0,5000)/1000)  
                self.closeAddsWindow()
                sleep(1+random.randint(0,2000)/1000)                   

            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="这本书的读者都在看"]')
            if element:
                elements = self.find_elements_by_xpath_without_exception(self.driver,'//android.support.v7.widget.RecyclerView/android.view.ViewGroup')
                index = random.randint(0,len(elements)-1)
                element = elements[index]
                element.click()
                
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="加入书架"]')
                if element:
                    element.click()
                
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="立即阅读"]')
                if element:
                    element.click()
                    sleep(1+random.randint(0,2000)/1000)
                     
            if random.randint(0,100) % 2 ==0:
                self.keyboard.clickAPoint((945,174), (1045,206))  
            else:
                self.keyboard.clickAPoint((945,174), (1045,206))
                #self.keyboard.clickAPoint((945,1900), (1045,1950))

        
        self.driver.back()    
        self.driver.back()
        self.driver.back()
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="确认退出"]')
        if element:
            element.click()         

    def tiantianFenHong(self):
        if not self.isFirst:
            return
        
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.RadioGroup/android.widget.RadioButton[5]')
        if element:
            element.click()
        else:
            return  
        
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="天天分红"]')
        if element:
            element.click() 
            sleep(3+random.randint(0,2000)/1000)
            self.driver.back()              
        
        self.isFirst = False
        
    def actAutomation(self):
        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.sign()
                self.tiantianFenHong()
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
    
def SheepingDevices(device):
    (deviceName,version) = device    
    print('Run task %s (%s)...' % (deviceName, os.getpid()))
    start = time.time()
    while(True):
        try:
            object = MiduAutomation(deviceName,version)
            object.actAutomation()
            #Always execution 
            break  
        except Exception:    
            print('phone session terminated!')
            print(sys.exc_info()) 

    end = time.time()
    print('Task %s runs %0.2f seconds.' % (deviceName, (end - start)))               
                    
if __name__ == '__main__':   
    devices = [('ORL1193020723','9.1.1'),('PBV0216C02008555','8.0'),('UEUDU17919005255','8.1.1'),('UEU4C16B16004079','8.1.1.1')]
    devices = [('ORL1193020723','9.1.1')]#Cupai 9
    #devices = [('PBV0216C02008555','8.0')] #huawei P9
    #devices = [('UEUDU17919005255','8.1.1')] #huawei Honor 6X
    #devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X 
    devices = [('A7QDU18420000828','9')]  
    #devices = [('SAL0217A28001753','9.1')]
       
      
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
            
    print('Parent process %s.' % os.getpid())
    p = Pool(len(devices))
    for device in devices:
        p.apply_async(SheepingDevices, args=(device,))
        time.sleep(50)                
    print('Waiting for all subprocesses done...')
    p.close()
    p.join() 