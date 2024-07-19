import sys
input = sys.stdin.readline
n = int(input())
org = list(input().rstrip())
ans = 0
for _ in range(n - 1):
    word = input().rstrip()
    cnt = 0
    comp = [x for x in org]
    for c in word:
        if c in comp:
            comp.remove(c)
        else:
            cnt += 1

    if cnt <= 1 and len(comp) <= 1:
        ans += 1

print(ans)