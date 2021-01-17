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
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################
#####################################################################################################################################        
#####################################################################################################################################                
    def __init__(self, deviceName='A7QDU18420000828',version='9',timerange=(0,24),username='18601793121', password='Initial0'):
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
        
        self.stat.deviceName = self.deviceName
        self.stat.AppName = self.__class__.__name__
        
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
        #desired_caps['disableAndroidWatchers'] = True  
        #desired_caps['skipUnlock'] = True 
        #desired_caps['skipLogcatCapture'] = True  
        desired_caps['skipServerInstallation'] = True  
        
        desired_caps['newCommandTimeout'] = 600 #default 60 otherwise quit automatically
        desired_caps['appActivity'] = 'com.qujianpan.client.ui.GuideActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = KeyBoards.KeyBoards(self.driver)
        
    def tearDown(self):
        self.driver.quit()
    def checkExecutionTime(self):
        if super().checkExecutionTime():
            if int(time.time()) - self.stat.lastExecutionTime >= 30*60: #30 minutes
                return True
        return False        
    def watchQuJianPanSmallAdsAndClose(self):
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")        
        for iter in range(10):
            if self.driver.current_activity == "com.qujianpan.adlib.adcontent.view.patchad.AdPatchBaseActivity":
                break
            else:
                self.sleep()
        self.sleep(6)
        self.driver.back()
        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")        

    def MoneyBoxn(self):
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")                
        print("--------go to 储蓄罐-------")#go to me tab
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[1]")
        if element:      
            element.click()         

        if self.stat.dailyFirstExecution:
            print("--------7 日礼包-------")#7 日礼包
            element=self.find_element_by_xpath_without_exception(self.driver, '//android.view.View/android.view.View/android.view.View[5]/android.view.View')
            if element:      
                element.click()                      
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="观看视频签到"]')
                if element:
                    current_activity = self.driver.current_activity
                    element.click()
                    print("--------watch ads-------") 
                    self.watchAdsAndCloseWindow(current_activity) 
                    self.sleep(1)
                    element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="收下了"]')
                    if element:
                        element.click() 
                        
                                          
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="明天再来吧"]')
                if element:
                    print("--------not first time in a day-------") #not first time in a day
                    element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.Image[contains(@text,"model_close")]')
                    if element:
                        element.click()                                          
        
        self.sleep(6)
        print("--------collect money-------")#collect money
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View/android.view.View/android.view.View[8]')
        if element:
            element.click() 
        self.sleep(6)
        print("--------兑换-------")#兑换
        element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="兑换"]')
        if element:
            element.click()   
            element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="立即兑换"]')
            if element:
                element.click()                       
                self.sleep(1)
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="知道了"]')
                if element:
                    element.click()  
                    self.sleep(4)
                    self.watchQuJianPanSmallAdsAndClose()
        self.sleep(6)
        print("--------领取奖励-------")#领取奖励
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View/android.view.View/android.view.View[9]')
        if element:
            element.click() 
            element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="幸运翻倍"] ')
            if element:
                current_activity = self.driver.current_activity
                element.click()   
                self.watchAdsAndCloseWindow(current_activity) 
            element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="知道了"]')
            if element:
                element.click()   
        self.sleep(6)                        
        print("--------每日任务------")#每日任务
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[1]/android.view.View[1]/android.view.View[5]/android.view.View[2]')
        if element:
            element.click() 
            self.sleep(1)        
            
            while(True):
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="领取奖励"]')
                if element:
                    current_activity = self.driver.current_activity
                    element.click() 
                    self.sleep(3)
                    if self.driver.current_activity != '.ui.MainActivity':
                        self.sleep(6)
                        self.watchAdsAndCloseWindow(current_activity)        
                else:
                    break
            
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.Image[contains(@text,"model_close")]')
            if element:
                element.click()
        
        self.sleep(6)   
        print("--------小猪转盘------")#小猪转盘
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[1]/android.view.View[1]/android.view.View[5]/android.view.View[3]')
        if element:
            element.click() 
            self.sleep(1)        
            for iter in range(15): 
                print("........."+str(iter)+".........")          
                element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[1]/android.view.View[5]/android.view.View[2]')
                if element:
                    current_activity = self.driver.current_activity
                    element.click()
                    element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="放弃"]')
                    if element:
                        element.click()
                        self.sleep(2)
                        print("--------finished 小猪转盘 , back to main window------")
                        self.driver.back()
                        break 
                    self.sleep(3)
                    #direct money
                    if self.driver.current_activity == 'com.innotech.jb.combusiness.web.SignDetailWebActivity':
                        print("--------direct money------")
                        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="恭喜抽中"]/../android.view.View')
                        if element:
                            element.click()
                            
                        continue
                    #3 seconds ads
                    elif self.driver.current_activity == 'com.qujianpan.adlib.adcontent.view.patchad.AdPatchBaseActivity':
                        print("--------3 seconds ads------")
                        self.watchQuJianPanSmallAdsAndClose()
                        continue
                    else:
                        #long ads
                        print("--------long ads------")
                        self.watchAdsAndCloseWindow(current_activity)
                        continue
        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")        
    
    def closeNormalWindow(self):
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")        
        #close window if it exists
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/iv_close')                                   
        if element:
            element.click()  
        else:
            self.driver.back()   
        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")
         
    def preExecution(self):
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")
        self.sleep(10)
        print("--------refuse to update------")#refuse to update
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivClose')
        if element:
            element.click()
        
        print("--------close 提现 ads------")#close 提现 ads
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/new_red_close')
        if element:
            element.click()
        
        print("--------refuse to install ------")#refuse to install 
        #self.sleep(5)
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/ivChaiClose')
        if element:
            element.click() 
            
        print("--------close home tab show------")#close home tab show
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/home_bottom_close')
        if element:
            element.click()               
            
        print("--------go to me tab------")#           #go to me tab
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[4]")
        if element:      
            element.click() 
        
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/mainCardGoldTotal')
        if element:
            self.stat.startMoney=int(element.text.split()[0].strip())
            if self.stat.dailyFirstExecution:
                self.stat.dailyStartMoney = self.stat.startMoney                                    
        
        #watch a ads             
        #element=self.find_element_by_xpath_without_exception(self.driver, "//android.support.v7.widget.RecyclerView[@resource-id='com.qujianpan.client:id/jiliTaskrecyclerView']/android.widget.LinearLayout[2]")
        #if element:      
        #    element.click()
        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")
       
    def afterExecution(self): 
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")               
#           #go to me tab
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[4]")
        if element:      
            element.click() 
        
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/mainCardGoldTotal')
        if element:
            self.stat.endMoney=int(element.text.split()[0].strip())
            if self.stat.dailyLastExecution:
                self.stat.dailyEndMoney = self.stat.endMoney
            
            #提现
            if self.stat.startMoney > 1000000:
                element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/mainCardCatchGlod')
                element.click()
                self.sleep(1)
                    #10 元
                element=self.find_element_by_xpath_without_exception(self.driver, "//android.support.v7.widget.RecyclerView[@resource-id='com.qujianpan.client:id/withdrawalAmountRecyView']/android.view.ViewGroup[2]")
                if element:      
                    element.click()
                    self.sleep(1)
                    #提现
                    element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/cashSubmit')
                    if element:
                        element.click()
                        self.sleep(1)   
                        self.driver.back()
                        self.sleep(1)
                        self.driver.back()                 
        #finish the task
        super().afterExecution()                
        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")
                
    def sign(self):
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")

        try:
