a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
s = []
for i in range(len(a)):
    s.append(b[i]-a[i])
print(a[s.index(max(s))], b[s.index(max(s))])