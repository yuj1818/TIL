import sys
input = sys.stdin.readline

def dfs(s):
    visited[s] = 1
    for i in range(n + 2):
        if not visited[i] and abs(pos[s][0] - pos[i][0]) + abs(pos[s][1] - pos[i][1]) <= 1000:
            dfs(i)

for _ in range(int(input())):
    n = int(input())
    pos = [list(map(int, input().split())) for _ in range(n + 2)]
    visited = [0] * (n + 2)
    dfs(0)
    if not visited[-1]: print('sad')
    else: print('happy')