#           #go to zhuan qian tab
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[3]")
            if element:      
                element.click()
            self.sleep(10)
            element = self.find_element_by_xpath_without_exception(self.driver, '//*[@resource-id="signUpAddBtn"]')
            if element:
                element.click()
                self.sleep(3)
                element = self.find_element_by_xpath_without_exception(self.driver, '//*[@resource-id="signUpAddBtn"]')
                if element:
                    current_activity = self.driver.current_activity
                    element.click()
                    #wait ads pop up 
                    self.sleep(3)
                    self.watchAdsAndCloseWindow(current_activity)
                    self.sleep(3)
                    self.closeNormalWindow()
                            
            #self.driver.switch_to.context('WEBVIEW_com.qujianpan.client')                
#                               
        except Exception:
            print('sigin except!')
            traceback.print_exc()              
        
        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")
    def watchAdsAndCloseWindow(self, activity):
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")                
        ads_activity = None
        #wait for the ads pop up
        for iter in range(60):
            if self.driver.current_activity !=activity:
                ads_activity = self.driver.current_activity
                break
            self.sleep()
        #watch ads until it finished
        for iter in range(60):
            if self.driver.current_activity== 'com.qujianpan.adlib.adcontent.view.video.AdInVideoBaseActivity':
                print()
            if self.driver.current_activity in set(['com.bytedance.sdk.openadsdk.activity.TTRewardVideoActivity','com.innotech.jb.combusiness.web.SignDetailWebActivity']):
                if self.closeAdsDetails():
                    break
            elif self.driver.current_activity=='com.iclicash.advlib.ui.front.InciteADActivity':
                self.sleep(1)
                element = self.find_element_by_xpath_without_exception(self.driver,'//*[@text="点击重播"]')
                if element:
                    if self.closeAdsDetails():
                        break                            
            else: #com.iclicash.advlib.ui.front.ADBrowser
                print(self.driver.current_activity)
                self.driver.back()
                self.sleep(3)
                if self.closeAdsDetails():
                    break                
                if self.driver.current_activity == activity:
                    break

        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")        
        
    def closeAddsWindow(self):
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")                
        for iter in range(2):
            if self.closeAdsDetails():
                print("GoOut--------"+sys._getframe().f_code.co_name+"-------") 
                break
        
    def closeAdsDetails(self):
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")                        
        element = self.find_element_by_id_without_exception(self.driver, 'com.qujianpan.client:id/tt_video_ad_close')
        if element:
            element.click()
            print("GoOut--------"+sys._getframe().f_code.co_name+"-------1")           
            return True
        
