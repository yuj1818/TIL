from collections import deque

def main():
    dyx = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}
    N, M, K = map(int, input().split())
    grid = [[0] * N for _ in range(N)]
    for _ in range(M):
        y, x = map(int, input().split())
        grid[y - 1][x - 1] = 2
    snake = deque([(0, 0)])
    t = 0
    for _ in range(K):
        d, p = input().split()
        dy, dx = dyx[d]
        for _ in range(int(p)):
            t += 1
            y, x = snake[0]
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N): return t
            if grid[ny][nx] != 2: 
                ty, tx = snake.pop()
                grid[ty][tx] = 0
            if grid[ny][nx] == 1: return t
            snake.appendleft((ny, nx))
            grid[ny][nx] = 1
    return t

if  __name__ == '__main__': print(main())