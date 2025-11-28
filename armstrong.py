# Check whether the number is armstrong number or not 
n = int(input('Enter a number :'))
num = n
total = 0

ln = len(str(n))

while(num>0):
    ld = num % 10
    total = total + (ld ** ln) # adding last digit to the total
    num //= 10

if(total == n ):
    print('Yes it is an Armstrong number')
else:
    print("No it's not an Armstrong number ")