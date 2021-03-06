# coding: utf-8
from time import sleep
import logging
import time
import random
import traceback 
import math
from qutoutiao import Key_Codes
from qutoutiao import DriverSwipe
from qutoutiao import Utils
from qutoutiao import KeyBoards
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import sys
from appium.webdriver.common.touch_action import TouchAction

class AutomationException(Exception):
    
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message
        
class ExecutionStatistics:
    def __init__(self):
        
        self.deviceName = None
        self.AppName = None
        
        self.startMoney = None
        self.endMoney = None
        
        self.dailyFirstExecution = False 
        self.dailyLastExecution = False 
        
        self.currentMoney = None       
        self.dailyStartMoney = None
        self.dailyEndMoney = None
        
        self.startTime = None
        self.entTime = None
        self.dailyTotalTime = None
        self.lastExecutionTime = None
        self.priority = 0
        
    def __lt__(self,other): 
        return self.priority < other.priority        

class ExecutionParam:
    def __init__(self,deviceName='A7QDU18420000828',version='9',port='4723',bootstrapPort='4723',username='18601793121', password='Initial0'):
        
        self.deviceName=deviceName
        self.version=version
        self.username=username
        self.password=password
        self.port = port
        self.bootstrapPort=bootstrapPort
    
class BaseOperation:   
    def __init__(self, executionparam=None,timerange=(0,24)):
        
        self.sleepseconds = 5
        self.driver = None
        self.util = None
        self.driverSwipe = None
        self.keyboard = None       
        (self.fromHour,self.toHour) = timerange
        
        self.deviceName=executionparam.deviceName
        self.version=executionparam.version
        self.username=executionparam.username
        self.password=executionparam.password
        self.port = executionparam.port
        self.bootstrapPort=executionparam.bootstrapPort
        
        
        self.stat = ExecutionStatistics()
        self.stat.startMoney = None
        self.stat.endMoney = None
        self.stat.startTime = None
        self.stat.endTime = None 
        
        self.stat.deviceName = self.deviceName
        self.stat.AppName = None
    
        self.stat.dailyFirstExecution = False
        self.stat.dailyLastExecution = False       
        self.stat.dailyStartMoney = None
        self.stat.dailyEndMoney = None
        
        self.stat.lastExecutionTime = None 
        self.stat.priority = 0  
        self.stat.executed = False
        self.stat.godMonitored=False
        
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = self.version
        self.desired_caps['deviceName'] = self.deviceName
        self.desired_caps['dontStopAppOnReset'] = True  
        self.desired_caps['noReset'] = True
        self.desired_caps['udid'] = self.deviceName
        self.desired_caps['newCommandTimeout'] = 300#1500 #default 60 otherwise quit automatically
        self.desired_caps['ignoreUnimportantViews'] = True 
        self.desired_caps['normalizeTagNames'] = True
        self.desired_caps['autoGrantPermissions'] = True 
        self.desired_caps['adbExecTimeout'] = 200000 #adb command timeout
        self.desired_caps['uiautomator2ServerLaunchTimeout'] = 100000 #initialize the app timeout
        
        
        
        #
        #desired_caps['disableAndroidWatchers'] = True  
        #desired_caps['skipUnlock'] = True 
        self.desired_caps['skipLogcatCapture'] = True  
        #self.desired_caps['skipServerInstallation'] = True  
        #desired_caps['unlockType'] = "password"
        #desired_caps['unlockKey'] = "123456"     
        
        #logging control
        logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
    def initAfterDriver(self):
        self.driver.implicitly_wait(3) #wait time when not find element
        self.driverSwipe = DriverSwipe.driverSwipe(self.driver)
        self.util = Utils.Utils(self.driver)
        self.keyboard = KeyBoards.KeyBoards(self.driver)
    def sleep(self,time=0,randIdex=2):
        #sleep some seconds
        sleep(time+random.randint(0,randIdex*1000)/1000)
    
    def ElementUsable(self,element):
        status=False
        try:    
            status= element and element.is_displayed()
        except Exception:
            pass
        return status
    def preExecution(self):
        self.stat.startTime = time.time()
        return 
    def afterExecution(self):
        self.stat.endTime = time.time()
        return
    def stringToTimeData(self,str_data):
        # ?????????????????????
        strptime = time.strptime(str_data,"%Y-%m-%d %H:%M:%S")
        #print("strptime",strptime)
        mktime = int(time.mktime(strptime))
        #print("mktime",mktime)
        return mktime 

    def possibilityExecution(self,number):
        randomnumber=random.randint(0,10000)/100;
        return randomnumber<=number
    
    def tearDown(self):
        try:
            apps = ['com.android.contacts','com.android.settings','com.android.mms']
            for appname in apps:
                self.driver.terminate_app(appname)     
        except Exception:
            pass

               
    def unlockTheScreen(self):
        if self.driver.is_locked():
            self.driver.lock(1)
            #
            self.driverSwipe.SwipeUp()
            element = self.find_element_by_id_without_exception(self.driver, 'com.android.systemui:id/lockPatternView')
            if element:
                #
                pass
        
    def checkExecutionTime(self):
        timeStruct = time.localtime(time.time())
        if timeStruct.tm_hour >= self.fromHour and timeStruct.tm_hour < self.toHour:
            return True
        return False
    def getPriority(self):
        timeStruct = time.localtime(time.time())
        fromTimeStr = "{}-{}-{} {}:{}:{}".format(timeStruct.tm_year, timeStruct.tm_mon,timeStruct.tm_mday,self.fromHour,'0','0')
        toTimeStr = None
        if self.toHour!=24:
            toTimeStr = "{}-{}-{} {}:{}:{}".format(timeStruct.tm_year, timeStruct.tm_mon,timeStruct.tm_mday,self.toHour,'0','0')
        else:
            toTimeStr = "{}-{}-{} {}:{}:{}".format(timeStruct.tm_year, timeStruct.tm_mon,timeStruct.tm_mday,23,'59','59')
        fromTime = self.stringToTimeData(fromTimeStr)
        toTime = self.stringToTimeData(toTimeStr)
        
        if toTime - time.time() <= 1*60*60*1000: #one hour
            return 0
        
        return 1
    
    def __lt__(self,other): 
        return self.getPriority() < other.getPriority()    
        
    def get_snap(self):
        """
        ????????????????????????????????????????????????PIL.Image??????????????????
        :return: ????????????
        """
        self.driver.save_screenshot('????????????????????????????????????.png')
        page_snap_obj = Image.open('????????????????????????????????????.png')
        return page_snap_obj
    
    def get_image(self,xpath='//android.view.View[@text="captcha"]/android.view.View/android.widget.Image[1]', name='captcha.png'):
        """
                ???????????????????????????????????????????????????
        :return: ?????????????????????
        """
