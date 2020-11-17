def palindrome():
    w = open('input.dat', 'rb').read()
    return w == w[::-1]
        