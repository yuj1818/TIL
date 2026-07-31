s = input()
p = input()
n, m = len(s), len(p)
s = ' ' + s
p = ' ' + p
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 1
for j in range(m):
    for i in range(n + 1):
        if not dp[i][j]: continue
        if j < m - 1 and p[j + 2] == '*':
            dp[i][j + 2] = 1
        
            for ci in range(i + 1, n + 1):
                if p[j + 1] != '.' and s[ci] != p[j + 1]: break
                dp[ci][j + 2] = 1
        elif p[j + 1] == '.':
            dp[i + 1][j + 1] = 1
        else:
            if i < n and s[i + 1] == p[j + 1]:
                dp[i + 1][j + 1] = 1
print('true' if dp[-1][-1] else 'false')