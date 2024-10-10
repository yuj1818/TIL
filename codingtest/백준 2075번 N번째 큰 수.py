import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
midx = [n - 1] * n
for _ in range(n):
    mv, mj = -float("inf"), 0
    for j in range(n):
        i = midx[j]
        if mv < graph[i][j]:
            mv = graph[i][j]
            mj = j
    midx[mj] -= 1
print(mv)