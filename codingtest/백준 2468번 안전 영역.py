n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

def dfs(y, x, visited, grid, h, n):
    s = [(y, x)]
    while s:
        r, c = s.pop()
        if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] <= h or visited[r][c]: continue
        visited[r][c] = True
        s.append((r + 1, c))
        s.append((r - 1, c))
        s.append((r, c + 1))
        s.append((r, c - 1))

def main(grid, n):
    min_value = min(map(min, grid))
    max_value = max(map(max, grid))
    ans = 0
    for h in range(min_value - 1, max_value):
        visited = [[False] * n for _ in range(n)]
        cnt = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > h and not visited[i][j]:
                    dfs(i, j, visited, grid, h, n)
                    cnt += 1
        ans = max(ans, cnt)
    return ans

print(main(ls, n))