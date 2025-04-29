import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = [[0] + list(map(int, input().split())) for _ in range(n)]
    total = 0
    for i in range(n):
        for j in range(2, n + 1):
            a[i][j] += a[i][j - 1]
        total += a[i][-1]
    ans = total
    for y in range(n - 2):
        for x in range(1, n - 1):
            for d1 in range(1, x + 1):
                for d2 in range(1, n - x):
                    if y + d1 + d2 >= n: continue
                    res = [0] * 5
                    for i in range(y): res[0] += a[i][x+1]
                    for i in range(d1): res[0] += a[y+i][x-i]
                    for i in range(d2): res[2] += a[y+d1+i][x-d1+i]
                    for i in range(y+d1+d2, n): res[2] += a[i][x-d1+d2]
                    for i in range(y + 1): res[1] += a[i][-1] - a[i][x+1]
                    for i in range(d2): res[1] += a[y+i+1][-1] - a[y+i+1][x+i+2]
                    for i in range(d1): res[3] += a[y+d2+i+1][-1] - a[y+d2+i+1][x+d2-i]
                    for i in range(y + d1 + d2 + 1, n): res[3] += a[i][-1] - a[i][x-d1+d2]
                    res[-1] = total-sum(res)
                    diff = max(res) - min(res)
                    if ans > diff: ans = diff
    print(ans)
    
main()