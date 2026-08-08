from collections import defaultdict, Counter
group = defaultdict(int)
n = int(input())
for _ in range(n):
    s = sorted(Counter(input()).items())
    k = ''.join([f'{k}{v}' for k, v in s])
    group[k] += 1
print(sorted(group.values(), reverse=True)[0])