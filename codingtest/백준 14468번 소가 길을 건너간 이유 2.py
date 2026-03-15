import sys
s = list(sys.stdin.readline().rstrip())
cnt = 0
c = set()
for i in range(52):
    if s[i] in c: continue
    c.add(s[i])
    for j in range(i + 1, 52):
        if s[i] == s[j]:
            x = set()
            for k in range(i + 1, j):
                if s[k] not in x:
                    cnt += 1
                    x.add(s[k])
                else: cnt -= 1
            break
print(cnt // 2)