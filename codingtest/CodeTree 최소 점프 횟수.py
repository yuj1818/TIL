ans = -1
n = int(input())
a = list(map(int, input().split()))
q = [(0, 0)]
while q:
    x, cnt = q.pop(0)
    if x == n - 1:
        ans = cnt
        break
    for i in range(1, a[x] + 1):
        nx = x + i
        if nx >= n: continue
        q.append((nx, cnt + 1))
print(ans)
