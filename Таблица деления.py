columns=int(input())
lines=int(input())
for i in range(lines):
    for k in range(columns):
        print((k+1)/(i+1), end=' ')
    print('')