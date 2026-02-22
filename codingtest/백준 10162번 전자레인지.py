n = int(input())
if n % 10:
    print(-1)
    exit()
ans = []
for x in (300, 60, 10):
    print(n // x, end=' ')
    n %= x