translit = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
            "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
            "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
            "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
            "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
            "б": "b", "ю": "ju", "ё": "jo"}

letters = {}
a = ''
for i in translit:
    letters[i[0].upper() + i[1:]] = translit[i][0].upper() + translit[i][1:]
    letters[i] = translit[i]
with open('cyrillic.txt', 'r') as f:
    line = f.read()
    for i in line:
        if i in letters:
            a += letters[i]
        else:
            a += i
with open('transliteration.txt', 'w') as f1:
    f1.write(a)

