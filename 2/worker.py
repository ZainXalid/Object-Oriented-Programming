class Worker():
    
    def __init__(self, name: str, title: str, tasks_completed = 0, years_in_service = 0):
        
        assert len(name) >= 3, "name must be three charaters atleast"
        assert len(title) >= 3, "title must be three characters atleast"
        assert tasks_completed >= 0, "tasks_completed must be greater than or equal to zero"
        assert years_in_service >= 0, "task_completed must be greater than or equal to zero"
        
        self.__name = name
        self.__title = title
        self.__tasks_completed = tasks_completed
        self.__years_in_service = years_in_service
    
    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def set_name(self, name):
        if(len(name)>= 3):
            self.__name = name
        else:
            raise Exception("name must be three charaters atleast")
        
    @property
    def get_title(self):
        return self.__title
    
    @get_title.setter
    def set_title(self, title):
        if(len(title)>= 3):
            self.__title = title
        else:
            raise Exception("title must be three charaters atleast")
    
    @property
    def get_tasks_completed(self):
        return self.__tasks_completed
    
    # @get_tasks_completed.setter
    def increment_tasks_completed(self):
        self.__tasks_completed = self.__tasks_completed + 1
        
    @property
    def get_years_in_service(self):
        return self.__years_in_service
    
    # @get_years_in_service.setter
    def increment_years_in_service(self):
        self.__years_in_service = self.__years_in_service + 1
    
    def efficieny(self):
        if(self.__years_in_service == 0):
            raise Exception(f"{self.__name} has not completed 1 year yet.")
        else:
            return f"{(self.__tasks_completed / self.__years_in_service) * 100} %"
    
    def Availability(self):
        pass
    
    def total_cost(self):
        pass
    
wrk1 = Worker("LML-1", "Welder" )
wrk1.increment_tasks_completed()
wrk1.increment_years_in_service()
print(wrk1.efficieny())