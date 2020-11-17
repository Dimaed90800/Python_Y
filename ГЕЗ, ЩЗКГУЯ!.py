alh = input()
n = int(input()) % len(alh)
code = alh[n:] + alh[0:n]
code1 = alh[-n:] + alh[:-n]
print(code)
print(alh)
print(code1)
