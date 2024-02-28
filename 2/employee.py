from worker import Worker

#Inheritance
class Employee(Worker):
    def __init__(self,name, title, salary:float, age_in_years:int, tasks_completed = 0, years_in_service = 0 ):
        super().__init__(name, title, tasks_completed, years_in_service)
        
        assert salary >= 0, "Salary cannot be less than zero"
        assert age_in_years >= 1, "Age cannot be less than or equal to zero" 
        
        self.__salary = salary
        self.__age_in_years = age_in_years
        
        self.__onleave = False
        self.__inservice = True
        
    #Encapsulation
    @property
    def get_salary(self):
        return self.__salary
        
    @get_salary.setter
    def set_salary(self, salary):
        if salary < 0:
            raise Exception("Salary cannot be less than zero")
        else:
            self.__salary = salary
    
    @property
    def get_onleave(self):
        return self.__onleave
    
    @get_onleave.setter
    def set_onleave(self, value):
        if(type(value) != bool):
            raise Exception("Value must be a boolean! True/False")
        else:
            if self.__onleave == False:
                self.__onleave = True
            else:
                self.__onleave = False
 
    def retirement_benefit_eligibility(self):
        if(self.__years_in_service >= 20):
            print(f"{self.__name} is eligible for retirement benefits")
    
    def separate(self):
        self.__inservice = False
   
    #Method Overriding            
    def Availability(self):
        if(not self.__inservice):
            print(f"{self.name} is no longer in service")
        if(self.__onleave):
            print(f"{self.__name} is on temporary leave")
    
    def total_cost(self):
        return self.__salary + self.__years_in_service
    
emp1 = Employee(name="Zain", title="CEO", salary=1000000, age_in_years=28 ) 
emp1.set_salary = 2000000
print(emp1.get_salary)