num=int(input())
search=[]
for i in range(num):
    search.append(input())
n=int(input())
search_words=[]
final=[]
for i in range(n):
    search_words.append(input())
for i in range(len(search)):
    there_is_search_word=True
    for j in range(len(search_words)):
        if search_words[j] not in search[i]:
            there_is_search_word=False
    if there_is_search_word:
        final.append(search[i])
for i in range(len(final)):
    print(final[i])