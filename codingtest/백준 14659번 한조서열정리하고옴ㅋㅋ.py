n = int(input())
h = list(map(int, input().split()))
s = 0
res = []
for i in range(1, n):
    if h[i] > h[s]:
        res.append(i - s - 1)
        s = i
res.append(i - s)
print(max(res))