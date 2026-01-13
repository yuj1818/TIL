import sys
input = sys.stdin.readline

def color():
    v, e = map(int, input().split())
    arr = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)
    for i in range(1, v + 1):
        if arr[i]: continue
        arr[i] = 1
        q = [i]
        while q:
            x = q.pop(0)
            nc = arr[x] % 2 + 1
            for nx in graph[x]:
                if not arr[nx]:
                    arr[nx] = nc
                    q.append(nx)
                elif arr[nx] != nc: return 'NO'
    return 'YES'

for _ in range(int(input())): print(color())