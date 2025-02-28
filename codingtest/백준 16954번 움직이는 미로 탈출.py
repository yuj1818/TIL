import sys
d = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 0)]

def main():
    board = [list(sys.stdin.readline().strip()) for _ in range(8)]
    visited = [[0] * 8 for _ in range(8)]
    visited[7][0] = 1
    s = [(7, 0)]
    t = 1
    while s and t < 9:
        tmp = []
        while s:
            y, x = s.pop()
            for dy, dx in d:
                ny, nx = y + dy, x + dx
                if 0 <= ny < 8 and 0 <= nx < 8 and visited[ny][nx] <= t:
                    if board[ny][nx] == '.' and (ny == 0 or board[ny - 1][nx] == '.'):
                        visited[ny][nx] = t + 1
                        tmp.append((ny, nx))
        board.pop()
        board.insert(0, ['.'] * 8)
        s = tmp
        t += 1

    print(1 if t > 8 else 0)

main()