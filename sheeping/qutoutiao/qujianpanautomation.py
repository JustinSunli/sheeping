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
from qutoutiao.baseoperation import AutomationException 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from multiprocessing import Pool
from selenium.webdriver import ActionChains
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


#assii unicode
from urllib.request import quote
from _ast import Raise

class  QujianpanAutomation(BaseOperation):
    def findTheGabageNameAndDoSort(self,garbageName):
        #element = self.find_element_by_id_without_exception(self.driver, "garbageName")
        #garbageName=''
        gtype = None 
        if self.gabageDict.get(garbageName):
            gtype = self.gabageDict[garbageName]
        else:    
            try:
                quotename = quote(garbageName)                        
                url = 'http://api.choviwu.top/garbage/getGarbage?garbageName={}'.format(quotename)
                req=urllib.request.urlopen(url)
                result=req.read()
                result = json.loads(result)
                gtype = result['data'][0]['gtype']
            except:
                gtype='干垃圾'

        fromelement = self.find_element_by_id_without_exception(self.driver, 'garbageImg')
        toelement = None
        if  gtype == '湿垃圾':
            #move to wet gabage
            toelement = self.find_element_by_id_without_exception(self.driver, 'garbageBlueCon')
            print
        elif gtype == '可回收':
            #move to recycle
            toelement = self.find_element_by_id_without_exception(self.driver, 'garbageGreenCon')
            print
        elif gtype == '有害垃圾':
            #move to harmful
            toelement = self.find_element_by_id_without_exception(self.driver, 'garbageRedCon')
            print
        elif gtype == '干垃圾':
            #move to dry
            toelement = self.find_element_by_id_without_exception(self.driver, 'garbageGrayCon')
            print
        else:
            toelement = self.find_element_by_id_without_exception(self.driver, 'garbageGrayCon')
            print
        
        self.driver.drag_and_drop(fromelement, toelement)
        
        return (garbageName,gtype)

    def gotoGameGabageSort(self):
        #go to me tab
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[3]")
        if element:      
            element.click()
            
        #refuse to ads
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivChaiClose')
        if element:
            element.click() 
            
        #self.driverSwipe.SwipeUp() 
        sleep(10+random.randint(0,5000)/1000)
  
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="分垃圾赚金币"]/../android.widget.TextView[@text="试玩"]')
        if element:
            element.click()
            
        ele = self.find_element_by_id_without_exception(self.driver, 'tryGameBtn')
        if ele:
            ele.click()                    
            
