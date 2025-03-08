def draw():
    side_size = int(input("Insert the square size: "))
    
    if side_size<2:
        print("Minimal square size is 2.")
        
    else:
        for i in range(side_size):
            print (("* ") * side_size)
            
draw()