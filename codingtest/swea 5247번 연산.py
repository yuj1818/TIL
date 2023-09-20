T = int(input())
L = 1000000
def bfs(s):
    q = []
    q.append((s, 0))
    visited = set()
    visited.add(s)
    while q:
        t, cnt = q.pop(0)
        if t == N:
            return cnt
        if t % 2 == 0 and 0 < t // 2 <= L // 2 and t // 2 not in visited:
            visited.add(t // 2)
            q.append((t // 2, cnt + 1))
        if 1 < t + 1 <= L + 1 and t + 1 not in visited:
            visited.add(t + 1)
            q.append((t + 1, cnt + 1))
        if -1 < t - 1 <= L - 1 and t - 1 not in visited:
            visited.add(t - 1)
            q.append((t - 1, cnt + 1))
        if 10 < t + 10 <= L + 10 and t + 10 not in visited:
            visited.add(t + 10)
            q.append((t + 10, cnt + 1))

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = bfs(M)
    print(f'#{tc} {ans}')