import sys


lst = []
for line in sys.stdin:
    lst.append(line)
 
sum_lst = sum([int(x.split()[0]) for x in lst])
sum_set = sum([int(x.split()[0]) for x in set(lst)])    
 
print(sum_lst - sum_set)