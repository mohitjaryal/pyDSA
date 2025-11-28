# Display divisor of number using 'Optimal Approach'

# importing
from math import sqrt

n = int(input('Enter number :'))

num = n
result = []

for i in range(1,int(sqrt(num))+1):
    if(num % i == 0):
        result.append(i) # adding divisor to the result
        if(num // i != i):
            result.append(num//i)
    
print('Divisors are :',result)