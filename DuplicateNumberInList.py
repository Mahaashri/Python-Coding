list = [1,2,3,4]
count = 0
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            count += 1
        else:
            count = count
if(count>0):
    print("True")
else:
    print("False")