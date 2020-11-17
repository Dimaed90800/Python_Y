Tnumber = list(filter(lambda x: x != ' ', list(input())))
a = 0
if Tnumber[0] != '8' and Tnumber[:2] != ['+', '7']:
    print('error 1st number')
else:
    if  (''.join(Tnumber[0]) == '8') or (''.join(Tnumber[0]) == '+'):
        Tnumber1 = ''.join(Tnumber[1:])
        if not Tnumber1.isalpha():
            Tnumber = Tnumber[0] + Tnumber1
            Tnumber = list(filter(lambda x: x != ' ', list(Tnumber)))
        else:
            print('error letter')
    else:
        print('error')
if ''.join(Tnumber[0]) == '8' :
    Tnumber = '+7' + ''.join(Tnumber[1:])
    Tnumber = list(filter(lambda x: x != ' ', list(Tnumber)))
if Tnumber.count('(') <= 1 and Tnumber.count(')') <= 1:
    Tnumber.remove('(')
    Tnumber.remove(')')
else:
    print('error skobki')
if (Tnumber[0] == '-') or (Tnumber[-1] == '-') or ('--' in Tnumber):
    print('error -')
for i in Tnumber:
    if i == '-':
        a+=1
for i in range(a):
    Tnumber.remove('-')
Tnumber2 = ''.join(Tnumber)
print(Tnumber2)