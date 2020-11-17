N = 7
dominoes = [[0] * N for _ in range(N)]
for _ in range(int(input())):
    i, j = map(int, input().split())
    dominoes[j][i] = dominoes[i][j] = dominoes[i][j] + 1

# count "friendly" pairs
npairs = 0
for i in range(N):  # for each domino i:j where i <= j
    for j in range(i, N):
        n = dominoes[i][j]
        if n:
            npairs += n * (n - 1) // 2   # {n \choose 2} pairs with itself
            for k in range(i+1, N):      # top-down
                npairs += dominoes[k][j] * n
            if i != j:  # don't count twice 
                for k in range(j+1, N):      # left-right
                    npairs += dominoes[i][k] * n

print(npairs)