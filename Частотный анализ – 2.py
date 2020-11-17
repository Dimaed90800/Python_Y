import re
from collections import Counter
 
t = '''\
Ехал Грека через реку. Видит Грека в реке рак.
Сунул Грека руку в реку, рак за руку Греку цап.
'''
 
words = re.findall(r'\w+', t)
words = [i.title() for i in words]
for word, i in Counter(words).most_common():
    ls = Counter(words).most_common()
    ls.sort(key=lambda x: (-x[1], x[0]))
for word, i in ls:
    print(word)