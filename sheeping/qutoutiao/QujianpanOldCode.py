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
                gtype='¸ÉÀ¬»ø'

        fromelement = self.find_element_by_id_without_exception(self.driver, 'garbageImg')
        toelement = None
        if  gtype == 'ÊªÀ¬»ø':
            #move to wet gabage
            toelement = self.find_element_by_id_without_exception(self.driver, 'garbageBlueCon')
            print
        elif gtype == '¿É»ØÊÕ':
            #move to recycle
            toelement = self.find_element_by_id_without_exception(self.driver, 'garbageGreenCon')
            print
        elif gtype == 'ÓÐº¦À¬»ø':
            #move to harmful
            toelement = self.find_element_by_id_without_exception(self.driver, 'garbageRedCon')
            print
        elif gtype == '¸ÉÀ¬»ø':
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
  
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.widget.TextView[@text="·ÖÀ¬»ø×¬½ð±Ò"]/../android.widget.TextView[@text="ÊÔÍæ"]')
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
            file.close()  #¹Ø±ÕÎÄ¼þ        

    def getMoney(self):
        try:
#           #go to zhuan qian tab
            element=self.find_element_by_xpath_without_exception(self.driver, "//android.widget.HorizontalScrollView[@resource-id='com.qujianpan.client:id/tl_home']/android.widget.LinearLayout/*[2]")
            if element:      
                element.click()

            self.driver.switch_to.context('WEBVIEW_com.qujianpan.client')
#             
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.webkit.WebView[@text="×¬Ç®"]/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.view.View[3]')
            if element:
                self.endMoney = element.text
        except Exception:
            self.logger.info("-------"+self.deviceName+"------"+'sigin except!')
            traceback.print_exc()  
    def lookadsgetgifts(self):
        #WEBVIEW_com.qujianpan.client
        sleep(1+random.randint(0,3000)/1000)
        element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="ÁìÈ¡"]')
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
            element = self.find_element_by_xpath_without_exception(self.driver,'//android.view.View[@text="ÁôÔÚÈ¤¼üÅÌ"]')
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