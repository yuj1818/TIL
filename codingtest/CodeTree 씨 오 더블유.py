n = int(input())
word = input()
C = [0] * n
W = [0] * n
C[0] = 1 if word[0] == 'C' else 0
W[-1] = 1 if word[-1] == 'W' else 0
for i in range(1, n):
    C[i] = C[i - 1] + (1 if word[i] == 'C' else 0)
for i in range(n - 2, -1, -1):
    W[i] = W[i + 1] + (1 if word[i] == 'W' else 0)
ans = 0
for i in range(1, n - 1):
    if word[i] == 'O': ans += (C[i] * W[i])
print(ans)
