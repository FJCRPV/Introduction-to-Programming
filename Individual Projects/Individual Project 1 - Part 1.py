import random
secret_number=random.randint(1,100)
i=int(input("Choose a number: "))
t=1
while i!=secret_number:
    if i<secret_number:
        print("Is bigger")
        i=int(input("Choose a number: "))
        t+=1
        if t==7:
            print ("Game over")
            print ("Secret number: " + str(secret_number))
            print ("Attempts: " + str(t))
            break
    elif i>secret_number:
        print("Is smaller")
        i=int(input("Choose a number: "))
        t+=1
        if t==7:
            print ("Game over")
            print ("Secret number: " + str(secret_number))
            print ("Attempts: " + str(t))
            break
if i==secret_number:
    print ("You found it!")
    print ("Secret number: "+ str(secret_number))
    print ("Attempts: " + str(t))