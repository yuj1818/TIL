from bisect import bisect_left
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for x in list(map(int, input().split())):
    idx = bisect_left(arr, x)
    if idx == n or arr[idx] != x: print(-1)
    else: print(idx + 1)