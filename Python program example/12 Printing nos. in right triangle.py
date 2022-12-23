# CODE-I:- 
n = int(input("Enter the number of rows:- "))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,end="" )
    print()
#  CODE-II:-    
n = int(input("Enter the number of rows:- "))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row,end="" )
    print()
