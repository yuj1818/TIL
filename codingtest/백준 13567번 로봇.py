import sys
input = sys.stdin.readline
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
m, n = map(int, input().split())

def find(sy, sx):
    di = 0
    for _ in range(n):
        f, x = input().split()
        x = int(x)
        if f == 'MOVE':
            ny = sy + x * d[di][0]
            nx = sx + x * d[di][1]
            if 0 <= ny < m and 0 <= nx < m:
                sy, sx = ny, nx
            else: return [-1]
        elif f == 'TURN':
            if x:
                di = di - 1 if di - 1 >= 0 else 3
            else:
                di = (di + 1) % 4
    return [sx, sy]

print(*find(0, 0))