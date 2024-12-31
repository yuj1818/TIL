import sys
input = sys.stdin.buffer.readline

def main():
    n, r, q = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    ans = [0] * (n + 1)
    s = [(r, -1)]
    seq = []

    while s:
        cur, par = s.pop()
        seq.append((cur, par))
        for w in graph[cur]:
            if w != par: s.append((w, cur))

    while seq:
        cur, par = seq.pop()
        ans[cur] = 1
        for w in graph[cur]:
            if w != par: ans[cur] += ans[w]

    for _ in range(q): print(ans[int(input())])

main()