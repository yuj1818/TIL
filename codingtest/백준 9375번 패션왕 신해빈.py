import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    closet = dict()
    ans = 1

    for _ in range(n):
        item, key = input().split()
        closet[key] = closet.get(key, 0) + 1

    for n in closet.values():
        ans *= n + 1

    print(ans - 1)