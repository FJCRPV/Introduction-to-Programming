'''
GROUP NUMBER: I4
GROUP ELEMENTS: 32301, 43529, 39001, 23921
'''


class User:

    def __init__(self, password, username, balance=0, lock_status=False, user_type="client"):
        self.__balance = balance
        self.__lock_status = lock_status
        self.__password = password
        self.__user_type = user_type
        self.__username = username

    def get_balance(self):
        return self.__balance

    def get_lock_status(self):
        return self.__lock_status

    def get_password(self):
        return self.__password

    def get_user_type(self):
        return self.__user_type

    def get_username(self):
        return self.__username

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            print("\nPlease deposit a positive amount.")
        else:
            self.__balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if self.__balance < withdraw_amount:
            print("\nYou do not have funds for this withdraw.")
        else:
            self.__balance -= withdraw_amount

    def change_balance(self, new_balance):
        self.__balance = new_balance
        
    def transfer(self, transfer_amount, transfer_destination):
        if self.__balance < transfer_amount:
            print("\nYou don't have funds for this transfer.")
        else: 
            self.__balance -= transfer_amount  
            print("\nThe amount of", transfer_amount, "was transfered to", transfer_destination + ".")

    def change_lock_status(self, lock_status):
        if (self.__lock_status == False) and (lock_status == False):
            print("The selected client is not locked.")
        elif (self.__lock_status == True) and (lock_status == True):
            print("The selected client is locked.")
        else:
            self.__lock_status = lock_status