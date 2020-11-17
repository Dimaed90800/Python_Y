def Number(num):
    if num.find('(') <= num.find(')'):
        num = num.replace('(', '', 1).replace(')', '', 1)
    else:
        raise ValueError()
    if num.find('--') != -1 or num[-1:] == '-':
        raise ValueError()
    num = ''.join(num.split()).replace('-', '')
    if num[:1] == '8':
        num = '+7' + num[1:]
    if num[:2] != '+7':
        raise ValueError()
    if len(num) != 12:
        raise ValueError()
    return num[:2] + str(int(num[2:]))


try:
    print(Number(input()))
except ValueError:
    print('error')
          