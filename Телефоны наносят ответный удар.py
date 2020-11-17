Codes = ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919',
         '980', '981', '982', '983', '984', '985', '986', '987', '988', '989',
         '920', '921', '922', '923', '924', '925', '926', '927', '928', '929',
         '930', '931', '932', '933', '934', '935', '936', '937', '938', '939',
         '902', '903', '904', '905', '906', '960', '961', '962', '963', '964',
         '965', '966', '967', '968', '969']


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
    if num[0] == +7:
        if num[1:4] not in Codes:
            raise ValueError('не определяется оператор сотовой связи')
    if num[0] == '+':
        if num[2:5] not in Codes:
            raise ValueError('не определяется оператор сотовой связи')
    return num[:1] + str(int(num[1:]))


try:
    print(Number(input()))
except ValueError as Error:
    print(Error)