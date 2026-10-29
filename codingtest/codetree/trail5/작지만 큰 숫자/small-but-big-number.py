from sortedcontainers import SortedSet
n, m = map(int, input().split())
a = SortedSet(map(int, input().split()))
for x in map(int, input().split()):
    i = a.bisect_right(x)
    if i == 0:
        print(-1)
        continue
    print(a[i - 1])
    a.remove(a[i - 1])