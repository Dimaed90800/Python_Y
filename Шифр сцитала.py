text=input()
n=int(input())

 
x=[text[i:i+int(len(text)/n)] for i in range(0,len(text),int(len(text)/n))]
res=''.join([''.join(i) for i in list(zip(*x))])
 
print(res)