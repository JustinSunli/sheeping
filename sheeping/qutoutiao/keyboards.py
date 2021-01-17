# coding: utf-8
from time import sleep
import random
from qutoutiao import Utils
from qutoutiao.Key_Codes import *

class KeyBoards:
    def __init__(self,driver):
        self.driver = driver
        self.util = Utils.Utils(self.driver)
        
    def preAKey(self,letter):
        if letter == '0':
            self.press0()
        elif letter == '1':
            self.press1()
        elif letter == '2':
            self.press2()
        elif letter == '3':
            self.press3()
        elif letter == '4':
            self.press4()
        elif letter == '5':
            self.press5()
        elif letter == '6':
            self.press6()
        elif letter == '7':
            self.press7()
        elif letter == '8':
            self.press8()
        elif letter == '9':
            self.press9()
        elif letter == 'A':
            self.pressA()
        elif letter == 'B':
            self.pressB()
        elif letter == 'C':
            self.pressC()
        elif letter == 'D':
            self.pressD()
        elif letter == 'E':
            self.pressE()
        elif letter == 'F':
            self.pressF()
        elif letter == 'G':
            self.pressG()
        elif letter == 'H':
            self.pressH()  
        elif letter == 'I':
            self.pressI()                                                                                                          
        elif letter == 'J':
            self.pressJ()    
        elif letter == 'K':
            self.pressK()
        elif letter == 'L':
            self.pressL()
        elif letter == 'M':
            self.pressM()
        elif letter == 'N':
            self.pressN()
        elif letter == 'O':
            self.pressO()                        
        elif letter == 'P':
            self.pressP()                                                                                                          
        elif letter == 'Q':
            self.pressQ()    
        elif letter == 'R':
            self.pressR()
        elif letter == 'S':
            self.pressS()
        elif letter == 'T':
            self.pressT()
        elif letter == 'U':
            self.pressU()
        elif letter == 'V':
            self.pressV()
        elif letter == 'W':
            self.pressW()                                                                                                          
        elif letter == 'X':
            self.pressX()    
        elif letter == 'Y':
            self.pressY()
        elif letter == 'Z':
            self.pressZ()
        elif letter == ' ':
            self.pressSpace()            
        else:
            print('Letter not supported')
            
    def press1(self):
#         clickPoint = self.util.ClickPoint((21,1441),(104,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)
        opts={'command':'input','args':['keyevent',KEYCODE_1]}
        self.driver.execute_script("mobile:shell",opts)        
    def press2(self):
#         clickPoint = self.util.ClickPoint((128,1441),(211,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        opts={'command':'input','args':['keyevent',KEYCODE_2]}
        self.driver.execute_script("mobile:shell",opts)         
    def press3(self):
#         clickPoint = self.util.ClickPoint((235,1441),(314,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_3]}
        self.driver.execute_script("mobile:shell",opts)                        
    def press4(self):
#         clickPoint = self.util.ClickPoint((340,1441),(419,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        opts={'command':'input','args':['keyevent',KEYCODE_4]}
        self.driver.execute_script("mobile:shell",opts)              
    def press5(self):
#         clickPoint = self.util.ClickPoint((446,1441),(526,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_5]}
        self.driver.execute_script("mobile:shell",opts)             
    def press6(self):
#         clickPoint = self.util.ClickPoint((552,1441),(632,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        opts={'command':'input','args':['keyevent',KEYCODE_6]}
        self.driver.execute_script("mobile:shell",opts)              
    def press7(self):
#         clickPoint = self.util.ClickPoint((658,1441),(736,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)    
        opts={'command':'input','args':['keyevent',KEYCODE_7]}
        self.driver.execute_script("mobile:shell",opts)           
    def press8(self):
#         clickPoint = self.util.ClickPoint((764,1441),(846,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)   
        opts={'command':'input','args':['keyevent',KEYCODE_8]}
        self.driver.execute_script("mobile:shell",opts)           
    def press9(self):
#         clickPoint = self.util.ClickPoint((872,1441),(943,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        opts={'command':'input','args':['keyevent',KEYCODE_9]}
        self.driver.execute_script("mobile:shell",opts)        
    def press0(self):
#         clickPoint = self.util.ClickPoint((978,1441),(1058,1535))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)     
        opts={'command':'input','args':['keyevent',KEYCODE_0]}
        self.driver.execute_script("mobile:shell",opts)        
    def pressQ(self):
#         clickPoint = self.util.ClickPoint((21,1566),(104,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)
        opts={'command':'input','args':['keyevent',KEYCODE_Q]}
        self.driver.execute_script("mobile:shell",opts)        
    def pressW(self):
        #clickPoint = self.util.ClickPoint((128,1566),(211,1683))
        #opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
        #self.driver.execute_script("mobile:shell",opts)
        
        opts={'command':'input','args':['keyevent',KEYCODE_W]}
        self.driver.execute_script("mobile:shell",opts)
    def pressE(self):
#         clickPoint = self.util.ClickPoint((235,1566),(314,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)     
        opts={'command':'input','args':['keyevent',KEYCODE_E]}
        self.driver.execute_script("mobile:shell",opts)                     
    def pressR(self):
#         clickPoint = self.util.ClickPoint((340,1566),(419,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)       
        opts={'command':'input','args':['keyevent',KEYCODE_R]}
        self.driver.execute_script("mobile:shell",opts)        
    def pressT(self):
