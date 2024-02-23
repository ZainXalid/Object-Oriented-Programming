# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 05:49:02 2024

@author: mzain
"""

class item():
    
    pay_rate = 0.8 # 20% Discount
    all = []
    
    def __init__(self, name : str, price : int, quantity=1):
        #Run validations to recived arguments        
        assert price >= 0, f"Price {price} is not >= 0"
        assert quantity >= 0, f"Quantity {quantity} is not >= 0"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity        
        
        #Action
        item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    def __repr__(self):
        return f"Item ('{self.name}', {self.price}, {self.quantity})"

item1 = item('Phone',100,1)
item2 = item('Laptop',1000,1)

#print('Total Price  ',item1.calculate_total_price())

item1.apply_discount()
item2.apply_discount()

#print(item1.calculate_total_price())
#print(item2.calculate_total_price())

print(item.all)