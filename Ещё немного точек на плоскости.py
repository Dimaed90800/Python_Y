n = []
x = []
y = []
for i in range(int(input())):
    n.append([int(i) for i in input().split()])
for i in n:
    x.append(i[0])
    y.append(i[1])
for i in (n):
    if i[1] != i[0]:
        if i[0] < 0 and i[1] > 0:
            if -(i[0]) > i[1]:
                    print('(' + str((i[0])) + ', ' + str(i[1]) + ')')
        elif i[1] < 0 and i[0] > 0:
            if i[0] > -(i[1]):
                    print('(' + str((i[0])) + ', ' + str(i[1]) + ')')
        if i[0] > 0 and i[1] > 0:
            if i[0] > i[1]:
                print('(' + str(i[0]) + ', ' + str(i[1]) + ')')
        if i[0] < 0 and i[1] < 0:
            if i[0] < i[1]:
                print('(' + str(i[0]) + ', ' + str(i[1]) + ')')
print(x)
print(y)
print('left: (' + str(min(x)) + ', ' + str(y.index(min(x))) + ')')
#print('right: (' + str(max(x)) + ', ' + str(y.index(max(x)) + 1) + ')')
#print('top: (' + str(x.index(max(y)) + 1) + ', ' + str(max(y)) + ')')
#print('bottom: (' + str(x.index(min(y)) + 1) + ', ' + str(min(y)) + ')')

