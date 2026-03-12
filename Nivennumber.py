#Niven Number Or Not Code
n = int(input("Enter a number:"))
temp = n
sum = 0

while temp>0:
    digit = temp%10
    sum += digit
    temp //= 10
if ((n%sum) == 0):
    print("Niven Number")
else:
    print("Not a Niven Number")