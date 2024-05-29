import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

import heapq

n = int(input())
arr = []

for _ in range(n):
    x = int(input())
    if x == 0:
        print(heapq.heappop(arr)[1] if arr else 0)
    else:
        heapq.heappush(arr, (abs(x), x))