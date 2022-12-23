# printing numbers in right angle triangle

# CODE-I:-
n = int(input("Enter the number of rows:- ")) #it stored the no. of rows

for i in range(1,n+1): # for loop for rows
    for j in range(1,i+1): # for loop for columns
# 'i' represents row, so for columns we take 'i+1' 
# cauz for row 2 colomn is 2 & for row 5 colomn is 5 & if we write only 'i'
# so for row 2 colomn is 1 & for row 5 colomn is 4
        print(j,end= "") # we dont want any space or new line after one no. so we add empty string
    print() # this is for to print loop in next line

# CODE-II:- same code with 1 change to print different digit format
n = int(input("Enter the number of rows:- "))
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print(i,end= "") # instead 'j' we write 'i' here
    print()

# CODE-II:- right angle with star '*'
n = int(input("Enter the number of rows:- "))
for i in range(1,n+1): 
    for j in range(1,i+1): 
        print("*",end="") # if we remove 'end' then it prints in a vertical line not in a traingle shape.
    print()
