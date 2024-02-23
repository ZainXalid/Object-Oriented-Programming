# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 05:49:02 2024

@author: mzain
"""
from item import Item
from phone import Phone 


item1 = Item('Remote', 10, 2)
phone1 = Phone('iPhone', 1500, 1)

phone1.apply_increment(0.1)
print(phone1.price) 
