import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def dfs(y, x):
    MAP[y][x] = 0
    for dy, dx in d:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w and MAP[ny][nx]: dfs(ny, nx)

def main():
    global w, h, MAP
    while 1:
        w, h = map(int, input().split())
        if w + h == 0: break
        MAP = [list(map(int, input().split())) for _ in range(h)]
        ans = 0
        for i in range(h):
            for j in range(w):
                if MAP[i][j]:
                    ans += 1
                    dfs(i, j)
        print(ans)

if __name__ == '__main__':
    main()