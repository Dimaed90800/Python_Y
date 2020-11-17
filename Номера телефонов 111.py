def Number(num):
    if num.find('(') <= num.find(')'):
        num = num.replace('(', '', 1).replace(')', '', 1)
    else:
        return ''    
    if num.find('--') != -1 or num[-1:] == '-':
        return ''
    num = ''.join(num.split()).replace('-', '')
    if num[:1] == '8':
        num = '+7' + num[1:]
    if num[:2] != '+7':
        return ''
    if len(num) != 12:
        return ''
    return num[:1] + str(int(num[1:]))


num = input()
res = Number(num)
if res:
    print(res)
else:
    print('error')
        