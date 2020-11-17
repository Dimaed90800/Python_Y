Letters = 'qwertyuiop\asdfghjkl\zxcvbnm\йцукенгшщзхъ\фывапролджэё\ячсмитьбю'


def g_password(password):
    if len(password) < 8:
        return False
    keybordUp = False
    keybordLw = False
    num = False
    line = True   
    for i in range(0, len(password) - 2):
        if password[i].isupper():
            keybordUp = True
        if password[i].islower():
            keybordLw = True
        if password[i].isdigit():
            num = True
        if password[i:i + 3].lower() in Letters:
            line = False
    return keybordUp and keybordLw and num and line


password = input()
res = g_password(password)
if res:
    print('ok')
else:
    print('error')
        