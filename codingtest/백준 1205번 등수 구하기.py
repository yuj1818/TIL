import sys
input = sys.stdin.readline
n, s, p = map(int, input().split())
if n:
    scores=list(map(int, input().split()))
    print(-1 if n >= p and scores[p-1] >= s else next((i+1 for i in range(n) if scores[i] <= s), n+1))
else:
    print(1)