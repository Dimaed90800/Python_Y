from itertools import islice, count
 
number = int(input())
 
days = [number, 1000, 2000, 3000, 4000, 5000]
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
 
y = []
for i in islice(count(0), 17):
    if i % 4 == 0:
        y.append(366)
    else:
        y.append(365)
 
result = []
 
def dd_mm(n, k):
    if k % 4 == 0:
        days_of_month[1] = 29
    else:
        days_of_month[1] = 28
    for i in islice(count(0), 12):
        if n - days_of_month[i] > 0:
            n = n - days_of_month[i]
        else:
            result.append(str(n) + ' ' + str(i+1))
            break
 
for i in islice(count(0), 6):
    m = days[i]
    for j in islice(count(0), 20):
        if m - y[j] > 0:
            m = m - y[j]
        else:
            dd_mm(m, j)
            break
            

for i in islice(count(0), 6):
    print(result[i])
