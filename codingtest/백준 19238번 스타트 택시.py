from heapq import heappush, heappop
import sys
input = sys.stdin.readline
dyx = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def find_person(ti, tj):
    hq = []
    heappush(hq, (0, ti, tj))
    visited = [[0] * N for _ in range(N)]
    visited[ti][tj] = 1

    while hq:
        d, y, x = heappop(hq)
        if (y, x) in customer: return y, x, d
        if f == d: continue
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not board[ny][nx] and not visited[ny][nx]:
                heappush(hq, (d + 1, ny, nx))
                visited[ny][nx] = 1
    return -1

def drive(si, sj, ei, ej):
    q = [(si, sj, 0)]
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    while q:
        y, x, d = q.pop(0)
        if (y, x) == (ei, ej): return d
        if f - d == 0: continue
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not board[ny][nx] and not visited[ny][nx]:
                q.append((ny, nx, d + 1))
                visited[ny][nx] = 1
    return -1

def main():
    global N, f, board, customer
    N, M, f = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ti, tj = map(lambda x: int(x) - 1, input().split())
    customer = dict()
    for _ in range(M):
        si, sj, ei, ej = map(lambda x: int(x) - 1, input().split())
        customer[(si, sj)] = (ei, ej)

    while customer:
        res = find_person(ti, tj)
        if res == -1: return -1
        ti, tj, d = res
        f -= d
        ei, ej = customer[(ti, tj)]
        res = drive(ti, tj, ei, ej)
        if res == -1: return -1
        f += res
        customer.pop((ti, tj))
        ti, tj = ei, ej
    return f

print(main())