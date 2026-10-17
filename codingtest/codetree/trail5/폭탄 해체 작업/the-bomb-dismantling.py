n = int(input())
bombs = [list(map(int, input().split())) for _ in range(n)]
bombs.sort(lambda x:(-x[0],x[1]))
removed = dict()
ans = 0
for s, t in bombs:
    for i in range(t, 0, -1):
        if i in removed: continue
        removed[i] = s
        ans += s
        break
print(ans)