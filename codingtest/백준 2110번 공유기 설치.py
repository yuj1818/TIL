import sys

def bs(pos, c):
    def check(n):
        pre, cnt = pos[0], 1
        for v in pos[1:]:
            if v - pre < n: continue
            cnt += 1
            pre = v
        return cnt >= c

    pos.sort()
    s, e = 0, (pos[-1] - pos[0]) // (c - 1) + 1
    while s < e:
        m = (s + e) // 2
        if check(m): s = m + 1
        else: e = m
    return s-1

input = sys.stdin.readline
N, C = map(int, input().split())
pos = [int(input()) for _ in range(N)]
sys.stdout.write(str(bs(pos, C)))