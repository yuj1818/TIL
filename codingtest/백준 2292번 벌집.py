N = int(input())
s = 1
cnt = 1
while s < N:
    s += 6 * cnt
    cnt += 1
print(cnt)