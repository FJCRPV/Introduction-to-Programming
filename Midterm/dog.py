# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:41:49 2020

@author: Francisco
"""

from animal import Animal

class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        
    def meals(self, meals):
        if self.__age <= 3:
            meals = 5
        elif 3 < self.__age <= 6:
            meals = 4
        else:
            meals = 3
            
    def animal_to_human(self, human_age):
        human_age = self.__age * 5
        return human_age
    
    def __str__(self):
        print("{} is {} years old, but in human years it has {}.\n{} also needs to eat {} times per day!".format(self.__name, self.__age, human_age, self.__name, meals))