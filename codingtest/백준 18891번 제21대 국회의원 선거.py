from math import modf
import sys
input = sys.stdin.readline
trans = lambda x: [x[0], int(x[1]), int(x[2])]
p, v = map(int, input().split())
groups = [trans(input().strip().split()) for _ in range(p)]
valid_v = 0
r = 253
for group in groups:
    valid_v += group[-1]
    r -= group[1]
valid_idx = set()
for i in range(p):
    if groups[i][1] >= 5 or groups[i][-1] / valid_v >= 0.03:
        valid_idx.add(i)
    else:
        valid_v -= groups[i][-1]
        r += groups[i][1]
for i in valid_idx:
    groups[i].append(groups[i][-1] / valid_v)
s = [0] * p
for i in valid_idx:
    s[i] = ((300 - r) * groups[i][-1] - groups[i][1]) / 2
    if s[i] < 1: s[i] = 0
    else: round(s[i])
total_s = sum(s)
lv = len(valid_idx)
if total_s != 30:
    _s = []
    if total_s > 30:
        for i in valid_idx:
            _s.append([i, *modf(s[i] * 30 / total_s)])
    else:
        for i in valid_idx:
            _s.append([i, *modf(s[i] + (30 - total_s) * groups[i][-1])])
    for i, F, I in _s: s[i] = int(I)
    total = sum(s)
    if total != 30:
        _s.sort(key=lambda x: (-x[1], s[0]))
        for x in range(30 - total):
            s[_s[x % lv][0]] += 1
t = [0] * p
_t = []
for i in valid_idx:
    _t.append([i, *modf(17 * groups[i][-1])])
for i, F, I in _t: t[i] = int(I)
total = sum(t)
if total != 17:
    _t.sort(key=lambda x: (-x[1], s[0]))
    for x in range(17 - total):
        t[_t[x % lv][0]] += 1

res = [[groups[i][0], groups[i][1] + s[i] + t[i]] for i in range(p)]
res.sort(key= lambda x: (-x[-1], x[0]))
for x in res: print(*x)