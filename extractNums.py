# Extract numbers

# User input
n = int(input('Enter number :'))
print('You entered :',n)
num = n

# Main logic
while (num > 0):
    last_digit = num % 10 # Taking last digit
    print(last_digit)
    num //= 10 # just taking integer val only not decimal