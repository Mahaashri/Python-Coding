n = int(input("Enter a number: "))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    temp = temp // 10

if n % sum == 0:
    print("Niven number")
else:
    print("Not Niven number")