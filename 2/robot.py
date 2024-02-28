from worker import Worker

#Inheritance
class Robot(Worker):
    
    def __ini__(self,name, title, tasks_completed, years_in_service, service_life = 1, initial_cost = 0, damaged = False,):
        super().__init(name, title, tasks_completed, years_in_service)
        
        assert service_life > 0, "service_life cannot be less than 0"
        assert initial_cost >= 0, "initial_cost cannot be less than 0"
        
        self.__service_life = service_life
        self.__initial_cost = initial_cost
        self.damaged = damaged
        
        self.__repair_cost = 0
        self.__number_of_repairs = 0
        
    #Encapulation
    @property
    def get_service_life(self):
        return self.__service_life
    
    @get_service_life.setter
    def set_service_life(self, years):
        if(years<= 0):
            raise Exception("Service Life cannot be 0 or less")
        else:
            self.__service_life = years
            
    @property
    def get_initial_cost(self):
        return self.__initial_cost
    
    @get_initial_cost.setter
    def set_initial_cost(self, cost):
        if(cost < 0):
            raise Exception("Initial cost cannot be 0 or less")
        else:
            self.__initial_cost = cost
            
    @property
    def get_repair_cost(self):
        return self.__repair_cost
    
    @get_repair_cost.setter
    def set_repair_cost(self, cost):
        if(cost <= 0):
            raise Exception("Repair cost cannot be less than 0")
        else:
            self.__repair_cost = self.__repair_cost + cost
            self.__number_of_repairs = self.__number_of_repairs + 1
            
    
    def average_yearly_breakdowns(self):
        if(self.__years_in_service <= 0):
            print(f"{self.__name} has yet to complete first year")
        else:
            print(f"{self.__name} has {self.__number_of_repairs / self.__years_in_service} breakdowns per years")
            
    def is_fit_for_service(self):
        if(self.__years_in_service >= self.__service_life):
            print(f"No, {self.__name}'s {self.__service_life} years of service life has ended")
            
        elif((self.__number_of_repairs / self.__years_in_service) > 24):
            print(f"No longer fit for service with f{self.__number_of_repairs / self.__years_in_service} yearly breakdowns")
        else:
            print(f"Yes, {self.__name} is fit for service")
    
    #Method Overriding
    def Availability(self):
        if(self.__years_in_service >= self.__service_life ):
            print(f"No, {self.__name}'s {self.__service_life} years of service life has ended")
        elif(self.damaged):
            print(f"{self.__name} is currently damaged")
        else:
            print(f"{self.__name} is available")
            
    def total_cost(self):
        return self.__initial_cost + self.__repair_cost
    