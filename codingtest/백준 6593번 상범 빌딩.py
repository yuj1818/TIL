import sys
input = sys.stdin.readline
d = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (-1, 0, 0), (1, 0, 0)]

def bfs():
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    visited[sl][sr][sc] = 1
    q = [(sl, sr, sc, 0)]
    while q:
        l, r, c, cnt = q.pop(0)
        if building[l][r][c] == 'E': return cnt
        for dl, dr, dc in d:
            nl, nr, nc = l + dl, r + dr, c + dc
            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C and building[nl][nr][nc] != '#' and not visited[nl][nr][nc]:
                q.append((nl, nr, nc, cnt + 1))
                visited[nl][nr][nc] = 1
    return -1

def main():
    global L, R, C, sl, sr, sc, building
    while 1:
        L, R, C = map(int, input().split())
        if L + R + C == 0: break
        building = []
        sl, sr, sc = 0, 0, 0
        for l in range(L):
            building.append([])
            for r in range(R):
                row = list(input().strip())
                for c in range(C):
                    if row[c] == 'S':
                        sl, sr, sc = l, r, c
                        row[c] = '.'
                building[-1].append(row)
            input()
        res = bfs()
        print('Trapped!' if res < 0 else f'Escaped in {res} minute(s).')

main()