products = set([input() for i in range(int(input()))])
recipes={}
recipes1=[]
for i in range(int(input())):
    recipe = input().split()
    recipes1+=[recipe[0]]
    recipes[recipe[0]] = set([input() for i in range(int(recipe[1]))])
for j in recipes1:
    if products >= recipes[j]:
        print(j)