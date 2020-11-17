n = int(input())
a = list(range(1, n+1))
if a[-1] == sum(a[:-1]):
    print(('-' * (n-1)) + '+')
elif sum(a) % 4 == 0:
    l = sum(a) / 4
    if l % 2 == 0:
        print(('-+' * (l/2)))
    else:
        print(('-+' * (l//2)) + '-')
else:
    print('IMPOSSIBLE')