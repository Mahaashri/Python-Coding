nums = list(map(int, input("Enter numbers: ").split()))
s = set()
for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if(nums[i]+nums[j]+nums[k]==0):
                          tup = tuple(sorted([nums[i], nums[j], nums[k]]))
                          s.add(tup)
list1 = []
for i in s:
    list1.append(list(i))
    print(list1)