import csv

class Item():
    
    pay_rate = 0.8 # 20% Discount
    all = []
    
    def __init__(self, name : str, price : int, quantity=1):
        #Run validations to recived arguments        
        assert price >= 0, f"Price {price} is not >= 0"
        assert quantity >= 0, f"Quantity {quantity} is not >= 0"

        #Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity        
        
        #Action
        Item.all.append(self)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter    
    def name(self, value):
        if len(value) > 10:
            raise Exception('Name can not be greater than 10 characters')
        else:
            self.__name = value
            
    @property
    def price(self):
        return self.__price

    def apply_increment(self, value):
        self.__price = self.__price + self.__price * value

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def calculate_total_price(self):
        return self.__price * self.quantity
     
    @classmethod
    def instantiate_from_csv(cls): #mandatory class (cls) reference 
        '''
        Different from @static method in a sense that it still has relation 
        with this class (has use only for this class) but usually do
        mainpulate data structure to instantiate objects, like we 
        do with csv
        
        Main Difference is mandatory class (cls) reference
        '''
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(            
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
    
    @staticmethod        
    def is_integer(num): #no mandatory reference like cls or self
        '''
        Different from @classmethod in a sense that it still has relation 
        with this class (has use only for this class) 
        but is not unique per instance!
        
        Main Difference is no mandatory reference like cls or self
        '''
        
        #Return True for integer even if a float has point zeros
        if isinstance(num, float):
            return num.is_integer()#built in is_integer
        elif isinstance(num, int):
            return True
        else:
            return False
        
    
    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', {self.__price}, {self.quantity})"

