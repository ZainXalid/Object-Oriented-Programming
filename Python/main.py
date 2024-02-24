# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 05:49:02 2024

@author: mzain
"""
from item import Item
from phone import Phone 
from laptop import Laptop 

#Inheritance
item1 = Item('Remote', 10, 2)
phone1 = Phone('iPhone', 1500, 1, 0)
laptop1 = Laptop('Asus', 3000, 1)

#Encapsulation
print(phone1.get_name)
phone1.set_name = 'Pixel'
print(phone1.get_name)

#Polymorphism
phone1.apply_discount()
laptop1.apply_discount()
print(phone1.price) 
print(laptop1.price) 

#Abstraction
phone1.send_email()
