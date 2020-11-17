number=int(input())
a=0
while number != 1:
    if number % 2 ==0:
        number = number/2
        a+=1
    if number %2 != 0:
        number = 3*number+1
        a+=1
    break
print(a)