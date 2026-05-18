def tsp(mask, pos):
    if mask == (1 << n) - 1:
        if A[pos][0] > 0: return A[pos][0]
        else: return float('inf')
    if dp[pos][mask] != 0: return dp[pos][mask]
    c = float('inf')
    for nx in range(n):
        if (mask & (1 << nx)) == 0 and A[pos][nx] > 0:
            nc = A[pos][nx] + tsp(mask | (1 << nx), nx)
            c = min(c, nc)
    dp[pos][mask] = c
    return c

n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]
print(tsp(1, 0))
