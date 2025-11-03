# Display divisor of number using 'Better Approach'

# Better approach

num = int(input('Enter a number :'))
n = num
result = [] # Empty list
for i in range(1, n // 2):
    if(n % i == 0):
        result.append(i)
result.append(num)
print('Divisors :',result)