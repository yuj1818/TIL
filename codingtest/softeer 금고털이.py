import sys
input = sys.stdin.readline
w, n = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(n)]
jewel.sort(key=lambda x: x[1])
ans = 0
while w > 0:
    m, p = jewel.pop()
    w -= m
    ans += p * m
    lp = p
ans += lp * w
print(ans)