import sys
input = sys.stdin.readline

def dfs(v, i, p, m, x, d):
    global maxV, minV
    if i == n:
        if maxV < v: maxV = v
        if minV > v: minV = v
        return
    if p > 0: dfs(v + nums[i], i + 1, p - 1, m, x, d)
    if m > 0: dfs(v - nums[i], i + 1, p, m - 1, x, d)
    if x > 0: dfs(v * nums[i], i + 1, p, m, x - 1, d)
    if d > 0: dfs(v // nums[i] if v > 0 else -((-v) // nums[i]), i + 1, p, m, x, d - 1)

n = int(input())
nums = list(map(int, input().split()))
p, m, x, d = map(int, input().split())
maxV, minV = -1 * (10 ** 9), 10 ** 9
dfs(nums[0], 1, p, m, x, d)
print(maxV)
print(minV)