#         elements = self.find_elements_by_xpath_without_exception(self.driver, "//android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.ImageView")
#         if len(elements)==0:
#             return False
#         iter=0
#         for element in elements:
#             if iter==0:
#                 iter+=1
#                 continue
#             
#             element.click()
#             ele = self.find_element_by_id_without_exception(self.driver, 'tryGameBtn')
#             if ele:
#                 ele.click()
#                 break
#             else:
#                 self.driver.back()
#                 #note ads vedio page
#                 element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']")
#                 if element:
#                     continue
#                 else:
#                     sleep(35)
#                     self.closeAddsWindow()
#                     #close gift window
#                     self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close').click()
#                     sleep(1+random.randint(0,3000)/1000)                    
                    
        with open('gabageconfig.json','r',encoding='utf-8') as fileR:   
            self.gabageDict.clear()
            self.gabageDict = json.load(fileR)
            #self.gabageDict = json.loads(self.gabageDict,encoding='utf-8')
            fileR.close()  
                                
        element = None
        iter=0
        while(iter < 4):
            iter+=1
            element = self.find_element_by_id_without_exception(self.driver, 'noTimesAlertBtn')
            if element:
                break

            #startBtn
            startbtn = True
            element = self.find_element_by_id_without_exception(self.driver, 'startBtn')
            if not element:
                element =self.find_element_by_id_without_exception(self.driver, 'continueBtn')
                startbtn = False 
            if(element == None):
                self.driver.back()
                return False
            
            element.click()
            #sleep(3+random.randint(0,3000)/1000)    
            while(True):
                (garbageName,gtype) = ('','')
                
                if startbtn:
                    fromPoint = self.util.centerPoint((387,894), (690,1197))
                    toPoint = self.util.centerPoint((375,1110), (705,1635))
                    self.keyboard.swip(fromPoint, toPoint)
                    startbtn=False
                
                element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@resource-id='garbageName']/android.view.View")
                if not element:
                    self.driver.back()
                    return False
                
                garbageName = element.text
            
                (garbageName,gtype) = self.findTheGabageNameAndDoSort(garbageName)
                
                #END correct
                element = self.find_element_by_id_without_exception(self.driver, 'watchResultBtn2')
                if element:
                    self.gabageDict[garbageName] = gtype
                    self.find_element_by_id_without_exception(self.driver, 'lastAnswerRightAlertClose').click()
                    #return True
                #end wrong
                element = self.find_element_by_id_without_exception(self.driver, 'watchResultBtn1')
                if element:
                    self.gabageDict[garbageName] = self.find_element_by_id_without_exception(self.driver, 'lastErrorGarbageType').text
                    self.find_element_by_id_without_exception(self.driver, 'lastAnswerErrorAlertClose').click()
                    #return True                
                
                element = self.find_element_by_id_without_exception(self.driver, 'coinDoubleBtn')
                if element:
                    element.click()
                    #all corrent
                    self.gabageDict[garbageName] = gtype
                    
                    sleep(40+random.randint(0,5000)/1000)
                    
                    #close ads window
                    self.closeAddsWindow()
                    #sleep(1+random.randint(0,3000)/1000)
                    
                    self.writeGabageDic()

                    #next question
                    self.find_element_by_id_without_exception(self.driver, 'nextQuestionBtn1').click()
                    
                else:
                    #shit wrong
                    gtype = self.find_element_by_id_without_exception(self.driver, 'errorGarbageType').text[0:3]
                    self.gabageDict[garbageName] = gtype
                    sleep(1+random.randint(0,3000)/1000)
                    
                    self.find_element_by_id_without_exception(self.driver, 'reLiveBtn').click()
                    sleep(1+random.randint(0,3000)/1000)
                    
                    #wait ads ends
                    sleep(40+random.randint(0,5000)/1000)
                    
                    #close ads window
                    self.closeAddsWindow()
                    #sleep(1+random.randint(0,3000)/1000)
                    
                    self.writeGabageDic()

                    self.find_element_by_id_without_exception(self.driver, 'reliveCoinAlertBtn').click()
                
            print()    
        
            print()
        return True
    
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
        super(QujianpanAutomation,self).__init__()
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
        
        self.gabageDict = {}
#         
#         self.username = username
#         self.password = password
    def init_driver(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = self.version
        desired_caps['deviceName'] = self.deviceName
        desired_caps['appPackage'] = 'com.qujianpan.client'
        desired_caps['dontStopAppOnReset'] = True  
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        
        desired_caps['ignoreUnimportantViews'] = True 
        desired_caps['disableAndroidWatchers'] = True  
        desired_caps['skipUnlock'] = True 
        desired_caps['skipLogcatCapture'] = True  
        desired_caps['skipServerInstallation'] = True  
        
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.qujianpan.client.ui.GuideActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = keyboards.KeyBoards(self.driver)
        
    def tearDown(self):
        self.driver.quit()


    def lookadsgetgifts(self):
        #WEBVIEW_com.qujianpan.client
        sleep(1+random.randint(0,3000)/1000)
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="领取"]')
        if element and element.is_displayed():
            element.click()

        while(True):
            #time gift
            
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@resource-id='header']/android.view.View[2]/android.view.View[2]")
            if element:
                element.click()

            #no times left
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@resource-id='popTimeRewardCover']/android.view.View[@resource-id='pop_notimes']/android.view.View[@resource-id='pop_konwBtn']")
            if element and element.is_displayed():
                element.click()
                break;

            sleep(1+random.randint(0,3000)/1000)
            #click ads
            element = self.find_element_by_id_without_exception(self.driver,'pop_timerStageBtn')
            if element:
                element.click()
            else:
                self.driver.back()
                continue
                
            sleep(35+random.randint(0,3000)/1000)    
            #close ads window
            self.closeAddsWindow()
            #
            sleep(1+random.randint(0,3000)/1000)
            #stay with qujianpan
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="留在趣键盘"]')
            if element:
                element.click() 
                continue 
                
            sleep(3+random.randint(0,3000)/1000)                          
            #close gift window
            element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close')
            if element:
                element.click()             
                
            sleep(1+random.randint(0,3000)/1000) 
        print()

    def dianjilingyu(self):
        while(True):
            #
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="点击领取"]')
            if element:
                element.click() 
            else:
                break
            
            sleep(35+random.randint(0,3000)/1000)    
            #close ads window
            self.closeAddsWindow()
            #
            sleep(1+random.randint(0,3000)/1000)
            #stay 
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="留在趣键盘"]')
            if element:
                element.click() 
                continue 
                
            sleep(3+random.randint(0,3000)/1000)                          
            #close gift window
            self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close').click()
            sleep(1+random.randint(0,3000)/1000)            
            

    def sign(self):
        try:
            self.sleep(5)
            #refuse to update
            element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivClose')
            if element:
                element.click()
            
            #refuse to install 
            self.sleep(5)
            element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivChaiClose')
            if element:
                element.click() 
