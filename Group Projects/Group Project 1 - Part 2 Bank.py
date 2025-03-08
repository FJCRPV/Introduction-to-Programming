'''
GROUP NUMBER: I4
GROUP ELEMENTS: 32301, 43529, 39001, 23921
'''
from myuser import User

admin = User("admin", "admin", user_type="admin")       #Here we are setting the attribute values for each of our users
joao = User("joao", "joao")
pedro = User("pedro", "pedro", balance=100, lock_status=True)

user_list = [admin, joao, pedro]

def login():
    user = None
    usr = input("Please insert your username: ")
    for u in user_list:
        if usr == u.get_username():          #We changed this line in the code before to use the class instead of a dictionary
            user = u
    if user != None:
        attempts = 3
        while attempts != 0:
            pwd = input("Please insert your password: ")
            if user.get_password() == pwd:     #We changed this line in the code before to use the class instead of a dictionary
                if user.get_lock_status() == False:
                    return user
                else:
                    print("User is locked. Contact bank administrator.\n")
                    break
            else:
                attempts -= 1
                print("Wrong password.")
                if attempts == 0:
                    user.change_lock_status(True)     #We changed this line in the code before to use the class instead of a dictionary
                    print("User" + user.get_username() +
                          "is locked. Contact bank administrator.\n")
                else:
                    print("You have" + str(attempts) + "attempts to login.")
    else:
        print("User does not exist.")
    return None



'''
YOUR NEW FUNCTIONS GO HERE
START
'''



def client_options(user):              #Creating a menu similar to the previous menus
    loop = True
    while loop:
        print("\n1. View balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Transfer money")
        print("0. Back")
        option = int(input("Please select one option from the menu: "))
        if option == 0:
            loop = False
        elif option == 1:
            print("\nYour account balance is: ", user.get_balance())    #We retrieve the user balance and print it out
        elif option == 2:
            deposit_amount=float(input("\nPlease insert the deposit value: "))  #We call a method to add the input funds to the user balance
            user.deposit(deposit_amount)
            print("\nYour current balance is: ", user.get_balance())    #And print the final balance
        elif option == 3:
            withdraw_amount=float(input("\nPlease inser the withdraw value: "))  #We call another method to take funds from the user balance instead
            user.withdraw(withdraw_amount)
            print("\nYour current balance is: ", user.get_balance())    #And print the final balance
        elif option == 4:         #Here we ask for the destination and the transfer amount
            transfer_destination=str(input("\nPlease insert the client to transfer the funds: "))
            transfer_amount=float(input("\nPlease insert the amount to transfer to " + transfer_destination + ": "))
            user.transfer(transfer_amount, transfer_destination)  #And call the method do make the transfer

'''
END
'''


def menu_admin(user):
    print("\nhello", user.get_user_type(), user.get_username(), "\n")      #We changed this line in the code before to use the class instead of a dictionary
    loop = True
    while loop:
        print("1. Admin options")
        print("0. Logout")
        option = int(input("Please select one option from the menu: "))
        if option == 0:
            loop = False
            print("\nGoodbye", user.get_username() + ".\n")       #We changed this line in the code before to use the class instead of a dictionary
        elif option == 1:
            admin_options(user)
        else:
            print("Please select a valid option.")


def menu_client(user):
    print("\nhello", user.get_user_type(), user.get_username(), "\n")     #We changed this line in the code before to use the class instead of a dictionary
    loop = True
    while loop:
        print("1. Client options")
        print("0. Logout")
        option = int(input("Please select one option from the menu: "))
        if option == 1:
            client_options(user)
        elif option == 0:
            loop = False
            print("\nGoodbye", user.get_username() + ".\n")       #We changed this line in the code before to use the class instead of a dictionary
        else:
            print("Please select a valid option.")


def login_menu():
    choice = None
    print("Welcome to Bank Rupt.\n")
    while choice != 0:
        print("1. Login")
        print("2. Exit")
        choice = int(input("Please select one option from the menu: "))
        if choice == 1:
            user = login()
            if user != None:
                if user.get_user_type() == "admin":         #We changed this line in the code before to use the class instead of a dictionary
                    menu_admin(user)
                else:
                    menu_client(user)
        elif choice == 2:
            print("Goodbye")
            break
        else:
            print("Please select a valid option.")

login_menu()