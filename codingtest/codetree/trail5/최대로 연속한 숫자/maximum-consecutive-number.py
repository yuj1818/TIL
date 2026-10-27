from sortedcontainers import SortedSet
n, m = map(int, input().split())
nums = list(map(int, input().split()))
s_num = SortedSet([-1, n + 1])
s_len = SortedSet([(-(n + 1), -1, n + 1)])
d = []
for y in nums:
    s_num.add(y)
    z = s_num[s_num.bisect_right(y)]
    x = s_num[s_num.bisect_left(y) - 1]
    s_len.remove((-(z - x - 1), x, z))
    s_len.add((-(y - x - 1), x, y))
    s_len.add((-(z - y - 1), y, z))
    print(-s_len[0][0])