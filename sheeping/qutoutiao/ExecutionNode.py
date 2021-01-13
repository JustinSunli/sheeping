# coding: utf-8

class ExecutionNode():
    def __init__(self, priority=1, automation=None):
        self.priority=priority
        self.automation=automation
    
    def __lt__(self,other): 
        return self.priority < other.priority        
            
    
