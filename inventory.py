#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:15:10 2022

"""
# Authors: Jenny Doan and Mara White

class Inventory: 
    def __init__(self, new_id, new_name, new_stock, new_price): 
        self.__id = new_id
        self.__name = new_name
        self.__stock = new_stock
        self.__price = new_price
    
    # accessors 
    def get_id(self):
        return self.__id
    def get_name(self): 
        return self.__name
    def get_stock(self):
        return self.__stock
    def get_price(self): 
        return self.__price
    
    # look at notes for this one- she said it was a little complicated
    def restock(self, new_stock):
        if -(int(new_stock)) >= 0:
            self.__stock = int(self.__stock) - new_stock
            return True
        else: 
            return False
        
    def purchase(self, purch_qty): 
        if purch_qty <= int(self.__stock): 
            self.__stock = int(self.__stock) - purch_qty
            return True
        else: 
            return False
    
    # look at example string function
    def __str__(self): 
        # format to print menu of attributes
        # center align price and qty for formatting preference
        var = "{:<10}{:<28}{:<20}{:<1}".format(self.__id, self.__name, self.__price, self.__stock)
        return var
  
        
        
        
        
