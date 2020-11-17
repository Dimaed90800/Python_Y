houres = input().split()
minutes = input().split()
for i in range(len(houres)):
    houres[i] = int(houres[i])
for i in range(len(minutes)):
    minutes[i] = int(minutes[i])
houres = sorted(houres)
minutes = sorted(minutes)
for i in range(len(houres)):
    for j in range(len(minutes)):
        g = houres[i] % 10
        a = houres[i] // 10
        if (houres[i] + minutes[j])/2 != (g + a):
            for f in range(len(houres)):
                houres[i] = str(houres[i])
            for e in range(len(houres)):
                minutes[i] = str(minutes[i])
            for i in range(len(houres)):
                if len(houres[i]) == 1:
                    houres[i] = '0' + houres[i]
            for i in range(len(minutes)):
                if len(minutes[i]) == 1:
                    minutes[i] = '0' + minutes[i]
                print(houres[i] + ':' + minutes[i])
