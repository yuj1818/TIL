import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(set(list(map(int, input().split()))))
cnt = len(nums)
arr = []

def dfs(l, idx):
    if l == m:
        print(' '.join(map(str, arr)))
        return

    for i in range(idx, cnt):
        arr.append(nums[i])
        dfs(l + 1, i)
        arr.pop()

dfs(0, 0)