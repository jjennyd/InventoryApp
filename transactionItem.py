#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 14:29:35 2022

"""
# Authors: Jenny Doan and Mara White

class TransactionItem:
    def __init__(self, id_num, name, price, quantity): 
        self.__id = id_num
        self.__name= name
        self.__quantity = quantity
        self.__price = price
        
    # accessors
    def get_id(self): 
        return self.__id
    def get_name(self): 
        return self.__name
    def get_stock(self): 
        return self.__quantity 
    def get_price(self):
        return self.__price
    
    # mutators
    def set_id(self, new_id): 
        self.__id = new_id
        return self.__id
    def set_name(self, new_name): 
        self.__name = new_name
        return self.__name
    def set_qty(self, new_qty): 
        self.__quantity = new_qty
        return self.__quantity
    def set_price(self, new_price): 
        self.__price = new_price
        return self.__price
        
    # calculate costs
    def calc_cost(self): 
        cost = float(self.__price) * float(self.__quantity)
        return cost
    
    def __str__(self): 
        # format to create the invoice
        transaction = "{:<10}{:<28}{:<20}{:<8}".format(self.__id, self.__name, self.__price, self.__quantity)
        return transaction
        
