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

class  HuoShanAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        #�ռ����� ���ֻ�--����--������ѡ��---ָ��λ��-���������ֶ������Ǹ�webviewԪ�أ��ֻ����Ϸ�����ʾ��x��y������ 
        
        #adb not found
        #netstat -ano|findstr '5037'
        #tasklist |findstr '15828'
        
        # adb devices
        # adb shell pm list package # adb shell pm list package -3 -f 
        # adb logcat -c // clear logs
        # adb logcat ActivityManager:I *:s
        
        self.deviceName=deviceName
        self.version=version
        self.username=username
        self.password=password
        
        self.driver = None
        self.basecount = 10
        self.currentcount = 0  
        self.luckyDrawed = False     
        
        
#         
#         self.username = username
#         self.password = password
    def init_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = self.version
        desired_caps['deviceName'] = self.deviceName
        desired_caps['appPackage'] = 'com.ss.android.ugc.livelite'
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.ss.android.ugc.live.main.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = keyboards.KeyBoards(self.driver)
     
     
    def tearDown(self):
        self.driver.quit()        
    def sign(self):
        #sigin  
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="红包"]')
        if element:
            element.click()
            
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.Image[@text="开宝箱得金币"]')
            if element:
                element.click()
                self.driver.back()
            
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="去签到"]')
            #self.find_element_by_id_without_exception(self.driver,'//android.view.View[contains(@text,"去签到")]')
            if element:
                element.click()
                self.driver.back()

        if self.luckyDrawed:
            return              
        #lucky draw
        #WebPage
        return
        self.driverSwipe.SwipeUp() 
        sleep(1+random.randint(0,10000)/1000)        
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="幸运大转盘"]')
        if element:
            element.click()  
            for iter in range(7):
                if random.randint(0,100) % 5 ==0:
                    self.driver.back()
                    break      
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="明天再来"]')
                if element:
                    self.luckyDrawed = True
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
                    #close
                    element = self.find_element_by_xpath_without_exception(self.driver,'//android.webkit.WebView/android.view.View[7]/android.view.View[2]/android.view.View/android.view.View')   
                    if element:
                        element.click()
                        continue   
   
        print()        
    def watchvedios(self,number):
        sleepseconds = 5
        if random.randint(0,100)%2 == 0:
            sleep(sleepseconds+random.randint(0,10000)/1000)
            self.driver.back()        
        if random.randint(0,100)%2 == 0:
            sleep(sleepseconds+random.randint(0,10000)/1000)
            self.driver.back()       
        if random.randint(0,100)%2 == 0:
            sleep(sleepseconds+random.randint(0,10000)/1000)
            self.driver.back()   
        #self.keyboard.clickAPoint((248,534), (484,804))  
        
        sleepseconds = 5
        sleep(sleepseconds+random.randint(0,5000)/1000)
        
        for iter in range(number):
            self.driverSwipe.SwipeUp()
            
            #sometimes pause
            if random.randint(0,1024) % 17 ==0:
                sleep(sleepseconds+80+random.randint(0,15000)/1000)
            else:
                sleep(sleepseconds+random.randint(0,15000)/1000)
            
            #like the vedio
            if random.randint(0,125) % 3 ==0:
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.ImageView')
                if element:
                    element.click()
                    sleep(random.randint(0,3000)/1000)
                    
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[8]')
            if element:
                element.click()
                sleep(random.randint(0,3000)/1000)
                
            self.currentcount+=1
            if(self.currentcount>self.basecount):
                break

        

        
    def actAutomation(self):
        crashCount = 0
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
                print('Tash %s carsh %s times!' % (self.deviceName,crashCount))
                traceback.print_exc()
                if self.driver :
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
            object = HuoShanAutomation(deviceName,version)
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
    #devices = [('ORL1193020723','9.1.1')]#Cupai 9
    #devices = [('PBV0216C02008555','8.0')] #huawei P9
    #devices = [('UEUDU17919005255','8.1.1')] #huawei Honor 6X
    #devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X 
    
    devices = [('A7QDU18420000828','9')]  
    #devices = [('SAL0217A28001753','9.1')]
       
      
#     for (deviceName,version) in devices:
#         kuaishou = KuaiShouAutomation(deviceName,version)
#         t = threading.Thread(target=kuaishou.actAutomation(), args=(deviceName,version,))
#         t.start()
#         sleep(random.randint(0, 10))
        
    print('Parent process %s.' % os.getpid())
    p = Pool(len(devices))
    for device in devices:
        p.apply_async(SheepingDevices, args=(device,))
        time.sleep(100)                
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()        