# Printing nos. in right triangle
# Floyd's triangle 

n = int(input("Enter the number of rows:- "))   
num = 1
for row in range(1,n+1): # if n=4 then it will be 1,2,3,4 cauz we give 'n+1' not only 'n'
# in below line we want 1 colomn in row-1 the 2 colomn in row-2... 4 colomn in row-4
    for col in range(1,row+1): # it means 1 to row+1 colomn itmeans 1 to 1, 1 to n
        print(num,end=" ")
        num = num+1
    print()
