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

#assii unicode
from urllib.request import quote
from _ast import Raise

class  QujianpanAutomation(BaseOperation):
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
        desired_caps['noReset'] = True
        desired_caps['udid'] = self.deviceName
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.qujianpan.client.ui.MainA'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = keyboards.KeyBoards(self.driver)
        
    def tearDown(self):
        self.driver.quit()


    def lookadsgetgifts(self):
        sleep(1+random.randint(0,3000)/1000)
        while(True):
            #time gift
            
            self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@resource-id='header']/android.view.View[2]/android.view.View[2]").click()
            
            
            #element = self.find_element_by_id_without_exception(self.driver,'pop_notimes')
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.webkit.WebView/android.view.View/android.view.View[@resource-id='popTimeRewardCover']/android.view.View[@resource-id='pop_notimes']/android.view.View[@resource-id='pop_konwBtn']")
            if element and element.is_displayed():
                element.click()
                break;
 
            #self.keyboard.clickAPoint((891,99), (1080,171))  

            #element = self.find_element_by_xpath_without_exception(self.driver, "//android.support.v4.view.ViewPager[@resource-id='com.qujianpan.client:id/mViewPager']/android.view.ViewGroup/android.webkit.WebView")
            element = self.find_element_by_id_without_exception(self.driver,'pop_timerPointerBtn')
            if element:
#                 element = self.find_element_by_id_without_exception(self.driver,'pop_konwBtn')
#                 if element:
#                     #0 chance left
#                     #
#                     self.find_element_by_id_without_exception(self.driver, 'pop_konwBtn').click()
#                     #self.keyboard.clickAPoint((192,891), (888,1023))
#                     #sleep(1+random.randint(0,3000)/1000)
#                     #self.keyboard.clickAPoint((192,891), (888,1023))
#                     break
#                 #time bonus
#                 #
#                 self.keyboard.clickAPoint((909,639), (951,675))
                element.click()
            
            elif element:
                self.keyboard.clickAPoint((235,1238), (850,1351))
                
            sleep(35+random.randint(0,3000)/1000)    
            #close ads window
            
            
            self.closeAddsWindow()
            #
            sleep(1+random.randint(0,3000)/1000)
            #close gift window
            self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close').click()
            sleep(1+random.randint(0,3000)/1000)
            
#             resultstring = element.text
#             pattern = re.compile('[^0-9]')
#             resultstring = pattern.sub('',resultstring)
#             leftcount = int(resultstring)
#             #pop
#             sleep(1+random.randint(0,3000)/1000)
#             element = self.find_element_by_id_without_exception(self.driver, 'pop_timerStageBtn')
#             if element:
#             
#             if leftcount - 1 ==0:
#                 break
            
            
        print()
    def sign(self):
        try:
            #refuse to update
            element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivClose')
            if element:
                element.click()
            #refuse to install 
            #self.driver.back()
            
            #refuse to ads
            element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivChaiClose')
            if element:
                element.click() 
#             #go to zhuan qian tab
#             element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[2]")
#             if element:
#                 element.click()
#             
#             element = self.find_element_by_id_without_exception(self.driver, 'signBtn')
#             if element:
#                 element.click()
#                 
#             element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/llyGetCoin')
#             if element:
#                 element.click()
#                 sleep(35+random.randint(0,3000)/1000)
#                 #close ads window
#                 self.closeAddsWindow()  
#                 sleep(1+random.randint(0,3000)/1000)
#                 #close gift window
#                 self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close').click()
#                 sleep(1+random.randint(0,3000)/1000)
            
#             #refuse to update
#             element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivClose')
#             if element:
#                 element.click()
#             #refuse to install 
#             #self.driver.back()
#             
#             #refuse to ads
#             element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivChaiClose')
#             if element:
#                 element.click()                
        except Exception:
            print('sigin except!')
            traceback.print_exc()              

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
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[4]")
        if element:
            element.click()
            
        #refuse to ads
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivChaiClose')
        if element:
            element.click() 
        #sleep(35+random.randint(0,5000)/1000)
        #
        #self.driverSwipe.SwipeUp() 
        sleep(10+random.randint(0,5000)/1000)
        #advanced task
        #self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@resource-id='fixedTaskNav']/android.widget.ListView/android.view.View[2]").click()
        
        #gabage sort
        #快来玩
