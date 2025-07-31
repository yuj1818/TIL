import sys
input = sys.stdin.readline

def find(x):
    if usado[x] < 0: return x
    usado[x] = find(usado[x])
    return usado[x]

N, Q = map(int, input().split())
edges = sorted([list(map(int, input().split())) for _ in range(N - 1)], key=lambda x: x[-1])
questions = sorted([list(map(int, input().split())) + [i] for i in range(Q)], reverse=True)
usado = [-1] * (N + 1)
ans = []
for k, v, i in questions:
    while edges and edges[-1][-1] >= k:
        p, q, r = edges.pop()
        pr, qr = find(p), find(q)
        if pr < qr:
            usado[pr] += usado[qr]
            usado[qr] = pr
        elif pr > qr:
            usado[qr] += usado[pr]
            usado[pr] = qr
    vr = find(v)
    ans.append((i, -usado[vr] - 1))
ans.sort()
for _, cnt in ans: print(cnt)