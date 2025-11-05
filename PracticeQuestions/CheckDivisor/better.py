# Display divisor of number using 'Brute Force Approach'

n = int(input('Enter number :'))

num = n
result = []

for i in range(1, n //2):
    if(num % i == 0):
        result.append(i) # adding divisor to the result
result.append(num)
print('Divisors :',result)