import sys
input = sys.stdin.readline
N = int(input())
arr = [input().strip() for _ in range(N)]
ans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == '.': continue
        v = int(arr[i][j])
        ans[i][j] = '*'
        for dy, dx in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
            ny, nx = i + dy, j + dx
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == '.' and ans[ny][nx] != 'M':
                ans[ny][nx] += v
                if ans[ny][nx] > 9: ans[ny][nx] = 'M'
for r in ans: print(''.join(map(str, r)))