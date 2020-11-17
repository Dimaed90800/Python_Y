cat = False
counter = 0
line = ''
while line != 'СТОП':
       line=input()
       counter += 1
       if 'Кот' in line or 'кот' in line:
              cat = True
              print('МЯУ')
              break
if 'Кот' not in line or 'кот' not in line:
       print('НЕТ')
       