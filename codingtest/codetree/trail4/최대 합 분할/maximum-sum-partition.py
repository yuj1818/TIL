n = int(input())
arr = [0] + list(map(int, input().split()))
m = sum(arr)
dp = {0: 0}
for x in arr:
    n_dp = {k:v for k,v in dp.items()}
    for d, v in dp.items():
        a = d + x
        if n_dp.get(a, -1) < v + x:
            n_dp[a] = v + x
        b = d - x
        if n_dp.get(b, -1) < v:
            n_dp[b] = v
    dp = n_dp
print(dp.get(0, 0))