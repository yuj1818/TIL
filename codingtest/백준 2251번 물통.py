import sys
input = sys.stdin.readline
move = [[0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1]]
size = list(map(int, input().split()))
q = [[0, 0, size[-1]]]
visited = set([(0, 0, size[-1])])
ans = set()
while q:
    cur = q.pop(0)
    if cur[0] == 0: ans.add(cur[-1])
    for s, e in move:
        nxt = cur[:]
        if nxt[s] > 0:
            nxt[e] += nxt[s]
            nxt[s] = 0
            if nxt[e] > size[e]:
                nxt[s] += nxt[e] - size[e]
                nxt[e] = size[e]
        if tuple(nxt) not in visited:
            q.append(nxt)
            visited.add(tuple(nxt))
print(' '.join(map(str, sorted(ans))))