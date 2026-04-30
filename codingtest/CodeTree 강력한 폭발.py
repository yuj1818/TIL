def launch(idx, bombs):
    global ans
    if idx == B:
        ans = max(ans, len(bombs))
        return
    y, x = pos[idx]
    for i in range(3):
        b = set()
        for dy, dx in kind[i]:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n): continue
            b.add((ny, nx))
        launch(idx + 1, bombs | b)
            

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
kind = [[(-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0)], [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)], [(0, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]]
ans = 0
pos = []
B = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]: 
            B += 1
            pos.append((i, j))
launch(0, set())
print(ans)
