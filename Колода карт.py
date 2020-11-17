from itertools import product
 
 
dropsuit = input()
 
suits = ['пик', 'треф', 'бубен', 'червей']
nominals = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз')
 
suits.remove(dropsuit)
 
for n, s in product(nominals, suits):
    print(n, s)