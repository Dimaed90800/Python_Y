with open('prices.txt', 'rt') as f:
    line = f.readlines()
    lines = list(filter(lambda x: x != '\t', list(line)))
    del lines[::3]
    Nums = []
    quantity = lines[::2]
    price = lines[1::2]
    for i in range(len(price)):
        Nums.append(price[i] * quantity[i])
print(sum(Nums))