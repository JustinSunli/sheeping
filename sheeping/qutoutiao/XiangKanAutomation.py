# coding: utf-8
# 验证身份证
from time import sleep
from appium import webdriver
import traceback
import re
import time
import os
import sys
import random
import threading
from multiprocessing import Pool

from qutoutiao import DriverSwipe
from qutoutiao.BaseOperation import BaseOperation 
from qutoutiao import Utils
from qutoutiao import KeyBoards
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException



class XiangKanAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        super(XiangKanAutomation,self).__init__()
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

        self.basecount = 40
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
        desired_caps['appPackage'] = 'com.xiangkan.android'
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 1000 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.bikan.reading.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = KeyBoards.KeyBoards(self.driver)
     
    def tearDown(self):
        self.driver.quit()
                
    def sign(self):
#         sleepseconds=5
#         sleep(sleepseconds+random.randint(0,5000)/1000)
#         self.driver.back()
#         sleep(sleepseconds+random.randint(0,5000)/1000)
#         self.driver.back()        
#         sleep(sleepseconds+random.randint(0,5000)/1000)
#         self.driver.back()                   
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="签到"]')
        if element:
            element.click()
            sleep(random.randint(0,3000)/1000)
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="领取奖励"]')
            if element:
                element.click()            
        
        sleep(random.randint(0,5000)/1000)
        
    def readAArticle(self):
        try:
            #
            for iter in range(random.randint(20,29)):
            #for iter in range(random.randint(5,9)):
                sleep(5+random.randint(0,5000)/1000)
                self.driverSwipe.SwipeUpALittle()
                self.clickMe()
                
            self.driver.back()           
            self.articleCount+=1
        except Exception:
            traceback.print_exc() 
            return
        
        self.driver.back()
        
    def clickMe(self):
        sleep(1+random.randint(0,2000)/1000)
        element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.ImageView[@resource-id='com.xiangkan.android:id/fudai_icon']")
        if element:
            element.click()
            sleep(1+random.randint(0,2000)/1000)

        sleep(3+random.randint(0,5000)/1000)        
        element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='继续阅读']")
        if element:
            element.click()
            sleep(1+random.randint(0,2000)/1000)
                             
    def headPageRefreshSwipeDown(self):
        #Go to header page
        sleep(10+random.randint(0,5000)/1000) 
        #com.xiangkan.android:id/tv_tab_title
        try:
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='首页']")
            if element:
                element.click() 
        except NoSuchElementException:
            self.driver.back()
            element = self.find_element_by_xpath_without_exception(self.driver,"//android.widget.TextView[@text='首页']")
            if element:
                element.click()                 
        #
        times = random.randint(2,6)
        for inter in range(times):
            self.driverSwipe.SwipeUpALittle()
            sleep(random.randint(500,3000)/1000)
        
    def readArticles(self, number):
        sleep(10+random.randint(0,5000)/1000)                
        self.headPageRefreshSwipeDown()
        sleep(random.randint(0,5000)/1000)
        
        for iter in range(number): 
            self.clickMe()           
            elements = self.driver.find_elements_by_xpath("//androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView")
            if len(elements) ==0:
                self.clickMe()
                self.headPageRefreshSwipeDown()
                continue
            if len(elements) <= 1:
                continue
            
            index = 0
            if len(elements) > 1:
                index = random.randint(1,len(elements)-1)
            elements[index].click()
            
            self.readAArticle()
            #self.driver.back()
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
        sleepseconds = 5
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.vedioCount+=1
        for iter in range(number):
            self.driverSwipe.SwipeUp()
            self.clickMe()
            
                        #sometimes pause
            if random.randint(0,1024) % 11 ==0:
                sleep(sleepseconds+80+random.randint(0,5000)/1000)
            else:
                sleep(sleepseconds+random.randint(0,5000)/1000)
            self.vedioCount+=1
            
            #like the vedio
            if random.randint(0,125) % 3 ==0:
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView')
                if element:
                    element.click()            
                    sleep(random.randint(0,15000)/1000) 
                    
            self.currentcount+=1
            if(self.currentcount>2*self.basecount):
                break            
            
        sleep(20+random.randint(0,5000)/1000)
            
        
        
    def actAutomation(self):
        crashCount=0
        while(True):
            try:
                self.init_driver()
                self.sign()
                #self.watchVedios(random.randint(0,3))
                self.readArticles(self.basecount+random.randint(0,2))
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

def SheepingDevices(device):
    (deviceName,version) = device    
    print('Run task %s (%s)...' % (deviceName, os.getpid()))
    start = time.time()
    while(True):
        try:
            object = XiangKanAutomation(deviceName,version)
            object.actAutomation()
            #Always execution 
            break  
        except Exception:    
            print('phone session terminated!')
            print(sys.exc_info()) 

    end = time.time()
    print('Task %s runs %0.2f seconds.' % (deviceName, (end - start)))    

if __name__ == '__main__':   
    devices = [('DU2YYB14CL003271','4.4.2')]#,('A7QDU18420000828','9'),('SAL0217A28001753','9')]     
    devices = [('SAL0217A28001753','9')]
    devices = [('A7QDU18420000828','9')]
    devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X 
    
    readDeviceId = list(os.popen('adb devices').readlines())
    devices=[]
    for outputline in readDeviceId:
        codes = re.findall(r'(^\w*)\t', outputline)
        if len(codes)!=0:
            deviceName=codes[0]
             
#             versionoutput=list(os.popen('adb -s %s shell  getprop ro.build.version.release' % (deviceName)).readlines())
#             version = re.findall(r'(^.*)\n', versionoutput[0])[0]
#             devices.append((deviceName,version))
            devices.append((deviceName,""))
            
    print('Parent process %s.' % os.getpid())
    p = Pool(len(devices))
    for device in devices:
        p.apply_async(SheepingDevices, args=(device,))
        time.sleep(50)                
    print('Waiting for all subprocesses done...')
    p.close()
    p.join() 
        