nums = []
for i in range(3):
    nums.append(int(input()))
ma = max(nums)
mi = min(nums)
res = 0
a = nums.index(ma)
b = nums.index(mi)
if a == 0 and b == 1:
    if a == 0 and nums[2] == a:
        print(b)
    else:
        res = nums[2]
if a == 0 and b == 2:
    if a == 0 and nums[1] == a:
        print(b)
    else:    
        res = nums[1]
if a == 1 and b == 0:
    if a == 1 and nums[2] == a:
        print(b)
    else:        
        res = nums[2]
if a == 1 and b == 2:
    if a == 1 and nums[0] == a:
        print(b)
    else:     
        res = nums[0]
if a == 2 and b == 0:
    if a == 2 and nums[1] == a:
        print(b)
    else:     
        res = nums[1]
if a == 2 and b == 1:
    if a == 2 and nums[0] == a:
        print(b)
    else:         
        res = nums[0]
if nums[0] == nums[1] and nums[1] == nums[2]:
    res = nums[0]
print(res)
