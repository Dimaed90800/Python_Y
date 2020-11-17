number=int(input())
words=[]
for i in range(number):
    words.append(input())
    if 'не' in words[i]:
        s = words.find('не')
        words = words[0:s][s:-1]
        print(words)
    if 'Не' in words:
        f = words.find('Не')
        words = words[0:f][f:-1]
        print(words)