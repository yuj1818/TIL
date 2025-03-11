from collections import deque
import sys
input = sys.stdin.readline

d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
n, q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**n)]
la = list(map(int, input().split()))
SIZE = 2 ** n

def fire(board, SIZE, size):
    nboard = [[0] * SIZE for i in range(2 ** n)]
    for r in range(0, SIZE, size):
        for c in range(0, SIZE, size):
            for i in range(size):
                for j in range(size):
                    nboard[r + j][c + size - i - 1] = board[r + i][c + j]
    board = nboard
    melted = []
    for y in range(SIZE):
        for x in range(SIZE):
            cnt = 0
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < SIZE and 0 <= nx < SIZE and board[ny][nx]:
                    cnt += 1
            if cnt < 3 and board[y][x]: melted.append((y, x))
    for y, x in melted:
        board[y][x] -= 1
    return board

def calc(board, SIZE):
    visited = [[0] * SIZE for _ in range(SIZE)]
    total = 0
    max_size = 0
    for y in range(SIZE):
        for x in range(SIZE):
            size = 0
            if visited[y][x] or not board[y][x]: continue
            q = deque([(y, x)])
            visited[y][x] = 1
            while q:
                r, c = q.popleft()
                total += board[r][c]
                size += 1
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < SIZE and 0 <= nc < SIZE and not visited[nr][nc] and board[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
            if max_size < size: max_size = size
    print(total)
    print(max_size)

for l in la:
    board = fire(board, SIZE, 2 ** l)

calc(board, SIZE)