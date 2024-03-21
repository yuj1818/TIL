def solution(triangle):
    answer = triangle[0][0]
    dp = [[0] * (i + 1) for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
    for d in range(0, len(triangle)-1):
        for i in range(d+1):
            dp[d+1][i] = max(dp[d][i] + triangle[d+1][i], dp[d+1][i])
            dp[d+1][i+1] = max(dp[d][i] + triangle[d+1][i+1], dp[d+1][i+1])
            answer = max(answer, dp[d+1][i], dp[d+1][i+1])
    return answer
