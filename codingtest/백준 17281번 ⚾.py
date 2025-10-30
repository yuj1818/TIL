from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]
cases = list(permutations(range(1, 9), 8))
ans = 0
for case in cases:
    case = list(case)
    case.insert(3, 0)
    score = 0
    idx = 0
    for i in range(n):
        b1, b2, b3, o = 0, 0, 0, 0
        while o < 3:
            p = case[idx]
            res = scores[i][p]
            if res == 0: o += 1
            elif res == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif res == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif res == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            idx = (idx + 1) % 9
    ans = max(score, ans)
print(ans)