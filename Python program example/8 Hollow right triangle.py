# we wrote same code before it, shape is same but in diff. direction

n = int(input("Enter the number of rows:- "))
for row in range(0,n): # '0' to 'nth' value for row
    for col in range (0,n): # '0' to 'nth' value for colomn
        if row==0 or col==(n-1) or row==col:
            print("*",end="")
        else:
            print(end=" ")
    print() # this print is for, after printing * in 1 line it goes to second line