#         element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[@resource-id='advanceTaskCon']/android.view.View[3]/android.view.View[1]")
#         if element.text == '分垃圾赚金币':
#             element.click()
#         ele = self.find_element_by_id_without_exception(self.driver, 'tryGameBtn')
#         if ele:
#             ele.click()
#         else:
#             sleep(30)
#             self.driver.back()
#             self.closeAddsWindow()
#             self.find_element_by_xpath_without_exception(self.driver, "//android.widget.LinearLayout[@resource-id='com.qujianpan.client:id/navigation_ll']/android.widget.RelativeLayout[3]").click()
#             self.find_element_by_xpath_without_exception(self.driver, "//android.support.v7.widget.RecyclerView[@resource-id='com.qujianpan.client:id/jiliTaskrecyclerView']/android.widget.LinearLayout[2]/android.widget.RelativeLayout/android.widget.ImageView").click()
#             self.find_element_by_id_without_exception(self.driver, 'tryGameBtn').click()
        elements = self.find_elements_by_xpath_without_exception(self.driver, "//android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout/android.widget.ImageView")
        if len(elements)==0:
            return False
        iter=0
        for element in elements:
            if iter==0:
                iter+=1
                continue
            
            element.click()
            ele = self.find_element_by_id_without_exception(self.driver, 'tryGameBtn')
            if ele:
                ele.click()
                break
            else:
                self.driver.back()
                #note ads vedio page
                element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']")
                if element:
                    continue
                else:
                    sleep(35)
                    self.closeAddsWindow()
                    #close gift window
                    self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close').click()
                    sleep(1+random.randint(0,3000)/1000)                    
                    
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
                    break
                #end wrong
                element = self.find_element_by_id_without_exception(self.driver, 'watchResultBtn1')
                if element:
                    self.gabageDict[garbageName] = self.find_element_by_id_without_exception(self.driver, 'lastErrorGarbageType').text
                    self.find_element_by_id_without_exception(self.driver, 'lastAnswerErrorAlertClose').click()
                    break                
                
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
    def closeAddsWindow(self):
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/tt_video_ad_close')
        if element:
            element.click()
        else:
            #Tencent ads union
            self.keyboard.clickAPoint((60,45), (150,135))  
    def writeGabageDic(self):
        with open('gabageconfig.json','w',encoding='utf-8') as file: 
            json.dump(self.gabageDict, file, ensure_ascii=False)   
            file.close()  #关闭文件        
 
    def payGameGabageSort(self):
        
        print()
        
    def actAutomation(self):
        while(True):
            try:
                self.init_driver()
                self.sign()
                #qujianpan.lookadsgetgifts()
                
                count = 0
                while(True):
                    status=self.gotoGameGabageSort()
                    if status:
                        break
                    else:
                        count+=1
                    
                    if(count == 3):
                        #too many elements could not found
                        raise AutomationException('Automation Exception!Ｒedo')
                
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

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    devices = [('DU2YYB14CL003271','4.4.2')]
    devices = [('PBV0216C02008555','8.0')] #huawei P9 
    devices = [('ORL1193020723','9.1.1')]#Cupai 9
    #devices = [('UEUDU17919005255','8.1.1')] #huawei Honor 6X 
    
       

    #devices = [('A7QDU18420000828','9')]  
    #devices = [('SAL0217A28001753','9.1')]     
    for (deviceName,version) in devices:
        qujianpan = QujianpanAutomation(deviceName,version)         
        t = threading.Thread(target=qujianpan.actAutomation(), args=(deviceName,version,))
        t.start()
        sleep(random.randint(0, 10))