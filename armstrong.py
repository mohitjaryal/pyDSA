# Check whether the number is armstrong number or not 
n = int(input('Enter a number :'))
num = n
total = 0

ln = len(str(n))

while(num>0):
    ld = num % 10