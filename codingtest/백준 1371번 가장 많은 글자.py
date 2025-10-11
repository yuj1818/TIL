import sys
from collections import defaultdict
d = defaultdict(int)
for line in sys.stdin.readlines():
    for x in line.strip():
        if x == ' ': continue
        d[x] += 1
sorted_d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
max_v = sorted_d[0][1]
for k, v in sorted_d:
    if v < max_v: break
    print(k, end='')