def solution(m, n, puddles):
    ways = [[1] * m for _ in range(n)]
    
    for x, y in puddles:
        
        if y - 1 == 0:
            for nx in range(x - 1, m):
                ways[y - 1][nx] = 0
                
        if x - 1 == 0:
            for ny in range(y - 1, n):
                ways[ny][x - 1] = 0

        ways[y - 1][x - 1] = 0
    
    for i in range(1, n):
        for j in range(1, m):
            if ways[i][j]:
                ways[i][j] = ways[i - 1][j] + ways[i][j - 1]
    
    return ways[n - 1][m - 1] % 1000000007