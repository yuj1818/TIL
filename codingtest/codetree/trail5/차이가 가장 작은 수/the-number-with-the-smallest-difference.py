from sortedcontainers import SortedSet
from collections import Counter
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
cnt = Counter(arr)
sa = SortedSet(arr)
ans = float('inf')
for i in range(1, n):
    x = arr[i] - m
    ti = sa.bisect_right(x)
    if ti == 0: continue
    if sa[ti - 1] == arr[i] and cnt[arr[i]] == 1: continue
    ans = min(ans, arr[i] - sa[ti - 1])
if ans == float('inf'): print(-1)
else: print(ans)