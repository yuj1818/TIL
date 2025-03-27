import sys
input = sys.stdin.readline
MAX = 400001
p = [[0, 2, 2, 2, 2],
     [2, 1, 3, 4, 3],
     [2, 3, 1, 3, 4],
     [2, 4, 3, 1, 3],
     [2, 3, 4, 3, 1]]

def main():
    a = list(map(int, input().split()))
    n = len(a)
    a = [a.pop()] + a
    dp = [MAX] * 5
    dp[0] = 0

    for i in range(n - 1):
        f, b = a[i], a[i + 1]
        if f == b:
            dp = [x + 1 for x in dp]
            continue
        ndp = [p[f][b] + x for x in dp]
        for j in range(5):
            if p[j][b] + dp[j] < ndp[f]:
                ndp[f] = p[j][b] + dp[j]
        dp = ndp

    print(min(dp))

main()