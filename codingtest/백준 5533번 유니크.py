import sys
input = sys.stdin.readline
n = int(input())
scores = [0] * n
nums = []
round = [dict() for _ in range(3)]
for _ in range(n):
    num = list(map(int, input().split()))
    nums.append(num)
    for i, x in enumerate(num): round[i][x] = round[i].get(x, 0) + 1
for num in nums:
    res = 0
    for i, x in enumerate(num):
        if round[i][x] == 1: res += x
    print(res)