import sys
input = sys.stdin.readline

def bfs(f, s, g, u, d):
    visited = [1] + [0] * f
    visited[s] = 1
    q = [(s, 0)]
    while q:
        x, cnt = q.pop(0)
        if x == g: return cnt
        for nxt in [x + u, x - d]:
            if 0 < nxt <= f and not visited[nxt]:
                q.append((nxt, cnt + 1))
                visited[nxt] = 1
    return 'use the stairs'

def main():
    f, s, g, u, d = map(int, input().split())
    print(bfs(f, s, g, u, d))

main()