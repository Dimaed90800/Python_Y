def Leap(n):
    if n%4 == 0 and n%100 != 0:
        print('Високосный')
    elif n%400 == 0:
        print('Високосный')
    else:
        print('Не високосный')

