nums = input().split() 
from_to = input().split() 
squares_of_nums = [int(i)**2 for i in nums] 
from_to = [int(i) for i in from_to] 
print(sum(squares_of_nums[from_to[0]:from_to[1]+1]))
