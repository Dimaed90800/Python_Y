from math import ceil
import sys
cities =[]
 
for line in sys.stdin:
    cities.append(line)
popul = {}
for x in cities:
    city, _, pop = x.split()
    pop = int(ceil(int(pop)/100000)) * 100
    popul[pop] = popul.get(pop,[]) + [city]
 
popul = sorted(popul.items())
 
for k, v in popul:
        print('{} - {}: {}'.format(int(k) - 100, k,  ', '.join(sorted(v))))
