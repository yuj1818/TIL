import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
cnt, ans, i = 0, 0, 0

while i < m - 2:
    if s[i:i+3] == 'IOI':
        cnt += 1
        if cnt == n:
            cnt -= 1
            ans += 1
        i += 2
    else:
        cnt = 0
        i += 1

print(ans)