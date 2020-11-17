def Number(num):
    if num.find('--') != -1 or num[-1:] == '-':
        raise ValueError('неверный формат')
    num = ''.join(num.split()).replace('-', '')
    if num[:1] == '8':
        num = '+7' + num[1:]
    if num[:2] != '+7':
        raise ValueError('неверный формат')
    if num.count('(') == num.count(')') and num.count(')') <= 1 and \
       num.count('(') <= 1:
        num = num.replace('(', '', 1).replace(')', '', 1)
    else:
        raise ValueError('неверный формат')
    if num.find(')') == 0 and num.find(')') > 0:
        raise ValueError('неверный формат')
    if len(num) != 12:
        raise ValueError('неверное количество цифр')
    return num[:1] + str(int(num[1:]))


try:
    print(Number(input()))
except ValueError as Error:
    print(Error)