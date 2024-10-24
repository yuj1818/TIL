import sys
s = sys.stdin.readline().strip()
ac, cnt = s.count('a'), len(s)
s+=s
for i in range(len(s)-ac+1):
    cnt = min(cnt, s[i:ac+i].count('b'))
print(cnt)