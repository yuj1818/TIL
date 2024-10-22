cnt = 0
for i in range(1, int(input()) + 1):
    if i < 100:
        cnt += 1
    else:
        s = list(map(int, str(i)))
        if s[1] - s[0] == s[2] - s[1]:
            cnt += 1
print(cnt)