from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
arr = list(map(int, input().split()))
for _ in range(m):
    x = int(input())
    l, r = bisect_left(arr, x), bisect_right(arr, x)
    print(r - l)