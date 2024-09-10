import sys
input = sys.stdin.readline

def dfs(s, root):
    for e in connection[s]:
        if not connected[root][e]:
            connected[root][e] = 1
            dfs(e, root)

n = int(input())
connection = [[] for _ in range(n)]
connected = [[0] * n for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            connection[i].append(j)

for i in range(n):
    dfs(i, i)

for line in connected:
    print(*line)