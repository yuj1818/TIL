n = int(input())
cnt = 0
i = 0
while 1:
    if n % 5:
        n -= 2
        cnt += 1
    else:
        cnt += n // 5
        break
    if n < 0: break
if n < 0: print(-1)
else: print(cnt)