import sys
a, b = map(int, input().split())
r = int(input())
v = set([(a, b)])
t = 0
while 1:
    t += 1
    if a + b + 2 < r: a, b = a + 1, b + 1
    else: a, b = a // 2, b // 2
    if (a, b) in v:
        print(t)
        sys.exit()
    else: v.add((a, b))