import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    m = int(input())
    dp = [[0] * 2 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, i + 2):
            s, e = i, j
            cnt = -1
            while 1:
                if 1 <= s and e <= n and nums[s] == nums[e]:
                    s -= 1
                    e += 1
                    cnt += 1
                else: break
            dp[i][j - i] = cnt
    for _ in range(m):
        s, e = map(int, input().split())
        print(1 if dp[(s + e) // 2][(s + e) % 2] >= (s + e) // 2 - s else 0)
        
main()