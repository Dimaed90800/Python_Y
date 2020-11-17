word=input()
word1=input()
counter=0
counter1=0
for i in range(len(word)):
    if word[i] == word1[i]:
        counter+=1
    if word[i] in word1:
        counter1+=1
print(counter, counter1-counter)