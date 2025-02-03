from itertools import permutations
import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
boxes = list(map(int, input().split()))
ans = 50 * N * K
for seq in permutations(boxes, N):
    i = 0
    tw = 0
    k = K
    while k > 0:
        m = M
        while 1:
            w = seq[i % N]
            if m - w >= 0:
                tw += w
                m -= w
                i += 1
            else: break
        k -= 1
        if tw > ans: break
    if ans > tw:
        ans = tw
print(ans)