#         clickPoint = self.util.ClickPoint((446,1566),(526,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)     
        opts={'command':'input','args':['keyevent',KEYCODE_T]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressY(self):
#         clickPoint = self.util.ClickPoint((552,1566),(632,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_Y]}
        self.driver.execute_script("mobile:shell",opts)             
    def pressU(self):
#         clickPoint = self.util.ClickPoint((658,1566),(736,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        opts={'command':'input','args':['keyevent',KEYCODE_U]}
        self.driver.execute_script("mobile:shell",opts)              
    def pressI(self):
#         clickPoint = self.util.ClickPoint((764,1566),(846,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)      
        opts={'command':'input','args':['keyevent',KEYCODE_I]}
        self.driver.execute_script("mobile:shell",opts)        
    def pressO(self):
#         clickPoint = self.util.ClickPoint((872,1566),(943,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        opts={'command':'input','args':['keyevent',KEYCODE_O]}
        self.driver.execute_script("mobile:shell",opts)        
    def pressP(self):
#         clickPoint = self.util.ClickPoint((978,1566),(1058,1683))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_P]}
        self.driver.execute_script("mobile:shell",opts)                                                                      
    def pressA(self):
#         clickPoint = self.util.ClickPoint((74,1715),(159,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)
        opts={'command':'input','args':['keyevent',KEYCODE_A]}
        self.driver.execute_script("mobile:shell",opts)        
    def pressS(self):
#         clickPoint = self.util.ClickPoint((179,1715),(261,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_S]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressD(self):
#         clickPoint = self.util.ClickPoint((286,1715),(368,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_D]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressF(self):
#         clickPoint = self.util.ClickPoint((392,1715),(472,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_F]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressG(self):
#         clickPoint = self.util.ClickPoint((498,1715),(579,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        opts={'command':'input','args':['keyevent',KEYCODE_G]}
        self.driver.execute_script("mobile:shell",opts)           
    def pressH(self):
#         clickPoint = self.util.ClickPoint((605,1715),(685,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)
        opts={'command':'input','args':['keyevent',KEYCODE_H]}
        self.driver.execute_script("mobile:shell",opts)            
    def pressJ(self):
#         clickPoint = self.util.ClickPoint((710,1715),(789,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_J]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressK(self):
#         clickPoint = self.util.ClickPoint((816,1715),(896,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_K]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressZ(self):
#         clickPoint = self.util.ClickPoint((179,1866),(261,1985))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)   
        opts={'command':'input','args':['keyevent',KEYCODE_Z]}
        self.driver.execute_script("mobile:shell",opts)           
    def pressX(self):
#         clickPoint = self.util.ClickPoint((286,1866),(368,1985))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_X]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressC(self):
#         clickPoint = self.util.ClickPoint((392,1866),(472,1985))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)

        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_C]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressV(self):
#         clickPoint = self.util.ClickPoint((498,1866),(579,1985))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_V]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressB(self):
#         clickPoint = self.util.ClickPoint((605,1866),(685,1985))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_B]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressN(self):
#         clickPoint = self.util.ClickPoint((710,1866),(789,1985))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_N]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressM(self):
#         clickPoint = self.util.ClickPoint((816,1866),(896,1985))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  
        opts={'command':'input','args':['keyevent',KEYCODE_M]}
        self.driver.execute_script("mobile:shell",opts)                 
    def pressL(self):
#         clickPoint = self.util.ClickPoint((926,1715),(1004,1835))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        opts={'command':'input','args':['keyevent',KEYCODE_L]}
        self.driver.execute_script("mobile:shell",opts)                                                                   
    
    def ADBInput(self,str):
        clickPoint = self.util.ClickPoint((926,1715),(1004,1835))
        opts={'command':'input','args':['text',str]}
        self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)  

    def pressSpace(self):
#         clickPoint = self.util.ClickPoint((413,2000),(663,2135))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)
        opts={'command':'input','args':['keyevent',KEYCODE_SPACE]}
        self.driver.execute_script("mobile:shell",opts)          
        
    def pressDelete(self):
#         clickPoint = self.util.ClickPoint((926,1866),(1058,1985))
#         opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
#         self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)
        opts={'command':'input','args':['keyevent',KEYCODE_DEL]}
        self.driver.execute_script("mobile:shell",opts)          
    def pressLowHighCase(self):
        clickPoint = self.util.ClickPoint((21,1866),(156,1985))
        opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
        self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
    def pressChineseEnglish(self):
        self.width=self.driver.get_window_size().get('width')
        self.height=self.driver.get_window_size().get('height')
        if self.width ==720 and self.height==1366:
            #coolpad
            self.clickAAbsolutePoint((531,1315),(600,1400))
        else:
            #switch Chinese to English
            clickPoint = self.util.ClickPoint((796,2000),(893,2135))
            opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
            self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
        
    def clickAPoint(self,fromPoint,toPoint):
        clickPoint = self.util.ClickPoint(fromPoint,toPoint)
        opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
        self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30) 
    def clickAAbsolutePoint(self,fromPoint,toPoint):
        clickPoint = self.util.ClickAbsolutePoint(fromPoint,toPoint)
        opts={'command':'input','args':['tap',clickPoint[0],clickPoint[1]]}
        self.driver.execute_script("mobile:shell",opts)
        #sleep(random.randint(1,2)/30)         
    def swip(self,fromPoint,toPoint):
        opts={'command':'input','args':['swipe',fromPoint[0],fromPoint[1],toPoint[0], toPoint[1], '300']}
        self.driver.execute_script("mobile:shell",opts)

    