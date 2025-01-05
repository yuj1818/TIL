import sys
input = sys.stdin.readline

def main():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[1] = p[0]
    for i in range(2, n + 1):
        dp[i] = p[i - 1]
        m = 0
        for j in range(i // 2 + 1):
            t = dp[i - j] + dp[j]
            if t > m: m = t
        dp[i] = m
    print(dp[-1])

main()