import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    check = [0] * n
    for i in range(n): check[a[i]] += 1
    zero = [i for i in range(n) if not check[i]]
    for c in zero:
        q = [c]
        while q:
            x = q.pop(0)
            nxt = a[x]
            check[nxt] -= 1
            if check[nxt] == 0: q.append(nxt)
    ans = 0
    for i in range(n):
        if check[i] != 1: ans += 1
    print(ans)