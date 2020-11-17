
from itertools import cycle, chain, repeat
 
 
line = input()
nums =input().split()
a = int(nums[0])
b = int(nums[1])


 
ishift = cycle(chain(repeat(str.upper, a), repeat(str.lower, b)))
rline = ''.join(shift(ch) for ch, shift in zip(line, ishift))
 
print(rline)