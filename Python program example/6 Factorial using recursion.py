''' Factorial of non-negative integer --->n!
 5! = 5 x 4 x 3 x 2 x 1 = 120
NOTE:- factorial of '0' & '1' is '1'---> 0! = 1

Three ways to write this prigram in python-->
2. by using recursion (If a function called itself then its a recursive function).
3. by using iterative - for loop

Recursive function have 2 parts-->
1.Base case - it is a stopping condition. 
2.Recursive case - here recursive cond. called itself until stopping condition not arrives.

'''

# CODE-II:- by recursive function
def fact(n):
    if n==0: # its a base conditon
        return 1 # 0!=1
    else:
        return n*fact(n-1) # n!=n(n-1)-->
# 5!=5(5-1)=5x4 so execution paused in above line, then value of 'n' reduce so its,
#  4=4x3..... then n=2 so n*(fact1) = 2x1, then 1*fact(0) = 1x0 then after if loop execution is done.
# now it restart previous execution--> 5x4x3x2x1=120 
n = int(input("Enter the number:- "))
result = fact(n)
print("Factorial of",n,"is",result)
