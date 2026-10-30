from heapq import heappush, heappop
n = int(input())
hq = []
for _ in range(n):
    s = input().split()
    if s[0] == 'push':
        heappush(hq, -int(s[1]))
    elif s[0] == 'pop':
        print(-heappop(hq))
    elif s[0] == 'size':
        print(len(hq))
    elif s[0] == 'empty':
        print(0 if hq else 1)
    else:
        print(-hq[0])