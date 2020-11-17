city=input()
city1=input()
while True:
    if city[-1] == 'ь':
                city=city[:-1]
    if city[-1] == city1[0]:
        print('ВЕРНО')
        break
    else:
        print('НЕВЕРНО')
        break