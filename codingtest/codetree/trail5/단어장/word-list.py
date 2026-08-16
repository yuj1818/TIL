from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()
for _ in range(n):
    s = input()
    sd[s] = sd.get(s, 0) + 1
for k, v in sd.items():
    print(k, v)