'''
GROUP NUMBER:
    I4

GROUP ELEMENTS:
    32301, 43529, 39001, 23921
'''

dict1={"username": "pedro",                              #Creating our dictionaries here
       "password": "pedro"}
dict2={"username": "joana",
       "password": "joana"}
dict3={"username": "maria",
       "password": "maria"}
dict4={"username": "admin",
      "password": "admin"}

def login_menu():                                        #We use this function with a control variable for the while loop
    control_variable = True 
    while control_variable:
        print("\n1. Login\n2. Exit")
        option = int(input("Please select one option from the menu: ")) #Our goal is to have the user input an integer
        if option == 1:                                  #If the integer is the one on the menu, everything is OK
            login()
        elif option == 2:
            control_variable = False
            print("\nGoodbye.")                          #We had some problems with exiting the function in later parts of the code
            import os                                    #if the option == 2, which is why we resorted to importing os and forcing the
            os._exit(0)                                  #code to quit for that specific case
        else:
            print("\nPlease select a valid option.")
            login_menu()
    return

a=3                                                        #Here we are setting variable values to use later to check if the user is blocked or not
b=3
c=3
d=3
user_unlocked_a=True
user_unlocked_b=True
user_unlocked_c=True
user_unlocked_d=True

def login():                                               #In this function we are checking if the input username belongs in any of the 4 dictionaries
    user = str(input("Please insert your username: "))  
    if user in dict1["username"]:                          #If it does, we ask for a password
        password=str(input("Please insert your password: "))
        global a
        a-=1                                               #For each password try we are taking one of the tries away
        global user_unlocked_a
        while user_unlocked_a:                             #Then we are checking if the input password belongs in the same dictionary as the username
            if password in dict1["password"]:
                menu_client(user)                          #If it does, we call the next function
            else:
                print("\nWrong password.")                 #If it doesn't, we call the initial login menu again. Here, we recommend you trying the wrong password "z" instead of the wrong password "e"
                if a<=0:                                   #After the user reaches zero tries, the program blocks it
                    print("Wrong password.\nUser "+ user + " is locked. Contact bank administrator.")
                    user_unlocked_a = False
                    login_menu()
                else:
                    print("You have",str(a),"attempts to login.")
                    login_menu()
        else:
            print("\nUser "+ user + " is locked. Contact bank administrator.")
            login_menu()
            
    elif user in dict2["username"]:                      #Here we are doing the same as before but checking for the second dictionary
        password=str(input("Please insert your password: "))
        global b
        b-=1
        global user_unlocked_b
        while user_unlocked_b:
            if password in dict2["password"]:
                menu_client(user)        
            else:
                print("\nWrong password.")               #Here, we recommend you trying the wrong password "z" instead of the wrong password "e"
                if b<=0:
                    print("Wrong password.\nUser "+ user + " is locked. Contact bank administrator.")
                    user_unlocked_b = False
                    login_menu()
                else:
                    print("You have",str(b),"attempts to login.")
                    login_menu()
        else:
            print("\nUser "+ user + " is locked. Contact bank administrator.")
            login_menu()
                    
    elif user in dict3["username"]:                      #Here we are doing the same as before but checking for the third dictionary
        password=str(input("Please insert your password: "))
        global c
        c-=1
        global user_unlocked_c
        while user_unlocked_c:
            if password in dict3["password"]:
                menu_client(user)        
            else:
                print("\nWrong password.")               #Here, we recommend you trying the wrong password "z" instead of the wrong password "e"
                if c<=0:
                    print("Wrong password.\nUser "+ user + " is locked. Contact bank administrator.")
                    user_unlocked_c = False
                    login_menu()
                else:
                    print("You have",str(c),"attempts to login.")
                    login_menu()
        else:
            print("\nUser "+ user + " is locked. Contact bank administrator.")
            login_menu()
                    
    elif user in dict4["username"]:                      #Here we are doing the same as before but checking for the fourth dictionary
        password=str(input("Please insert your password: "))
        global d
        d-=1
        global user_unlocked_d
        while user_unlocked_d:
            if password in dict4["password"]:
                menu_admin(user)        
            else:
                print("\nWrong password.")               #Here, we recommend you trying the wrong password "z" instead of the wrong password "e"
                if d<=0:
                    print("Wrong password.\nUser "+ user + " is locked. Contact bank administrator.")
                    user_unlocked_d = False
                    login_menu()
                else:
                    print("You have",str(d),"attempts to login.")
                    login_menu()
        else:
            print("\nUser "+ user + " is locked. Contact bank administrator.")
            login_menu()
    else:
        print("\nUser does not exist.")
        login_menu()

def menu_admin(user):                                   #We wanted to do a simple function for the menu, so it simply takes the input and calls the correct function
    print("\nHello admin\n\n1. Admin options\n2. Logout")
    option = int(input("Please select one option from the menu: "))
    if option == 1:
        menu_admin(user)
    elif option == 2:
        print("\nGoodbye admin.")
        login_menu()
    else:
        print("\nPlease select a valid option.")
        menu_admin(user)

def menu_client(user):                                 #We wanted to do a simple function for the menu, so it simply takes the input and calls the correct function
    print("\nHello client", user, ".\n\n1. Client options\n2. Logout")
    option = int(input("Please select one option from the menu: "))
    if option == 1:
        menu_client(user)
    elif option == 2:
        print("\nGoodbye", user, ".")
        login_menu()
    else:
        print("\nPlease select a valid option.")
        menu_client(user)

print("Welcome to Bank Rupt.")
login_menu()