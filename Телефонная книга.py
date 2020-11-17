phone_book={}
for i in range(int(input())):
    line=input().split()
    if line[1] in phone_book:
        phone_book[line[1]] +=' '+line[0]
    else:
        phone_book[line[1]] = line[0]
for j in range(int(input())):
    line1=input()
    if line1 in phone_book:
        print(phone_book[line1])
    else:
        print('Нет в телефонной книге')
