"""
Group 1 
Exercise 2
Francisco Perestrello, 39001
"""

def postal_code_validator():
    postal_code = str(input("Postal code: "))
        
    if len(postal_code) != 8:
        print("Postal Code length is wrong.")
              
    if postal_code[:4].isdigit() == False:
        print("The first four elements in postal code must be digits.")
               
    if postal_code[5:].isdigit() == False:
        print("The last 3 elements in postal code must be digits.")
                
    if postal_code[4] != "-":
        print("Postal Code must have a hyphen seperating the number in the fifth position.")
            
    if ((len(postal_code) == 8) and (postal_code[:4].isdigit()) and (postal_code[5:].isdigit()) and (postal_code[4] == "-")):
        print("Postal code {} is ok.".format(postal_code))
            
postal_code_validator()