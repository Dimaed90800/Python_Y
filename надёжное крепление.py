a = int(input())
b = int(input())
c = int(input())
nums = []
if a >= b and a>=c:
    if b >= c:
        nums.append(a)
    else:
        nums.append(c)
if b >= c  and b >= a:
    if b >= c:
        nums.append(a)
    else:
        nums.append(c)
if c >= a and c >= b:
    if a >=b :
        nums.apped(a)
    else:
        nums.append(b)
if len(nums) > 1:
    print(max(nums))
else:
    print(*nums)