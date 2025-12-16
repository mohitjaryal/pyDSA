# if the number is palindrome return true otherwise flase
n = int(input('Enter number :'))
num = n 
result = 0
while(num>0):
    last_digit = num % 10
    result = (result * 10) + last_digit
    num //= 10
if n == result:
    print(True)
else:
    print(False)