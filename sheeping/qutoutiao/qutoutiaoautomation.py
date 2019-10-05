# coding: utf-8
from time import sleep
from appium import webdriver
import traceback
import re
import time
import os
import sys
import random
import threading
from qutoutiao import DriverSwipe
from qutoutiao.baseoperation import BaseOperation 
from qutoutiao import Utils
from qutoutiao import keyboards
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException



class QutoutiaoAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        # 空间坐标 打开手机--设置--开发者选项---指针位置-启动后，你手动触摸那个webview元素，手机的上方会显示（x，y）坐标 
        
        #adb not found
        #netstat -ano|findstr “5037”
        #tasklist |findstr “15828”
        #taskkill /pid 3172 /f
        # adb -s [devicename] shell set specific devices
        
        # adb devices
        # adb shell pm list package
        # adb logcat -c // clear logs
        # adb logcat ActivityManager:I *:s
        #aapt dump badging C:\Users\Administrator\Desktop\api\ff0602.apk

        
        self.deviceName = deviceName
        self.articleCount = 0
        self.vedioCount = 0
        self.username = username
        self.password = password
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
        desired_caps['appPackage'] = 'com.jifen.qukan'
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.jifen.qkbase.main.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = keyboards.KeyBoards(self.driver)
     
    def tearDown(self):
        self.driver.quit()


        

    def findWilliam(self):
        sleep(random.randint(0,5000)/1000)
        # go to me
        self.driver.find_element_by_id('com.jifen.qukan:id/mb').click()
        sleep(random.randint(0,5000)/1000)
        
        self.driver.find_elements_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView").get(0).send_keys(self.username)
        self.driver.find_elements_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView").get(1).send_keys(self.password)
        sleep(random.randint(0,5000)/1000)
        
        element = self.driver.find_element_by_xpath("//android.widget.Button[contains(text(),'{}')]".format('登录'))
        element.click()
        sleep(random.randint(0,5000)/1000)
        
    def logout(self):
        # go to me
        self.driver.find_element_by_id('com.jifen.qukan:id/mb').click()
        sleep(random.randint(0,5000)/1000)
        
        # go to setting
        while(True):
            sleep(random.randint(0,5000)/1000)
            self.driverSwipe.swipeDown()
            element = self.driver.find_element_by_xpath("//android.widget.TextView[contains(text(),'{}')]".format('设置'))
            if element:
                element.click()
                break

        # go to exit
        while(True):
            sleep(random.randint(0,5000)/1000)
            self.driverSwipe.swipeDown()
            element = self.driver.find_element_by_xpath("//android.widget.Button[contains(text(),'{}')]".format('退出登录'))
            if element:
                element.click()
                break
                
    def sign(self):
        
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.TextView[@text="领取"]')
        if element:
            element.click()
        
        sleep(random.randint(0,5000)/1000)
        # sign in
        self.keyboard.clickAPoint((648,2019), (864,2160))
#         element=self.find_element_by_id_without_exception(self.driver,'com.jifen.qukan:id/mc')
#         if element:
#             element.click()
            
        sleep(random.randint(0,5000)/1000)  
        #self.driverSwipe.AdbSwipeLeft()
        #sleep(random.randint(0,5000)/1000)  
        #self.driverSwipe.AdbSwipeLeft()      
        
    def readAArticle(self, comments):
        try:
            #
            for iter in range(random.randint(5,7)):
                sleep(10+random.randint(0,10000)/1000)
                self.driverSwipe.SwipeUpALittle()
                self.clickMe()
            
#             self.driver.find_element_by_id('com.jifen.qukan:id/b9e').click()
#             sleep(random.randint(0,5000)/1000)
#             self.driver.find_element_by_id('com.jifen.qukan:id/vw').send_keys(comments)
#             sleep(random.randint(0,5000)/1000)
#             self.driver.find_element_by_id('com.jifen.qukan:id/vz').click()
            
            self.articleCount+=1
        except Exception:
            print('read article exception')
            traceback.print_exc() 
            #self.driver.back()
            return
        
        self.driver.back()
        
        
#     def timeBonus(self):
#         try:
#             sleep(3+random.randint(0,5000)/1000)        
#             element = self.find_element_by_id_without_exception(self.driver,'com.jifen.qukan:id/a7q')
#             if element:
#                 element.click()
#             
#             sleep(3+random.randint(0,5000)/1000)
#             element = self.find_element_by_id_without_exception(self.driver,'com.jifen.qukan:id/a4d')
#             if element:
#                 element.click()
#                 
#         except Exception as e:
#             traceback.print_exc()            
#             return
    def clickMe(self):
        
        sleep(3+random.randint(0,5000)/1000)        
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView')
        if element:
            element.click()
        
            sleep(40+random.randint(0,5000)/1000)
            
            self.driver.back()
        
                             
    def headPageRefreshSwipeDown(self):
        # go to toutiao
        self.keyboard.clickAPoint((0,2019), (216,2160))

#         element=self.find_element_by_id_without_exception(self.driver, 'com.jifen.qukan:id/m9')
#         if element:
#             element.click()
        #self.timeBonus();
        times = random.randint(5,8)
        for inter in range(times):
            self.driverSwipe.SwipeUpALittle()
            sleep(random.randint(0,5000)/1000)
            #
        
    def readArticles(self, number):
                
        self.headPageRefreshSwipeDown()
        sleep(random.randint(0,5000)/1000)
        self.driverSwipe.SwipeLeft()
        
        
        for iter in range(number):            
            elements = self.driver.find_elements_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView")
            if len(elements) ==0:
                self.headPageRefreshSwipeDown()
                continue
            index = 0
            if len(elements)>1:
                index = random.randint(0,len(elements)-1)
            elements[index].click()
            self.readAArticle('14亿中国人，14亿护旗手')
            
            self.driver.back()
            #refresh
            self.headPageRefreshSwipeDown()
            
            self.currentcount+=1
            if(self.currentcount>2*self.basecount):
                break
        
        
    def watchVedios(self, number):
        # go to little vedio
        self.keyboard.clickAPoint((432,2019), (648,2160))

#         element=self.find_element_by_id_without_exception(self.driver, 'com.jifen.qukan:id/ma')
#         if element:
#             element.click()        
        sleep(20+random.randint(0,5000)/1000)
        self.vedioCount+=1
        for iter in range(number):
            self.driverSwipe.SwipeUp()
            self.clickMe()
            sleep(20+random.randint(0,5000)/1000)
            self.vedioCount+=1
            
            
            self.currentcount+=1
            if(self.currentcount>2*self.basecount):
                break            
            
        sleep(20+random.randint(0,5000)/1000)
            
        
        
    def actAutomation(self):
        while(True):
            try:
                self.init_driver()
                self.sign()
                self.watchVedios(self.basecount+random.randint(0,2))
                self.readArticles(self.basecount+random.randint(0,2))
                self.tearDown()
                break
#             except WebDriverException:
#                 break        
            except Exception:
                print('phone session terminated!')
                traceback.print_exc() 
                if not self.driver :
                    self.tearDown()   

if __name__ == '__main__':   
    devices = [('DU2YYB14CL003271','4.4.2')]#,('A7QDU18420000828','9'),('SAL0217A28001753','9')]     
    devices = [('SAL0217A28001753','9')]
    #devices = [('A7QDU18420000828','9')]
    for (deviceName,version) in devices:
        qutoutiao = QutoutiaoAutomation(deviceName,version)
        t = threading.Thread(target=qutoutiao.actAutomation(), args=())
        t.start()
        sleep(random.randint(0, 10))
        