"""
Group 1 
Exercise 1
Francisco Perestrello, 39001
"""

def convert():
    temperature = float(input("Insert the temperature you want to convert: "))
    unit = str(input("What are the units? "))
    
    if unit[0].lower() == "f":
        farenheit = ((temperature*9/5)+32)
        print("The temperature is {}{}".format(farenheit,unit[0].upper()))
    
    if unit[0].lower() == "k":
        kelvin = (temperature+273.15)
        print("The temperature is {}{}".format(kelvin,unit[0].upper()))
        
convert()