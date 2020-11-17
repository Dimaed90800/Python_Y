translit = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",  
            "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
            "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
            "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
            "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
            "б": "b", "ю": "ju", "ё": "jo"}

f = ('cyrillic.txt', 'rt')
line = f.readlines()
for i in line:
    if i in translit:
        if line[i].upper():
            i[0] = i[0].upper()
            line[i] = translit[i]
        else:
            i = i.upper()
            line[i] = translit[i]
        line[i] = translit[i]
f.close()
f1 = open('transliteration.txt', 'rt')
f1.write(line)
f1.close