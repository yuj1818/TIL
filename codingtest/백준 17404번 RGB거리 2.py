import sys
input = sys.stdin.readline
INF = float('inf')

def main():
    n = int(input())
    costs = [list(map(int, input().split())) for _ in range(n)]
    ans = INF
    for c in [0, 1, 2]:
        dp = [[INF] * 3 for _ in range(n)]
        dp[0][c] = costs[0][c]
        for i in range(1, n):
            dp[i] = [costs[i][idx] + v for idx, v in enumerate([min(dp[i - 1][1], dp[i - 1][2]), min(dp[i - 1][0], dp[i - 1][2]), min(dp[i - 1][0], dp[i - 1][1])])]
        dp[-1][c] = INF
        ans = min(ans, min(dp[-1]))
    print(ans)

main()