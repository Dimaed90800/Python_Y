def continueFibonacciSequence(sequence, n): 
    for i in range(n): # для i в количестве раз n
        nextElement = sequence[-1] + sequence[-2] # следующий элемент равен последний элемент + предпоследний
        sequence += [nextElement] # нужно += вместо =...+, иначе там создаётся нова ячейка
    print(sequence)
continueFibonacciSequence([1, 2, 3], 5)