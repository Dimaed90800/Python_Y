word= input()
while True:
    if word[0] == 'А' or word[0] == 'а':
        print('ДА')
        break
    if word[0] != 'А' or word[0] != 'а':
        print('НЕТ')
        break
