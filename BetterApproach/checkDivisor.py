# Display divisor of number using 'Better Approach'

num = int(input('Enter a number :'))
n = num
result = [] # Empty list
for i in range(n // 2):
    if(n % i == 0):
        result.append(i)