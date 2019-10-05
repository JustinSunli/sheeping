# coding: utf-8
class driverSwipe(object):

    def __init__(self, driver):
        self.driver = driver
        self.width = self.driver.get_window_size().get('width')
        self.height = self.driver.get_window_size().get('height')
    
    def SwipeUp(self):
        self.driver.swipe(self.width / 2, self.height * 3/ 4, self.width /2 , self.height /4)

    def SwipeUpALittle(self):
        self.driver.swipe(self.width / 2, self.height * 5/ 6, self.width /2 , self.height * 4 / 6)

    def SwipeDown(self):
        self.driver.swipe(self.width / 2,self.height /4 , self.width /2 , self.height * 3/ 4)

    def SwipeDownALittle(self):
        self.driver.swipe(self.width / 2, self.height * 4 / 6 , self.width /2 , self.height * 5/ 6)
        
    def SwipeRight(self):
        self.driver.swipe(self.width / 4,self.height /2 , self.width * 3 / 4 , self.height / 2)

    def SwipeLeft(self):
        self.driver.swipe(self.width * 3 / 4,self.height /2 , self.width / 4 , self.height / 2)
        
    def AdbSwipeLeft(self):
        opts={'command':'input','args':['swipe','500','100','100', '100', '300']}
        self.driver.execute_script("mobile:shell",opts)

    def clickTheCenter(self):
        self.driver.move_by_offset(self.width//2,self.height//2).double_click()   