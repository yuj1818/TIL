from itertools import combinations
n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = float('inf')
for comb in combinations(points, m):
    dist = 0
    mp1, mp2 = [], []
    for p1, p2 in combinations(comb, 2):
        v = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
        if v > dist: 
            dist = v
            mp1, mp2 = p1, p2
    ans = min((mp1[0] - mp2[0]) ** 2 + (mp1[1] - mp2[1]) ** 2, ans)
print(ans)
