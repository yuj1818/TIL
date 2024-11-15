import sys
input = sys.stdin.readline
n = int(input())
s = input()
ans, cnt, acc = 0, 0, 0
for i in range(n):
    if s[i] == '2':
        cnt += 1
        acc += cnt
        ans += acc
    else:
        acc, cnt = 0, 0
print(ans)