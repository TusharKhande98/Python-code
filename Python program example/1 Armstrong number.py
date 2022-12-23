'''Find the number is armstrong or not.
Q. So what is armstrong no?
A. number of 'n' digits, which are equal to sum of 'nth' power, of its digits.
suppose we have single digit, so only one digit which is 5 so its power is also 'n=1'.
So if we consider 5 to the power 'n'which is '1' is equal to 5.
In this way 0,1,2,3,4,5,6,7,8,9 are all armstrong numbers.

*now we conider 2 digits number as '22'*
'22' has two digits, so n=2(its power).
find 'nth' power of digits---> we get 2 to power 2 = 4 & 2 to power 2 = 4
sum of 'nth' power of its digits----> 4 + 4 = 8 {which is not 22, so its not armstrong no.}

*now we conider 3 digits number as '153'*
'153' has three digits, so n=3(its power).
find 'nth' power of digits---> 
we get 1 to power 3 = 1 & 5 to power 3 = 125 & 3 to power 3 = 27.
sum of 'nth' power of its digits----> 1 + 125 + 27 = 153 {so its Armstrong no.}'''

for i in range(1001):
    num  = i #here we stored our actual no. to compare with last result
    result = 0 # here we stored nth power & sum of nth power of digit.
    n = len(str(i)) # here we find length of no. by converting it int string.
    while(i!=0):
        digit = i%10 # this variable holds digit from the no. eg.- from '153' it stored '3'.
        result = result + digit**n # here it perform as 0+3**3=27.
        i = i//10 # we already calculate 3 so by truncate division we get 15 only--> 153//10 = 15.
# this while loop runs until the condition i = 0. for 153 when it check at end 'i=i//10=0' the loop terminated
    if num==result:         
        print(num) # instead 'num' we can write 'result' also both are same if they are equal
