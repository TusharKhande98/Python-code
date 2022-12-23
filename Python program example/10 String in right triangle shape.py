string = input("Enter the string:- ")
length = len(string)
for row in range(length): # it means '0' to our length
    for col in range(row+1): # it means '0' to our row value
        print(string[col],end="")
    print()