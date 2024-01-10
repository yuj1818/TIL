import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, k = map(int, input().split())
value = sorted([int(input()) for _ in range(n)], reverse=True)
ans = 0

for v in value:
    if k // v > 0:
        ans += k // v
        k %= v

    if k == 0:
        break

print(ans)