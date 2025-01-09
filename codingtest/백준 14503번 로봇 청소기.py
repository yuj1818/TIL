import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    cnt = 1
    arr[r][c] = 2
    while 1:
        for _ in range(4):
            d = (d + 3) % 4
            nr, nc = r + dr[d], c + dc[d]
            if arr[nr][nc] == 0:
                arr[nr][nc] = 2
                cnt += 1
                r, c = nr, nc
                break
        else:
            r, c = r - dr[d], c - dc[d]
            if arr[r][c] == 1: return cnt

print(main())