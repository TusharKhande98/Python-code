n = int(input("Enter how many nos. u want in this series:- ")) 
first = 0
second = 1
for i in range(n):
    print(first)
    temp = first # which is '0' we stored in temp 
    first = second # which is 1 for now
    second = temp + second # here we get addition of first 2 nos 0(first)+1(second)=1