#       element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'关闭'广告)]")
#       if element:
#           element.click()
#           return True
#       
#       element = self.find_element_by_xpath_without_exception(self.driver, "//android.view.View[contains(@text,'关闭')]")
#       if element:
#           element.click()
#           return True        
        
        element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.LinearLayout[@resource-id='com.qujianpan.client:id/action_bar_root']/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.view.View")
        if element and element.is_enabled() and element.is_displayed():
           element.click()
           print("GoOut--------"+sys._getframe().f_code.co_name+"-------2")           
           return True
        
        return False
        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")           
                    
    def actAutomation(self):
        super().actAutomation()
        print("Enter--------"+sys._getframe().f_code.co_name+"-------")                
        self.stat.startTime = time.time()
        crashCount=0
        while(True):
            try:
                super().preExecution()
                self.init_driver()
                self.preExecution()
                if self.stat.dailyFirstExecution:
                    self.sign()
                self.MoneyBoxn()
                self.afterExecution()
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
                if crashCount > 3:
                    break                             

        self.stat.endTime = time.time()
        print("GoOut--------"+sys._getframe().f_code.co_name+"-------")        
        
if __name__ == '__main__':    

    #devices = [('DU2YYB14CL003271','4.4.2'),('A7QDU18420000828','9'),('SAL0217A28001753','9')]
    #devices = [('DU2YYB14CL003271','4.4.2')]
    devices = [('PBV0216C02008555','8.0')] #huawei P9 
    #devices = [('ORL1193020723','9.1.1')]#Cupai 9
    devices = [('UEUDU17919005255','8.0.0')] #huawei Honor 6X 
    #devices = [('UEU4C16B16004079','8.1.1.1')] #huawei Honor 6X 
    
    
       

    devices = [('A7QDU18420000828','9')]  
    #devices = [('SAL0217A28001753','9.1')]     
    for (deviceName,version) in devices:
        qujianpan = QujianpanAutomation(deviceName,version,(0,24))  
        
        qujianpan.stat.dailyFirstExecution = True
        qujianpan.stat.dailyLastExecution = False 
          
        t = threading.Thread(target=qujianpan.actAutomation())
        t.start()
        sleep(random.randint(0, 10))
        



        