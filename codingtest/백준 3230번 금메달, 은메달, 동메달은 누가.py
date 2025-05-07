n, m = map(int, input().split())
rank = []
for i in range(1, n + 1): rank.insert(int(input())-1, i)
res = []
for i in range(m - 1, -1, -1): res.insert(int(input())-1, rank[i])
for i in range(3): print(res[i])