n = int(input("Enter a number: "))

sq = n * n

if str(sq).endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not Automorphic Number")