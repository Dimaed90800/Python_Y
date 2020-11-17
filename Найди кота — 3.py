cat = False
counter = 0
counter1=0
line = ''
while line != 'СТОП':
       line=input()
       counter1+=1
       if 'Кот' in line or 'кот' in line:
              cat = True
              counter += 1
              if counter1 == -1:
                     counter1+=2
              break
       if 'Кот' not in line or 'кот' not in line:
              counter1=-1
              
print(counter, counter1)