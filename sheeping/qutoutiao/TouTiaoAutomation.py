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
from qutoutiao import key_codes
from qutoutiao import DriverSwipe
from qutoutiao import Utils
from qutoutiao import keyboards
import traceback
from qutoutiao.baseoperation import BaseOperation 
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

class  TouTiaoAutomation(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        super(TouTiaoAutomation,self).__init__()
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
        
        desired_caps['appPackage'] = 'com.ss.android.article.lite'
        
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        
        desired_caps['appActivity'] = 'com.ss.android.article.lite.activity.SplashActivity'
        
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
        #point = exists(Template(r"..\imagesrc\tpl1580907022260.png",threshold=0.8))
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View[3]")
        if not element:
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.webkit.WebView/android.webkit.WebView/android.view.View/android.app.Dialog/android.view.View/android.view.View[2]/android.view.View[3]")
        if element: 
            element.click()
            sleep(15 +random.randint(0,5000)/1000)
            
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@text='关闭广告']")
            if element:
                element.click()
            else:
                self.driver.back()        
        else:
            self.driver.back() 
    def doTask(self):
        #keyevent("BACK")
        sleepseconds = 5    
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        sleep(sleepseconds+random.randint(0,5000)/1000)
        self.driver.back()
        
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.ImageView[@resource-id='com.ss.android.article.lite:id/aq1']")
        if element:
            element.click()
            sleep(2+random.randint(0,3000)/1000)
            for i in range(5) :
                element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@text='搜索']")
                if element:
                    element.click()
                    sleep(2+random.randint(0,3000)/1000)
                    self.driver.back()
        
            self.driver.back()
        #go to task
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TabWidget/android.widget.RelativeLayout[4]/android.widget.ImageView")
        if element:
            element.click()
            
        self.watchVedio()
        
        #open ball
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='treasure-box-enable-1.da338c08']")
        x1 = element.location['x']
        y1 = element.location['y'] 
        action=TouchAction(self.driver).long_press(element)


        # 结果傻逼了，正常的人类停顿了一下，回过神来发现，卧槽，滑过了,然后开始反向滑动
        action=action.wait(600)
        y1=y1+3
        action=action.move_to(x=x1, y=y1)  # 先移动去一点
        y1=y1+3
        action=action.move_to(x=x1, y=y1)  # 先移动去一点
        y1=y1+3
        action=action.move_to(x=x1, y=y1)  # 先移动去一点

        # 小范围震荡一下，进一步迷惑极验后台，这一步可以极大地提高成功率
        action=action.wait(300)
        y1=y1+3
        action=action.move_to(x=x1, y=y1)  # 先移动去一点
        action=action.wait(400)
        y1=y1+3
        action=action.move_to(x=x1, y=y1) # 再退回来，模仿人的行为习惯

        action=action.wait(600)  # 0.6秒后释放鼠标
        action.release().perform()
        
        if element:
            element.click()
            sleep(1+random.randint(0,2000)/1000)
            self.watchVedio()
        

       ##走路
        sleep(1+random.randint(0,1000)/1000)
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='走路赚钱']/../android.view.View[@text='去查看']")
        if element:
            element.click()
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'领取')]")
            if element:
                element.click()
                self.driver.back()
        ##吃饭
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='吃饭补贴']/../android.view.View[@text='去查看']")
        if element:
            element.click()
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'领取')]")
            if element:
                element.click()
                self.watchVedio() 
                self.driver.back()  
         ##睡觉赚钱
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='睡觉赚钱']/../android.view.View[@text='去查看']")
        if element:
            element.click()
            sleep(2+random.randint(0,2000)/1000)
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='我睡醒了']")
            if element:
                element.click()
                sleep(2+random.randint(0,2000)/1000)
                element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'领取')]")
                if element:
                    element.click()
                    self.watchVedio()
                
                self.driver.back()  
            
        #go to sleep
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.Image[@text='睡觉赚钱']/../android.view.View[@text='去查看']")
        if element:
            element.click()
            sleep(2+random.randint(0,2000)/1000)
            element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@text='我要睡了']")
            if element:
                element.click()  
                self.driver.back()          
        
        self.driverSwipe.SwipeUp()
        sleep(1+random.randint(0,1000)/1000)
        self.driverSwipe.SwipeUp()
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View/android.view.View[13]/android.widget.Button[3]")
        if element:
            element.click()
            for i in range(5) :
                element = self.find_element_by_xpath_without_exception(self.driver, "//android.widget.TextView[@text='搜索']")
                if element:
                    element.click()
                    sleep(2+random.randint(0,3000)/1000)
                    self.driver.back()
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
            object = TouTiaoAutomation(deviceName,version)
            object.actAutomation()
            #Always execution 
            break  
        except Exception:    
            print('phone session terminated!')
            print(sys.exc_info()) 

    end = time.time()
    print('Task %s runs %0.2f seconds.' % (deviceName, (end - start)))  
    
class AutomationThread (threading.Thread):
    def __init__(self, device):
        threading.Thread.__init__(self)
        self.device = device 
    def run(self):
        SheepingDevices(self.device)
    
if __name__ == '__main__':    

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    devices = [('DU2YYB14CL003271','4.4.2')]
    devices = [('SAL0217A28001753','9.1')]
    devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X  
    devices = [('ORL1193020723','9.1.1')]#Cupai 9
       
    devices = [('A7QDU18420000828','9'),('SAL0217A28001753','9')]  
    #devices = [('SAL0217A28001753','9.1')]   
    
    #devices = [('TUKDU18108020017','9')] 
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
    SheepingDevices(devices[0])
#     p = Pool(len(devices))
    autothreads=[]
    for device in devices:
        runThread = AutomationThread(device)
        runThread.start()
        autothreads.append(runThread)
        time.sleep(50)                
    for td in autothreads:
        td.join()   
    print('Waiting for all subprocesses done...')
#     p.close()
#     p.join() 