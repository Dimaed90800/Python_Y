pile=int(input())
pile2=int(input())
while pile != 0 and pile2 != 0:
    num1=int(input())
    num2=int(input())
    if num1==1:
        pile=pile-num2
        print(pile, pile2)
    else:
        pile2=pile2-num2
        print(pile, pile2) 
print(0, 0)