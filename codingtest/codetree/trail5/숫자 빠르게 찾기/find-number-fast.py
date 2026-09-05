from bisect import bisect_right
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    x = int(input())
    i = bisect_right(arr, x)
    if arr[i - 1] == x: print(i)
    else: print(-1)