from animal import Animal

class Bird(Animal):
    
    def __init__(self, name, age, gender, talk = True):
        super().__init__(name, age, gender)
        self.__talk = bool
       
    def get_talk (self):
        return self.__talk
            
    def add_favorite_words(self, new_words):
        if self.__talk == False:
            print("The bird doesn't talk")
            words = None
        else:
            words = []
            words.append(new_words)
           
    def animal_to_human(self, human_age):
        human_age = self.__age * 8
        return human_age
        
    def print_favorite_words(self):
        if self.__talk == False:
            print("The bird doesn't talk")
            words = None
        else:
            print(words)
        
    def __str__(self):
        print("{} is {} years old, but in human years it has {}".format(self.__name, self.__age, self.__human_age))