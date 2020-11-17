numbers=int(input())
for i in range(numbers):
    for k in range(i,-1, -1):
        print('Осталось секунд:', k)
    print('Пуск', i+1)