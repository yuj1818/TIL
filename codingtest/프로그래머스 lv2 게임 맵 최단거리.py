from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
N = M = 0

def solution(maps):
    global N, M, min_v
    N = len(maps)
    M = len(maps[0])
    ans = find_fast_way(0, 0, maps)
    if ans:
        return ans
    else:
        return -1

def find_fast_way(y, x, maps):
    q = deque()
    visited = [[0] * M for _ in range(N)]
    q.append((y, x))
    visited[y][x] = 1
    while q:
        r, c = q.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c]
        for d in range(4):
            nc = c + dx[d]
            nr = r + dy[d]
            if 0 <= nc < M and 0 <= nr < N and not visited[nr][nc] and maps[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))