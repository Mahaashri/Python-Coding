def fact(digit):
    f = 1
    for i in range(1, digit+1):
        f = f * i
    return f
    
n = int(input("Enter a number: "))
temp = n
sum = 0

while temp > 0:
    digit = temp % 10
    sum += fact(digit)
    temp //= 10

if sum == n:
    print("Strong Number")
else:
    print("Not Strong Number")