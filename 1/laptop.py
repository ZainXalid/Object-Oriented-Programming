from item import Item

class Laptop(Item):

    pay_rate = 0.5
    
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        
