import sys
input = sys.stdin.readline
n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
cycles = []

def dfs(s, n):
    visited[n] = 1
    if visited[nums[n]]:
        if s == nums[n]: cycles.append(s)
    else: dfs(s, nums[n])

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    dfs(i, i)

print(len(cycles))
for x in cycles: print(x)