import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
memo = {}

for _ in range(n):
    key, val = input().split()
    memo[key] = val

for _ in range(m):
    print(memo[input().rstrip()].decode())