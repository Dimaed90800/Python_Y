def swap (first, second):
    third=first[:]
    for i in range(len(first)): first.pop()
    first.extend(second)
    for i in range(len(second)): second.pop()
    second.extend(third)
