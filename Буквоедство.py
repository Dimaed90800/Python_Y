word=input()
print(word)
for i in range(len(word)):
    if len(word)%2 ==0:
        while len(word) != 2:
            word=word[1:-1]
            print(word)
    if len(word)%2 != 0:
        while len(word) != 1:
            word=word[1:-1]
            print(word)