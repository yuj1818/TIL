import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    s, e = 0, n - 1
    while s < e:
        if a[s] + a[e] == a[i]:
            if s == i: s += 1
            elif e == i: e -= 1
            else:
                ans += 1
                break
        elif a[s] + a[e] < a[i]: s += 1
        else: e -= 1
print(ans)