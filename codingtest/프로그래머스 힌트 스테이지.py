
from itertools import product

def solution(cost, hint):
    N = len(cost)
    ans = float('inf')
    cases = list(product((0, 1), repeat=N - 1))
    for case in cases:
        hcnt = [0] * (N + 1)
        total = 0
        for i in range(N - 1):
            if case[i]:
                total += hint[i][0]
                for j in range(1, len(hint[i])): hcnt[hint[i][j]] += 1
        for s in range(N): total += cost[s][min(N - 1, hcnt[s + 1])]
        if ans > total: ans = total
    return ans
