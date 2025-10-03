import sys
input = sys.stdin.readline
n = int(input())
res = [0]
for x in list(map(int, input().split())):
    if x: res.append(res[-1] + 1)
    else: res.append(x)
print(sum(res))