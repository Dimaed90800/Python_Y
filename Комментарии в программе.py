count=int(input()[1:]) 
for i in range(count): 
    line = input() 
    if '#' in line: 
        print(line[:line.find('#')].rstrip()) 
    else: 
        print(line.rstrip())