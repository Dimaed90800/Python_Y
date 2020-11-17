birthday={}
for i in range(int(input())):
    line=input().split()
    if line[2] in birthday:
        birthday[line[2]] +=' '+line[0]
    else:
        birthday[line[2]] = line[0]
for j in range(int(input())):
    line1=input()
    if line1 in birthday:
        print(birthday[line1])
    else:
        print()