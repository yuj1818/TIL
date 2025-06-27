n = 1000 - int(input())
a = [1, 5, 10, 50, 100, 500]
ans = 0
while n > 0 and a:
    x = a.pop()
    ans += n // x
    n %= x
print(ans)