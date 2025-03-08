"""
Group 2
Exercises 1, 2, 3, 4 and 5
Francisco Perestrello, 39001
"""


character_list = [
                {
                "name":"Thanos",
                "avenger":False,
                "powers":{
                            "strength":100,
                            "intelligence": 80,
                            "magic":100,
                            "humor": 10
                        }
                
                },
                {
                "name":"Iron Man",
                "avenger":True,
                "powers":{
                            "strength":80,
                            "intelligence": 100,
                            "magic":0,
                            "humor": 90
                        }
                
                },
                {
                "name":"Captain America",
                "avenger":True,
                "powers":{
                            "strength":80,
                            "intelligence": 90,
                            "magic":0,
                            "humor": 50
                        }
                
                },
                {
                "name":"Hulk",
                "avenger":True,
                "powers":{
                            "strength":95,
                            "intelligence": 10,
                            "magic":10,
                            "humor": 70,
                        }
                
                },
                {
                "name":"Loki",
                "avenger":False,
                "powers":{
                            "strength":70,
                            "intelligence": 90,
                            "magic":90,
                            "humor": 80
                        }
                },
        ]

    
def print_character(character_list):
          
            if character_list["avenger"] == True:
                print("Avenger {}".format(character_list["name"]))
                
                for power in character_list["powers"]:
                    print("{}{}: {}".format("\t", power, character_list["powers"][power]))
                
            if character_list["avenger"] == False:
                print("Villain {}".format(character_list["name"]))
                
                for power in character_list["powers"]:
                    print("{}{}: {}".format("\t", power, character_list["powers"][power]))
                
#TEST
#print_character(character_list[1])


def print_characters():
    char_filter = str(input("Which characters do you want to list? "))
    
    if char_filter.lower() == "all":      
        for i in range(len(character_list)):
            print_character(character_list[i])        
    
    if char_filter.lower() == "avengers":
        print_character(character_list[1])
        print_character(character_list[2])
        print_character(character_list[3])
    
    if char_filter.lower() == "villains":
        print_character(character_list[0])
        print_character(character_list[4])

    
#TEST           
#print_characters()

 
def add_character(char_name, bool):           #Could not finish. - Will comment
    
        if char_name in character_list["name"]:   #Trying to print if it already exists
            print("Character {} already exists.".format(char_name))
        else:
            new_char = {} #add a dictionary that is the new character
            powers={}  #add its powers
            import random
            powers.update({"strength": random.randint(1,100), "intelligence": random.randint(1,100), "magic": random.randint(1,100), "humor": random.randint(1,100)}) #assigning values to powers
            new_char.update({"name": char_name, "avenger": bool, "powers": powers}) #update the dict of new char
            character_list.append(new_char) #append it to the inicial list of characters
            print("Character {} created with success.".format(char_name))

    
#demo data to add new characters to your list   
#add_character("Ant-man", True)
#add_character("Ant-man", True)
#add_character("Hawkeye", True)
#add_character("Red Skull", False)
#add_character("Ultron", False)
#TEST
#print_characters()


def remove_not_funny(humor_level):
    
    for i in range(len(character_list)): 
        if character_list[i]["powers"]["humor"] <= humor_level: 
            del character_list[i]
        else:
            break
            
#TEST
#remove_not_funny(65)
#print_characters()

def battle():
    import random
    char_1 = character_list[random.randint(1, len(character_list)-1)]
    char_2 = character_list[random.randint(1, len(character_list)-1)]
    char_1_name = char_1["name"]
    char_2_name = char_2["name"]
    
    while True:
        if char_1_name == char_2_name:
            print("One cannot battle himself.")
            break
        
        else:
            char_1_powers = char_1["powers"]
            char_2_powers = char_2["powers"]
    
            print("A new battle is about to begin betweem...")
            print("\nPlayer1: {}".format(char_1_name))
            print("{}Vs".format("\t"))
            print("Player2: {}".format(char_2_name))
    
            powers = ["strength", "intelligence", "magic", "humor"]
            selected_power = random.choice(powers)
            print("\nThe selected power is...")
            print("{} {}".format("\t", selected_power))
    
            if char_1_powers[selected_power] < char_2_powers[selected_power]:
                print("\nTHE WINNER IS...")
                print ("{}!!!".format(char_2_name))
                break
        
            if char_1_powers[selected_power] > char_2_powers[selected_power]:
                print("\nTHE WINNER IS...")
                print ("{}!!!".format(char_1_name))
                break
        
            if char_1_powers[selected_power] == char_2_powers[selected_power]:
                print ("\nIncredible... We have a tie!")
                break
        
#TEST
#battle()
