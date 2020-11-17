line=input()
line= line.upper()
line=line.split()
for i in range(len(line)):
    f='-'.join(line[i])
    print(f, end=' ')