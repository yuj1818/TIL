from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()
for i, x in enumerate(map(int, input().split())):
    if x in sd: continue
    sd[x] = i + 1
for k, v in sd.items():
    print(k, v)