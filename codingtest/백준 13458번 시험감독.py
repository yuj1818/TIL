import sys
input = sys.stdin.readline
n = input()
a = input().split(' ')
b, c = map(int, input().split(' '))
ans = 0
for x in a:
    ans += 1
    r = int(x) - b
    if r > 0:
        ans += r // c
        if r % c == 0: continue
        ans += 1
print(ans)