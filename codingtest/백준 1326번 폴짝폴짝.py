import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def bfs():
    q = [a]
    visited = [0] * n
    visited[a] = 1
    cnt = 0
    while q:
        nxt = []
        cnt += 1
        for x in q:
            for i in range(x % bridge[x], n, bridge[x]):
                if not visited[i]:
                    if i == b: return cnt
                    visited[i] = 1
                    nxt.append(i)
        q = nxt
    return -1

n = int(input())
bridge = list(map(int, input().split()))
a, b = map(lambda x: int(x) - 1, input().split())
print(bfs())