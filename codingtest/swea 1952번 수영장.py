T = int(input())
for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = min(dp[i - 1] + prices[0] * plan[i - 1], dp[i - 1] + prices[1], dp[i - 3] + prices[2] if i >= 3 else float('inf'))
    dp[12] = min(dp[12], prices[-1])
    print(f'#{tc} {dp[-1]}')