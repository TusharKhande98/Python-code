''' Factorial of non-negative integer --->n!
 5! = 5 x 4 x 3 x 2 x 1 = 120
NOTE:- factorial of '0' & '1' is '1'---> 0! = 1

Three ways to write this prigram in python--> 
1. inbuilt func- factorial from MATH module
2. by using recursion
3. by using iterative - for loop
'''

# CODE-I:- Factorial by inbuit function 
import math
n = int(input("Enter the number:- "))
result = math.factorial(n)
print("Factorial of",n, "is",result) # n & result variable's value print here.

 
