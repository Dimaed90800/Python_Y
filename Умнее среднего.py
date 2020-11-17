number=int(input())
counter=0
for i in range(number):
    numbers=int(input())
    if i == 0:
        numbers=0
        a=numbers
        counter+=1
        c=a+numbers
        print(0)
    if numbers > c/counter:
        a=numbers
        counter+=1
        c=a+numbers
        print('>')
    if numbers < c/counter:
        a=numbers
        counter+=1
        c=a+numbers
        print('<')
    if numbers == c/counter:
        numbers=0
        a=numbers
        counter+=1
        c=a+numbers        
        