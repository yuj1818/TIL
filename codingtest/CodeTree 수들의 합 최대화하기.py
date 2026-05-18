from itertools import permutations
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for p in permutations(range(n), n):
    total = 0
    for i in range(n):
        total += grid[i][p[i]]
    if ans < total: ans = total
print(ans)
