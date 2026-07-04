n = int(input())
arr = list(map(int, input().split()))
t = sum(arr)
if t % 2:
    print('No')
    exit()
v = t // 2
dp = set([0])
for x in arr:
    dp |= {prev + x for prev in dp if prev + x <= v}
if v in dp: print('Yes')
else: print('No')