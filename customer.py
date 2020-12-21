# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:08:01 2020

@author: ASUS
"""
import atm_card

class Customer:
    def __init__(self,id,custPin,custBalance):
        self.custPin = 1234
        self.custBalance = 10000
        self.id = id

    def getId(self):
        return self.id
    
    def getCustPin(self):
        return self.custPin
    
    def getCustBalance(self):
        return self.custBalance
    
    def Debet(self,nominal):
        if nominal <= self.custBalance :
            sisa = self.custBalance - nominal
            return 'Saldo Anda Saat Ini : ' + str(sisa)
        else :
            return 'Saldo Anda Tidak Mencukupi'
    def Withdrawal(self,nominal):
        if nominal <= self.custBalance :
            sisa = self.custBalance - nominal
            return 'Your Current Balance : ' + str(sisa)
        else :
            return 'Your Balance is Insufficient'
    def Simpan(self,nominal):
        return self.custBalance + nominal
    