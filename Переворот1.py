def reverse():
    with open('input.dat', 'rb') as f:
        line = f.read()    
    line = line[::-1]
    with open('output.dat', 'wb') as f1:
        f1.write(line)
    return()