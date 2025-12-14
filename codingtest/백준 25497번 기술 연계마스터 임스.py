import sys
input = sys.stdin.readline
input()
sk = []
lr = []
ans = 0
for x in input():
    if x.isdigit():
        ans += 1
        continue
    if x == 'S': sk.append(1)
    elif x == 'L': lr.append(1)
    elif x == 'K':
        if not sk: break
        sk.pop()
        ans += 1
    elif x == 'R':
        if not lr: break
        lr.pop()
        ans += 1
print(ans)