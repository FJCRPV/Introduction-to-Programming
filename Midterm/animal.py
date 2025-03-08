"""
Group 3 
Francisco Perestrello, 39001
"""

class Animal():
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_gender(self):
        return self.__gender
    
    def meals(self):
        return "3"
        
    def animal_to_human(self):
        pass
        
    def __str__(self):
        pass