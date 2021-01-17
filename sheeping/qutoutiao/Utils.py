# coding: utf-8
from time import sleep
from appium import webdriver
import re
import time
import os
import sys
import math
import random
from qutoutiao import Key_Codes

class Utils:
    def __init__(self,driver):
        self.driver = driver
        self.width=self.driver.get_window_size().get('width')
        self.height=self.driver.get_window_size().get('height')
        self.originalWidth = 1080
        self.originalHeigth = 2160
        self.mark = 0.3
    def watchvedios(self,textname):
        file = open(textname,'r')
        result = file.readlines()
        file.close()
        return result
        
    def ClickPoint(self,fromPoint,toPoint):
        (fromX,fromY) = fromPoint
        (toX,toY) = toPoint
        
        fromX = fromX + (toX-fromX)*self.mark
        fromY= fromY+(toY-fromY)*self.mark
        toX = toX - (toX-fromX)*self.mark
        toY = toY - (toY-fromY)*self.mark
        
        resFromX = math.ceil((fromX/self.originalWidth)*self.width) 
        resFromY = math.ceil((fromY/self.originalHeigth)*self.height)
        
        resToX = math.floor((toX/self.originalWidth)*self.width)
        resToY = math.floor((toY/self.originalHeigth)*self.height)
        
        clickPointX = random.randint(resFromX,resToX)
        clickPointY = random.randint(resFromY,resToY)
        return (clickPointX,clickPointY)
    
    def ClickAbsolutePoint(self,fromPoint,toPoint):
        (fromX,fromY) = fromPoint
        (toX,toY) = toPoint
        
        fromX = fromX + (toX-fromX)*self.mark
        fromY= fromY+(toY-fromY)*self.mark
        toX = toX - (toX-fromX)*self.mark
        toY = toY - (toY-fromY)*self.mark
        
        resFromX = math.ceil(fromX) 
        resFromY = math.ceil(fromY)
        
        resToX = math.floor(toX)
        resToY = math.floor(toY)
        
        clickPointX = random.randint(resFromX,resToX)
        clickPointY = random.randint(resFromY,resToY)
        return (clickPointX,clickPointY)
    
    #honor6X
    def getAPointX(self,x):
        self.originalWidth6X = 1080
        self.originalHeigth6X = 1920        
        resX = math.floor( x / self.originalWidth6X * self.width )
        return resX
    
    def getAPointY(self,y):
        self.originalWidth6X = 1080
        self.originalHeigth6X = 1920        
        resY = math.floor( y / self.originalHeigth6X * self.width )
        return resY    
        
    
    
    def centerPoint(self,fromPoint,toPoint):
        (fromX,fromY) = fromPoint
        (toX,toY) = toPoint
        centerX = ((fromX+toX)/2)/self.originalWidth * self.width
        centerY = ((fromY+toY)/2)/self.originalHeigth * self.height
        return (centerX,centerY)
        