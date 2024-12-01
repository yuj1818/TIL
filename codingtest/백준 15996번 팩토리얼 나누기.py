n, a = map(int, input().split())
d = a
ans = 0
while d <= n:
    ans += n // d
    d *= a
print(ans)