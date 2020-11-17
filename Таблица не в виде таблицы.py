number=int(input())

for i in range(number):
    for k in range(number):
        print(i+1, '*', k+1, '=', (k+1)*(i+1))