n, m = map(int, input().split())
a = list(map(int, input().split()))
q = list(range(1, n + 1))
cnt, s = 0, 1
for i in range(m):
    cnt += min((q.index(s) - q.index(a[i]) + n) % n, (q.index(a[i]) - q.index(s) + n) % n)
    s = q[(q.index(a[i]) + n + 1) % n]
    n -= 1
    q.remove(a[i])
print(cnt)