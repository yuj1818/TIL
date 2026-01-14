from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def prim(s):
    heap = []
    MST = [0] * (n + 1)
    heappush(heap, (0, s))
    tw = 0
    while heap:
        w, x = heappop(heap)
        if MST[x]: continue
        MST[x] = 1
        tw += w
        for i in range(1, n + 1):
            if graph[x][i] == 0 or MST[i]: continue
            heappush(heap, (graph[x][i], i))
    return tw

n, m = int(input()), int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
print(prim(1))