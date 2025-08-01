a, b = sorted(map(int, input().split()))
cnt = b - a - 1
if cnt > 0:
    print(cnt)
    for i in range(a + 1, b): print(i, end=' ')
else: print(0)