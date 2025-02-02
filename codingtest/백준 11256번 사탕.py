import sys
input = sys.stdin.readline
mult = lambda x: x[0] * x[1]
for _ in range(int(input())):
    j, n = map(int, input().split())
    size = [mult(list(map(int, input().split()))) for _ in range(n)]
    size.sort()
    ans = 0
    while j > 0:
        j -= size.pop()
        ans +=1
    print(ans)