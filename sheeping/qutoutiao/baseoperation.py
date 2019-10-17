# coding: utf-8
from time import sleep
import traceback 
from selenium.common.exceptions import NoSuchElementException

class AutomationException(Exception):
    
    def __init__(self,message):
        Exception.__init__(self)
        self.message=message
     
class BaseOperation:   
    def __init__(self, deviceName='A7QDU18420000828',version='9',username='18601793121', password='Initial0'):
       self.isFirst = True
       self.sleepseconds = 5
       
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