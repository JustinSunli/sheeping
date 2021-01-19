from appium import webdriver
import time

# coding: utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from time import sleep
import logging
from appium import webdriver
import re
import time
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
from qutoutiao.BaseOperation import AutomationException 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.request import quote
from _ast import Raise

class  Contacts(BaseOperation):
    def __init__(self, deviceName='A7QDU18420000828',version='9',timerange=(0,24),username='18601793121', password='Initial0'):
        super(Contacts,self).__init__(deviceName,version,timerange,username,password)
        
        self.stat.deviceName = self.deviceName
        self.stat.AppName = self.__class__.__name__
        
    def init_driver(self):
        self.desired_caps['appPackage'] = 'com.android.contacts'        
        self.desired_caps['appActivity'] = 'com.android.contacts.activities.PeopleActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.initAfterDriver()
    def tearDown(self):
        super().tearDown()        
        self.driver.quit()
               
    def actAutomation(self):
        super().actAutomation()
        self.logger.info("Enter--------"+sys._getframe().f_code.co_name+"-------")                
        self.stat.startTime = time.time()
        crashCount=0
        while(True):
            try:
                self.init_driver()
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
                if crashCount > 3:
                    break                             

        self.stat.endTime = time.time()
        self.logger.info("GoOut--------"+sys._getframe().f_code.co_name+"-------")        
        
if __name__ == '__main__':    

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    #devices = [('DU2YYB14CL003271','4.4.2')]
    devices = [('PBV0216C02008555','8.0')] #huawei P9 
    #devices = [('ORL1193020723','9.1.1')]#Cupai 9
    devices = [('UEUDU17919005255','8.0.0')] #huawei Honor 6X 
    #devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X  
    
        

    #devices = [('A7QDU18420000828','9')]  
    #devices = [('SAL0217A28001753','9.1')]    
    for (deviceName,version) in devices:
        contact = Contacts(deviceName,version,(0,24))  
          
        t = threading.Thread(target=contact.actAutomation())
        t.start()
        sleep(random.randint(0, 10))




#desired_caps = {}
#desired_caps['platformName'] = 'Android'
#desired_caps['platformVersion'] = '5.1.1'
#desired_caps['deviceName'] = 'emulator-5554'
#desired_caps['appPackage'] = 'com.android.contacts'
#desired_caps['appActivity'] = 'com.android.contacts.activities.PeopleActivity'
#desired_caps['unicodeKeyboard'] = True
#desired_caps['resetKeyboard'] = True
#driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
#driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
#driver.find_element_by_class_name("android.widget.EditText").send_keys("王彬")
#driver.find_element_by_xpath("//*[contains(@text,'姓名拼音')]").send_keys("wangbin")
#driver.find_element_by_xpath("//*[contains(@text,'昵称')]").send_keys("wb")
#driver.find_element_by_id("com.android.contacts:id/change_button").click()
#
#driver.find_element_by_id("android:id/text1").click()
## driver.find_element_by_id("com.android.documentsui:id/icon_mime").click()
#driver.find_element_by_class_name("android.widget.ImageView").click()
#driver.find_element_by_id("com.android.gallery:id/save").click()
#driver.find_element_by_xpath("//*[contains(@text,'电话')]").send_keys("17835344021")
## driver.swipe(804,1536,136,397)
#time.sleep(2)
#driver.find_element_by_xpath("//*[contains(@text,'电子邮件')]").send_keys("1874476942@qq.com")
#time.sleep(1)
#
#
#driver.swipe(804,1597,136,397)
#
#time.sleep(2)
#driver.find_element_by_xpath("//*[contains(@text,'地址')]").send_keys("山西省运城市")
#time.sleep(2)
#driver.find_element_by_xpath("//*[contains(@text,'公司')]").send_keys("北京忧思安")
#time.sleep(2)
#driver.find_element_by_xpath("//*[contains(@text,'职务')]").send_keys("测试项目主任的学生")
#time.sleep(2)
#driver.find_element_by_xpath("//*[contains(@text,'备注')]").send_keys("疯狂的菠萝")
#driver.swipe(804,1597,136,397)
#time.sleep(2)
#driver.find_element_by_xpath("//*[contains(@text,'聊天工具')]").send_keys("微信")
#driver.swipe(804,1597,136,397)
#time.sleep(2)
#driver.find_element_by_xpath("//*[contains(@text,'SIP')]").send_keys("111")
#time.sleep(1)
#driver.find_element_by_xpath("//*[contains(@text,'网站')]").send_keys("https://www.cnblogs.com/daiju123/")
#driver.find_element_by_class_name("android.widget.ImageButton").click()