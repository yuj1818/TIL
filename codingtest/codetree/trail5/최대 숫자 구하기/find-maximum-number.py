from sortedcontainers import SortedSet
n, m = map(int, input().split())
s = SortedSet(range(1, m + 1))
for x in list(map(int, input().split())):
    s.remove(x)
    print(s[-1])