#         img = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
#         sleep(2+random.randint(0,1000)/1000)  # ????????????????????????
#         location = img.location
#         size = img.size
#         top = location['y']
#         bottom = location['y'] + size['height']
#         left = location['x']
#         right = location['x'] + size['width']
        page_snap_obj = self.get_snap()

#         #???????????????????????????????????????????????????????????????????????????????????????2???????????????????????????????????????*2
#         # crop_imag_obj = page_snap_obj.crop((left,top,right,bottom))
#         crop_imag_obj = page_snap_obj.crop((2 * left, 2 * top, 2 * right, 2 * bottom))
#         size = 258, 159
#         crop_imag_obj.thumbnail(size)
        #??????????????????????????????????????????????????????
        page_snap_obj.save(name)
        return page_snap_obj
    def get_pixel_brightness(self,r,g,b):
        return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
            
    def get_distance(self,image):
        """
        ??????????????????????????????????????????
        :param image1: ???????????????????????????
        :param image2: ????????????????????????
        :return: ?????????????????????
        """
        #490 520
        rankFirstHalfFrom = 0.198
        rankFirstHalfTo = 0.378
        
        rankSecondHalfFrom = 0.667
        rankSecondHalfTo = 0.847
        thresholdRange = 10
        
        fromFirstHalfX =math.floor(self.top+ (self.bottom - self.top)* rankFirstHalfFrom)
        toFirstHalfX   =math.floor(self.top+ (self.bottom - self.top)* rankFirstHalfTo)
        
        fromSecondHalfX =math.floor(self.top+ (self.bottom - self.top)* rankSecondHalfFrom)
        toSecondHalfX   =math.floor(self.top+ (self.bottom - self.top)* rankSecondHalfTo)
        
        i = 0
        #????????????????????????????????????????????????????????
    
        previousArr=[]
        currentArr=[]
        positionRate=[]
        initialImageMatrix=image.load()
        ColumnSize = toFirstHalfX-fromFirstHalfX + toSecondHalfX-fromSecondHalfX
        #skip the first mix-picture area
        startPosition = self.right+2*thresholdRange
        for i in range(startPosition, image.size[0]):
            if len(currentArr)==(ColumnSize*thresholdRange):
                del currentArr[0:ColumnSize]
            if len(previousArr)==(ColumnSize*thresholdRange):
                del previousArr[0:ColumnSize]
                           
            for j in range(fromFirstHalfX, toFirstHalfX):
                rgb = initialImageMatrix[i, j]
                r,g,b = rgb[0],rgb[1],rgb[2]
                brightness = self.get_pixel_brightness(r,g,b)
                currentArr.append(brightness)    
    
            for j in range(fromSecondHalfX, toSecondHalfX):
                rgb = initialImageMatrix[i, j]
                r,g,b = rgb[0],rgb[1],rgb[2]
                brightness = self.get_pixel_brightness(r,g,b)
                currentArr.append(brightness) 
                
            if i-thresholdRange >= startPosition:
    #                 rgb = initialImageMatrix[i-10, j]
    #                 r,g,b = rgb[0],rgb[1],rgb[2]
    #                 brightness = get_pixel_brightness(r,g,b)                
    #                 previousArr.append(brightness)
                previousArr.extend(currentArr[0:ColumnSize])
            if len(previousArr)==len(currentArr) and len(currentArr)==thresholdRange*ColumnSize:
                rate = sum(currentArr) / sum(previousArr)
                positionRate.append((i,rate))
                
        positionRate.sort(key=lambda x:x[1])
        return positionRate[0][0] - self.right - thresholdRange
        
    def get_tracks(self,distance):
        """
        ????????????????????????????????????????????????????????????????????????
        ??????????????????????????????
        ??????v=v0+at
        ??????s=v0t+??at??
        ??????v??-v0??=2as
        :param distance:?????????????????????
        :return:?????????0.3??????????????????
        """
        distance += 20  # ?????????????????????????????????????????????
        # ?????????
        v = 0
        # ???????????????0.3s???????????????????????????0.3s????????????
        t = 0.3
        # ??????/?????????????????????????????????????????????0.3s?????????
        forward_tracks = []
        # ????????????
        current = 0
        # ??????mid???????????????
        mid = distance * 4 / 5
        while current < distance:
            if current < mid:
                # ?????????????????????????????????????????????????????????????????????????????????
                a = 2
            else:
                a = -3
            # ?????????
            v0 = v
            # 0.3?????????????????????
            s = v0 * t + 0.5 * a * (t ** 2)
            # ???????????????
            current += s
            # ?????????????????????,round()??????????????????????????????????????????????????????
            forward_tracks.append(round(s))
            # ??????????????????v????????????????????????????????????
            v = v0 + a * t

        # ???????????????????????????
        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]  # ????????????-20
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks} 
    def crack(self):
        """
        ???????????????????????????
        :return:
        """
        # ?????????  ?????????????????????
        #image = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="captcha"]/android.view.View/android.widget.Image[1]')
        image=self.get_image()
        # ??????????????????Box????????????
        box = self.find_element_by_xpath_without_exception(self.driver, '//android.view.View[@text="captcha"]/android.view.View/android.view.View/android.widget.Image[2]')
        if not box:
            return 
        location = box.location
        size = box.size
        self.top = location['y']
        self.bottom = location['y'] + size['height']
        self.left = location['x']
        self.right = location['x'] + size['width']

        #???????????????????????????????????????RBG????????????????????????????????????????????????????????????????????????
        distance = self.get_distance(image)

        # ??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
        tracks = self.get_tracks(distance)

        # ?????????????????????????????????????????????
        slider = self.find_element_by_xpath_without_exception(self.driver, '//android.view.View[@text="captcha"]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View')
        if not slider:
            return
        #button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
        #TouchAction(self.driver).long_press(element).move_to(x=0, y=10).release().perform()
        x1 = slider.location['x']
        y1 = slider.location['y']
        action=TouchAction(self.driver).long_press(slider)

        # ????????????????????????????????????????????????????????????????????????????????????
        for track in tracks['forward_tracks']:
            action=action.move_to(x=x1+track, y=y1)
            x1+=track

        # ??????????????????????????????????????????????????????????????????????????????????????????,????????????????????????
        action=action.wait(600)
        for back_track in tracks['back_tracks']:
            action=action.move_to(x=x1+back_track, y=y1)
            x1+=back_track

        # ?????????????????????????????????????????????????????????????????????????????????????????????
        action=action.wait(300)
        action=action.move_to(x=x1 +3, y=y1)  # ??????????????????
        action=action.wait(400)
        action=action.move_to(x=x1 -3, y=y1) # ???????????????????????????????????????

        action=action.wait(600)  # 0.6??????????????????
        action.release().perform()
        
        sleep(0.6)  # 0.6??????????????????
        try:
            success = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, '//'), '????????????'))
            self.login()
            sleep(5)
            self.close_win()
        except:
            # ?????????????????????????????????????????????????????????????????????????????????
            self.fail_again()  
        
       
    def find_element_by_id_without_exception(self,driver, id):
        #   
        element = None
        try:
            element = driver.find_element_by_id(id)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc()  
            pass          
                    
        return element 
    
    def find_elements_by_id_without_exception(self,driver, id):
        #   
        element = None
        try:
            element = driver.find_elements_by_id(id)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc()    
            pass        
                    
        return element             
    def find_element_by_xpath_without_exception(self,driver, xpath):
        #   
        element = None
        try:
            element = driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc()  
            pass
        
        return element    
    
    def find_element_by_accessibility_id_without_exception(self,driver, accessid):
        #   
        element = None
        try:
            element = driver.find_element_by_accessibility_id(accessid)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc()  
            pass
        
        return element      
    def find_elements_by_xpath_without_exception(self,driver, xpath):
        #   
        element = None
        try:
            element = driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc() 
            pass 
        
        return element  
    def actAutomation(self,basecount=10):
        self.stat.executed = True      