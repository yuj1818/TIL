import sys
input = sys.stdin.readline

def main():
    n, d = map(int, input().split())
    dp = [i for i in range(d + 1)]
    for s, e, w in sorted([list(map(int, input().split())) for _ in range(n)], key= lambda x: x[0]):
        if e <= d and e - s > w and dp[e] > (w + dp[s]):
            for i in range(e, d + 1):
                dp[i] = min(dp[i], dp[s] + w + i - e)
    print(dp[-1])

if __name__ == '__main__':
    main()