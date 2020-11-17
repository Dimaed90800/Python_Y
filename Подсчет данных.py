with open('input.txt', 'r') as f:
    lines = f.read()
    lines = lines.split()
    lenght = len(lines)
    plus = 0
    minus = 0
    zero = 0
    for i in range(lenght):
        if int(lines[i]) > 0:
            plus += 1
        if int(lines[i]) < 0:
            minus += 1
        if int(lines[i]) == 0:
            zero += 1
    line = '1 ' + str(plus) + ' ' + '-1 ' + str(minus) + ' ' + '0 ' + str(zero)
    if minus == 0:
        line = '1 ' + str(plus) + ' ' + '0 ' + str(zero)
    if plus == 0:
        line = '-1 ' + str(minus) + ' ' + '0 ' + str(zero)
    if zero == 0:
        line = '1 ' + str(plus) + ' ' + '-1 ' + str(minus)
    if zero == 0 and minus == 0:
        line = '1 ' + str(plus)
    if zero == 0 and plus == 0:
        line = '-1 ' + str(minus)
    if minus == 0 and plus == 0:
        line = '0 ' + str(zero)
    if lenght == 0:
        line = ''
with open('output.txt', 'w') as f1:
    f1.write(str(lenght) + '\n')
    f1.write(line)
    