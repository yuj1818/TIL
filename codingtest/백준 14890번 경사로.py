import sys
input = sys.stdin.readline

def check(a):
    visited = [0] * N
    for i in range(1, N):
        diff = a[i] - a[i - 1]
        if abs(diff) > 1: return 0
        elif diff == 1:
            for j in range(L):
                x = i - 1 - j
                if x < 0 or a[x] != a[i - 1] or visited[x]: return 0
                visited[x] = 1
        elif diff == -1:
            for j in range(L):
                x = i + j
                if x >= N or a[x] != a[i] or visited[x]: return 0
                visited[x] = 1
    return 1

def main():
    global N, L
    N, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for row in board:
        if check(row): ans += 1
    for col in zip(*board):
        if check(col): ans += 1
    print(ans)

main()