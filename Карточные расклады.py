import itertools

nominals = ['2','3','4','5','6','7','8','9','10','валет','дама','король','туз']
suits = ['пик','треф','бубен','червей']
allcomb = list(itertools.product(nominals,suits))
comb = []
for elem in allcomb:
    if (elem not in comb) and (list(elem).reverse() not in comb):
        comb.append(' '.join(elem))
comb.sort()
three = sorted(itertools.combinations(comb, 3))
for comb in three:
    comb = list(comb)
    comb.sort()
    if any([x.split()[1] == 'червей' for x in comb]) and any([y.split()[0] in nominals[9:] for y in comb]):
        print(', '.join(list(comb)))