n = int(input("Enter number: "))
sq = n*n

while n > 0:
    if n%10 != sq%10:
        print("Not Automorphic")
        break
    n //= 10
    sq //= 10
else:
    print("Automorphic")