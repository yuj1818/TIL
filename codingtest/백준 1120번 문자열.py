import sys
x, y = sys.stdin.readline().rstrip().split()
ans = 50
for i in range(len(y) - len(x) + 1):
    cnt = 0
    for j in range(len(x)):
        if x[j] != y[i + j]: cnt += 1
    if cnt < ans: ans = cnt
print(ans)