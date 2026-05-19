from itertools import permutations
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for p in permutations(range(n), n):
    mv = float('inf')
    for i in range(n):
        mv = min(mv, grid[i][p[i]])
    ans = max(ans, mv)
print(ans)
