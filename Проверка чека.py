a=input()
num=int(a[:4])
total=int(a[4:])
total2=0
wrong_string=[]
for i in range(num):
    string=input()
    sum1=int(string[13:])
    price=int(string[:7])
    amount=int(string[8:12])
    sum2=price*amount
    total2+=sum2
    if price*amount==sum1:
        continue
    else:
        wrong_string.append(i+1)
print(total-total2)
for i in wrong_string:
    print(i, end=' ')
    