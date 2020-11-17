numbers = (input()).split()
books=set()
library=set()
numbers=[int(j) for j in numbers]
for i in range(numbers[0]):
    books.add((input()))
for i in range(numbers[1]):
    if input() in books:
        print('YES')
    else:
        print('NO')        