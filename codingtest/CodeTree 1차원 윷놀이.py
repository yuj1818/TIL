def move(x):
    global ans
    if x == n:
        cnt = 0
        for c in cur:
            if c >= m: cnt += 1
        if ans < cnt: ans = cnt
        return
    for i in range(k):
        cur[i] += nums[x]
        move(x + 1)
        cur[i] -= nums[x]

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
cur = [1 for _ in range(k)]
ans = 0
move(0)
print(ans)
