import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
parent = list(range(n + 1))
friends = [0] + [1 for i in range(n)]

def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]

def union(y, x):
    x = find(x)
    y = find(y)
    if x == y: return
    if x > y:
        parent[x] = y
        friends[y] += friends[x]
        candy[y] += candy[x]
    else:
        parent[y] = x
        friends[x] += friends[y]
        candy[x] += candy[y]

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

group = []
for i in range(1, n + 1):
    if i == parent[i]: group.append((friends[i], candy[i]))
group.sort(key=lambda x: (x[0], x[1]))

dp = [0] * k
for p, c in group:
    for i in range(k - 1, p - 1, -1):
        dp[i] = max(dp[i - p] + c, dp[i])
print(dp[-1])