from item import Item

class Phone(Item):

    def __init__(self, name, price, quantity, broken_phone=0):
        super().__init__(name, price, quantity)
        
        #Run validations to recived arguments 
        assert broken_phone >= 0, f'Broken Phone {broken_phone} not greater than or equal to zero'
        
        #Assign to self
        self.broken_phone = broken_phone
