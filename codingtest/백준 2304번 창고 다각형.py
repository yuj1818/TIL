N = int(input())
pillars = {}
max_h = 0
for i in range(N):
    L, H = map(int, input().split())
    pillars[L] = H
    if max_h < H:
        max_h = H
        max_x = L
pillars = sorted(pillars.items())
max_idx = pillars.index((max_x, max_h))
area = 0
pre_x = 0
pre_y = 0
for x, y in pillars[:max_idx + 1]:
    if pre_y <= y:
        area += (x - pre_x) * pre_y
        pre_x = x
        pre_y = y
pre_x = 0
pre_y = 0
for i in range(N - 1, max_idx - 1, -1):
    if pre_y <= pillars[i][1]:
        area += abs(pillars[i][0] - pre_x) * pre_y
        pre_x = pillars[i][0]
        pre_y = pillars[i][1]
area += max_h
print(area)
