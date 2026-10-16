n = int(input())
b = sorted([int(input()) for _ in range(n)])
a = sorted(set(range(1, 2 * n + 1)) - set(b))
ans, bi = 0, 0
for ai in range(n):
    if bi < n and a[ai] > b[bi]:
        ans += 1
        bi += 1
print(ans)