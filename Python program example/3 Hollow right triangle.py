n= int(input("Enter the no. of rows:- "))
for row in range(n): # range is from 0 to 1
    for col in range(n):
        if col==0 or row==(n-1) or row==col:
# col==0-->vertical line(height), row==n-1-->below line(base), row==col-->hypotaneous.            
            print("*",end="")
        else:
            print(end=" ") # it create empty space when 'if condition is false'--> makes hollow shape.
    print() #this has a value '\n' so it goes to next line, after print 1 line every time

            