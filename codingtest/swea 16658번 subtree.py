T = int(input())
def bfs(s):
    a = 1
    q = list()
    q.append(s)
    while q:
        t = q.pop(0)
        for w in nodes[t]:
            q.append(w)
            a += 1
    return a

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    pairs = list(map(int, input().split()))
    nodes = [[] for _ in range(E + 2)]
    for i in range(E):
        nodes[pairs[i * 2]].append(pairs[i * 2 + 1])
    print(f'#{tc} {bfs(N)}')