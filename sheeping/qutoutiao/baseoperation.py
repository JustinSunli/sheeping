# coding: utf-8
from time import sleep
import random
import traceback 
import math
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
        
        self.startMoney = 0
        self.endMoney = 0
        self.startTime = 0
        self.endTime = 0
        self.executionStatus = False 
        self.currentMoney = 0
        self.dailyMoney = 0
        self.dailyTotalTime = 0
        self.lastExecutionTime = 0


class BaseOperation:   
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
       self.isFirst = True
       self.sleepseconds = 5
       self.driver = None
       self.util = None
       
       self.stat = ExecutionStatistics()
       self.stat.startMoney = 0
       self.stat.endMoney = 0
       self.stat.startTime = 0
       self.stat.endTime = 0 
    
    def get_snap(self):
        """
        对整个网页截图，保存图片，然后用PIL.Image拿到图片对象
        :return: 图片对象
        """
        self.driver.save_screenshot('极验验证过程中产生的图片.png')
        page_snap_obj = Image.open('极验验证过程中产生的图片.png')
        return page_snap_obj
    
    def get_image(self,xpath='//android.view.View[@text="captcha"]/android.view.View/android.widget.Image[1]', name='captcha.png'):
        """
                从网页的网站截图中，截取验证码图片
        :return: 验证码图片对象
        """
#         img = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
#         sleep(2+random.randint(0,1000)/1000)  # 保证图片刷新出来
#         location = img.location
#         size = img.size
#         top = location['y']
#         bottom = location['y'] + size['height']
#         left = location['x']
#         right = location['x'] + size['width']
        page_snap_obj = self.get_snap()

#         #这里强调一下：大概由于高分屏的原因，网页的截图是实际像素的2倍，所以验证码定位也要相应*2
#         # crop_imag_obj = page_snap_obj.crop((left,top,right,bottom))
#         crop_imag_obj = page_snap_obj.crop((2 * left, 2 * top, 2 * right, 2 * bottom))
#         size = 258, 159
#         crop_imag_obj.thumbnail(size)
        #实际生产环境下就不需要保存这张图片了
        page_snap_obj.save(name)
        return page_snap_obj
    def get_pixel_brightness(self,r,g,b):
        return math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
            
    def get_distance(self,image):
        """
        拿到滑动验证码需要移动的距离
        :param image1: 没有缺口的图片对象
        :param image2: 带缺口的图片对象
        :return: 需要移动的距离
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
        #����ÿ�е����ص����Ȳ���
    
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
        拿到移动轨迹，模仿人的滑动行为，先匀加速后均减速
        匀变速运动基本公式：
        ①：v=v0+at
        ②：s=v0t+½at²
        ③：v²-v0²=2as
        :param distance:需要移动的距离
        :return:存放每0.3秒移动的距离
        """
        distance += 20  # 先滑过一点，最后再反着滑动回来
        # 初速度
        v = 0
        # 单位时间为0.3s来统计轨迹，轨迹即0.3s内的位移
        t = 0.3
        # 位移/轨迹列表，列表内的一个元素代表0.3s的位移
        forward_tracks = []
        # 当前位移
        current = 0
        # 到达mid值开始减速
        mid = distance * 4 / 5
        while current < distance:
            if current < mid:
                # 加速度越小，单位时间的位移越小，模拟的轨迹就越多越详细
                a = 2
            else:
                a = -3
            # 初速度
            v0 = v
            # 0.3秒时间内的位移
            s = v0 * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表,round()为保留一位小数且该小数要进行四舍五入
            forward_tracks.append(round(s))
            # 速度已经达到v，该速度作为下次的初速度
            v = v0 + a * t

        # 反着滑动到准确位置
        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]  # 总共等于-20
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks} 
    def crack(self):
        """
        程序运行流程。。。
        :return:
        """
        # 步骤三  拿到有缺口图片
        #image = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="captcha"]/android.view.View/android.widget.Image[1]')
        image=self.get_image()
        # 步骤四：拿到Box图片位置
        box = self.find_element_by_xpath_without_exception(self.driver, '//android.view.View[@text="captcha"]/android.view.View/android.view.View/android.widget.Image[2]')
        if not box:
            return 
        location = box.location
        size = box.size
        self.top = location['y']
        self.bottom = location['y'] + size['height']
        self.left = location['x']
        self.right = location['x'] + size['width']

        #步骤六：对比两张图片的所有RBG像素点，得到不一样像素点间的差值，即要移动的距离
        distance = self.get_distance(image)

        # 步骤七：模拟人的行为习惯（先匀加速拖动后匀减速拖动），把需要拖动的总距离分成一段一段小的轨迹
        tracks = self.get_tracks(distance)

        # 步骤八：按照轨迹拖动，完成验证
        slider = self.find_element_by_xpath_without_exception(self.driver, '//android.view.View[@text="captcha"]/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View')
        if not slider:
            return
        #button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
        #TouchAction(self.driver).long_press(element).move_to(x=0, y=10).release().perform()
        x1 = slider.location['x']
        y1 = slider.location['y']
        action=TouchAction(self.driver).long_press(slider)

        # 正常人类总是自信满满地开始正向滑动，自信地表现是疯狂加速
        for track in tracks['forward_tracks']:
            action=action.move_to(x=x1+track, y=y1)
            x1+=track

        # 结果傻逼了，正常的人类停顿了一下，回过神来发现，卧槽，滑过了,然后开始反向滑动
        action=action.wait(600)
        for back_track in tracks['back_tracks']:
            action=action.move_to(x=x1+back_track, y=y1)
            x1+=back_track

        # 小范围震荡一下，进一步迷惑极验后台，这一步可以极大地提高成功率
        action=action.wait(300)
        action=action.move_to(x=x1 +3, y=y1)  # 先移动去一点
        action=action.wait(400)
        action=action.move_to(x=x1 -3, y=y1) # 再退回来，模仿人的行为习惯

        action=action.wait(600)  # 0.6秒后释放鼠标
        action.release().perform()
        
        sleep(0.6)  # 0.6秒后释放鼠标
        try:
            success = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, '//'), '验证成功'))
            self.login()
            sleep(5)
            self.close_win()
        except:
            # 位置没定位好，或者时间太长了，所以本次失败，进入下一轮
            self.fail_again()  
        
       
    def find_element_by_id_without_exception(self,driver, id):
        #   
        element = None
        try:
            element = driver.find_element_by_id(id)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc()  
            print()          
                    
        return element 
    
    def find_elements_by_id_without_exception(self,driver, id):
        #   
        element = None
        try:
            element = driver.find_elements_by_id(id)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc()    
            print()        
                    
        return element             
    def find_element_by_xpath_without_exception(self,driver, xpath):
        #   
        element = None
        try:
            element = driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc()  
            print()
        
        return element    
    
    def find_elements_by_xpath_without_exception(self,driver, xpath):
        #   
        element = None
        try:
            element = driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            #print('Element not found')
            #traceback.print_exc() 
            print() 
        
        return element  
    def actAutomation(self,basecount=10):
        print      