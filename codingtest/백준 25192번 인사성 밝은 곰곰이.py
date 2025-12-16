import sys
_, *arr = map(lambda x: x.rstrip(), sys.stdin.readlines())
ans = 0
p = set()
for x in arr:
    if x == 'ENTER':
        p = set()
        continue
    if x in p: continue
    p.add(x)
    ans += 1
print(ans)