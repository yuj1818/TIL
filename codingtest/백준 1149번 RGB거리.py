import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    costs[i] = [costs[i][idx] + v for idx, v in enumerate([min(costs[i - 1][1], costs[i - 1][2]), min(costs[i - 1][0], costs[i - 1][2]), min(costs[i - 1][0], costs[i - 1][1])])]

print(min(costs[-1]))