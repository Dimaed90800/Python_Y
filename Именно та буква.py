word = input()
number=int(input())
letter=input()
n=['а','б','в','г','д','е','ё','ж','з','и','к','л','м','н','о','п', 'р', 'с','т','у','ф','х','ц','ч','ш','щ','э','ю','я','ь','ъ']
while True:
    if number == word.find(letter)+1 and len(letter) == 1 and letter in n:
        print('ДА')
        break
    if number != word.find(letter)+1 and len(letter) == 1 and letter in n:
        print('НЕТ')
        break
    else:
        print('ОШИБКА')
        break