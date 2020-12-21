# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 12:44:07 2020

@author: ASUS
"""
class ATMCard:
    def __init__(self,defaultPin,defaultBalance):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance
        
    def getPin(self):
        return self.defaultPin
    
    def getSaldo(self):
        return self.defaultBalance
            
