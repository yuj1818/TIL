from sortedcontainers import SortedSet
from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
seats = SortedSet(range(1, m + 1))
ans = 0
for x in a:
    i = seats.bisect_right(x)
    if i == 0: break
    seats.remove(seats[i - 1])
    ans += 1
print(ans)
