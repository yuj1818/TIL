import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    input()
    r, c = map(int, input().split())
    arr = [input().strip() for _ in range(r)]
    ans = 0
    for row in arr: ans += row.count('>o<')
    for col in map(lambda x:''.join(x), zip(*arr)): ans += col.count('vo^')
    print(ans)