from itertools import combinations
n = int(input())
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
sy, sx, ey, ex = -1, -1, -1, -1
ans = float('inf')
coins = []
for i in range(n):
    r = input()
    for j in range(n):
        if r[j] == 'S': sy, sx = i, j
        elif r[j] == 'E': ey, ex = i, j
        if r[j].isdigit():
            coins.append((int(r[j]), i, j))
if len(coins) < 3:
    print(-1)
    exit()
coins.sort()
for comb in combinations(coins, 3):
    dist = abs(sy - comb[0][1]) + abs(sx - comb[0][2])
    for i in range(2):
        _, y1, x1 = comb[i]
        _, y2, x2 = comb[i + 1]
        dist += abs(y1 - y2) + abs(x1 - x2)
        if dist > ans: break
    else:
        dist += abs(y2 - ey) + abs(x2 - ex)
        if dist < ans: ans = dist
if ans == float('inf'): print(-1)
else: print(ans)
