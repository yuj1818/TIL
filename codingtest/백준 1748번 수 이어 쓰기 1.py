n = input()
m = len(n)
ans = 0
for i in range(1, m): ans += 9 * 10 ** (i - 1) * i
ans += (int(n) - 10 ** (m - 1) + 1) * m
print(ans)
