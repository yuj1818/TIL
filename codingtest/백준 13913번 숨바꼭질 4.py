import sys
input = sys.stdin.readline

def find():
    q = [n, -1]
    cnt = 1
    for x in q:
        if x == -1:
            if q[-1] == -1: break
            q.append(-1)
            cnt += 1
            continue
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= MAX and not dp[nx]:
                q.append(nx)
                dp[nx] = cnt
                pre[nx] = x
                if nx == k:
                    seq = []
                    while nx != -1:
                        seq.append(nx)
                        nx = pre[nx]
                    return cnt, seq[::-1]

def main():
    global n, k, MAX, dp, pre
    n, k = map(int, input().split())
    if n == k: return 0, [n]
    if n > k: return n - k, [x for x in range(n, k - 1, -1)]
    dp = [0] * (k + 2)
    pre = [-1] * (k + 2)
    dp[n] = -1
    MAX = k + 1
    return find()

t, seq = main()
print(t)
sys.stdout.write(' '.join(map(str, seq)))