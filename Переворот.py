with open('input.dat', 'rt', encoding="utf-8") as f:
    line = f.readlines()


def reverse(line):
    line = line[::-1]
    with open('output.dat', 'w') as f1:
        f1.write(line)