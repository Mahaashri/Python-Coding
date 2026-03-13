list = list(map(int, input("Enter numbers: ").split()))

count = 0

for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] == list[j]:
            count += 1

if count > 0:
    print("True")
else:
    print("False")