from collections import Counter
import sys
input = sys.stdin.readline
land = [list(map(int, input().split())) for _ in range(3)]
rland = list(zip(*land))
ans = 9

def calc(a):
    a = sorted(Counter(a).items(), key=lambda x: -x[1])
    v = a[0][0]
    res = 0
    for i in range(1, len(a)):
        res += abs(v - a[i][0]) * a[i][1]
    return res

for i in range(3):
    ans = min(ans, calc(land[i]), calc(rland[i]))
    
print(ans)