#           #go to zhuan qian tab
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[2]")
            if element:      
                element.click()
            
            self.driver.switch_to.context('WEBVIEW_com.qujianpan.client')
#             
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.webkit.WebView[@text="赚钱"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]')
            if element:
                self.startMoney = element.text
                            
            element = self.find_element_by_id_without_exception(self.driver, 'signBtn')
            if element:
                element.click()
                
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="点击领取"]')
                if element:
                    element.click()  
                               
                sleep(35+random.randint(0,3000)/1000)    
                #close ads window
                self.closeAddsWindow()
                #
                sleep(1+random.randint(0,3000)/1000)
                #stay 
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="留在趣键盘"]')
                if element:
                    element.click() 
                    
                sleep(3+random.randint(0,3000)/1000)                          
                #close gift window
                self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close').click()
                sleep(1+random.randint(0,3000)/1000)                 
#                               
        except Exception:
            print('sigin except!')
            traceback.print_exc()              

    def closeAddsWindow(self):
        element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'关闭广告')]")
        if element:
            element.click()
            return
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/tt_video_ad_close')
        if element:
            element.click()
        else:
            
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.FrameLayout[@id='android:id/content']/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView")
            if element:
               element.click()
               return 
            
            self.width=self.driver.get_window_size().get('width')
            self.height=self.driver.get_window_size().get('height')
            if self.width ==720 and self.height==1366:
                #coolpad
                self.keyboard.clickAAbsolutePoint((45,95),(94,141))
            else:
                #Tencent ads union
                self.keyboard.clickAPoint((60,45), (150,135))  
    def writeGabageDic(self):
        with open('gabageconfig.json','w',encoding='utf-8') as file: 
            json.dump(self.gabageDict, file, ensure_ascii=False)   
            file.close()  #关闭文件        

    def getMoney(self):
        try:
#           #go to zhuan qian tab
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[2]")
            if element:      
                element.click()

            self.driver.switch_to.context('WEBVIEW_com.qujianpan.client')
#             
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.webkit.WebView[@text="赚钱"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]')
            if element:
                self.endMoney = element.text
        except Exception:
            print('sigin except!')
            traceback.print_exc()     
                    
    def actAutomation(self):
        self.stat.startTime = time.time()
        crashCount=0
        while(True):
            try:
                
                self.init_driver()
                self.sign()
                self.lookadsgetgifts()
                self.dianjilingyu()
                
                
#                 count = 0
#                 while(True):
#                     status=self.gotoGameGabageSort()
#                     if status:
#                         break
#                     else:
#                         count+=1
#                     
#                     if(count == 5):
#                         #too many elements could not found
#                         raise AutomationException('Automation Exception!Ｒedo')
                
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
                if crashCount > 10:
                    break                             

        self.stat.endTime = time.time()
if __name__ == '__main__':    

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    #devices = [('DU2YYB14CL003271','4.4.2')]
    devices = [('PBV0216C02008555','8.0')] #huawei P9 
    #devices = [('ORL1193020723','9.1.1')]#Cupai 9
    #devices = [('UEUDU17919005255','8.1.1')] #huawei Honor 6X 
    #devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X 
    
    
       

    #devices = [('A7QDU18420000828','9')]  
    #devices = [('SAL0217A28001753','9.1')]     
    for (deviceName,version) in devices:
        qujianpan = QujianpanAutomation(deviceName,version)         
        t = threading.Thread(target=qujianpan.actAutomation(), args=(deviceName,version,))
        t.start()
        sleep(random.randint(0, 10))
        



        