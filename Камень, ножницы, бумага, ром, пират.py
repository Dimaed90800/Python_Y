pirot1 = input()
pirot2 = input()
if pirot1 == 'бумага' and pirot2 == 'камень' or pirot1 == 'ножницы' \
   and pirot2 == 'бумага' or pirot1 == 'камень' and pirot2 == 'ножницы' or \
   pirot1 == 'ром' and pirot2 == 'пират' or \
   pirot1 == 'ром' and pirot2 == 'бумага' or \
   pirot1 == 'камень' and pirot2 == 'ром' or \
   pirot1 == 'бумага' and pirot2 == 'пират' \
   or pirot1 == 'пират' and pirot2 == 'ножницы' \
   or pirot1 == 'пират' and pirot2 == 'камень' or\
   pirot1 == 'камень' and pirot2 == 'ром' or \
   pirot1 == 'ножницы' and pirot2 == 'ром':
    print('первый')
elif pirot1 == pirot2:
    print('ничья')
else:
    print('второй')
    
