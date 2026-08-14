from sortedcontainers import SortedDict
sd = SortedDict()
n = int(input())
for _ in range(n):
    s = input()
    sd[s] = sd.get(s, 0) + 1
for k, v in sd.items():
    print(f'{k} {v / n * 100:.4f}')