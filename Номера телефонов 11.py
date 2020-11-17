Tnumber = list(filter(lambda x: x != ' ', list(input())))
letters = 0
a = True
for i in range(len(Tnumber)):
    if Tnumber[i].isalpha():
        letters += 1
tn1 = ''.join(Tnumber[1:])
tn = ''.join(Tnumber[0])
tn2 = ''.join(Tnumber)
a = 0
if Tnumber[0] != '8' and Tnumber[:2] != ['+', '7']:
    print('error')
    a = False
elif letters > 0:
    print('error')
    a = False
elif Tnumber.count('(') > 1 and Tnumber.count(')') > 1:
    print('error')
    a = False
elif (Tnumber[0] == '-') or (Tnumber[-1] == '-') or ('--' in ''.join(Tnumber)):
    print('error')
    a = False
elif Tnumber.count('(') > Tnumber.count(')'):
    a = False
    print('error')  
elif tn2.find('(') <= tn2.find(')'):
    tn2 = tn2.replace('(', '', 1).replace(')', '', 1)
    Tnumber = list(filter(lambda x: x != ' ', list(tn2)))
    a = True
if tn == '8':
    Tnumber = '+7' + ''.join(Tnumber[1:])
    Tnumber = list(filter(lambda x: x != ' ', list(Tnumber)))
for i in Tnumber:
    if i == '-':
        a += 1
for i in range(a):
    Tnumber.remove('-')
if a:
    Tnumber2 = ''.join(Tnumber)
    print(Tnumber2)