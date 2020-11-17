import sys 
number = 0
for line in sys.stdin:
    number += 1
    if '#' in line:
        print('Line '+str(number)+': '+line[line.index('#') +1:].strip())
        
        