from collections import Counter
n, k = map(int, input().split())
a = sorted(Counter(map(int, input().split())).items(), key=lambda x: (-x[1], -x[0]))
for i in range(k):
    print(a[i][0], end=' ')