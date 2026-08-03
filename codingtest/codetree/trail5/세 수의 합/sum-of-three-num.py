from collections import Counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))
d = Counter(arr)
ans = 0
for i in range(n):
    d[arr[i]] -= 1
    for j in range(i):
        diff = k - arr[i] - arr[j]
        if diff in d: ans += d[diff]
print(ans)