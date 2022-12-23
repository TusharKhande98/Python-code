''' Factorial of non-negative integer --->n!
 5! = 5 x 4 x 3 x 2 x 1 = 120
NOTE:- factorial of '0' & '1' is '1'---> 0! = 1

Three ways to write this prigram in python-->
3. by using iterative - for loop
'''

# CODE-III:- By for loop
n = int(input("Enter the number:- "))
result = 1 # we want to multiply not addition, so we give value '1' not '0'
for i in range(n,0,-1): # inputed value to zero with reverse serie-->if n=5 then 5,4,3,2,1('0'excluded)
    result = result*i
'''
Above for loop run like as below condition
suppose,i=4 condition true then... 
result = result*i---> result=1*4=4
        then i=3 so result= 4x3=12
        then i=2 so result= 12x2=24
        then i=1 so result= 24x1=24
'''    
print("Factorial of",n,"is",result)
