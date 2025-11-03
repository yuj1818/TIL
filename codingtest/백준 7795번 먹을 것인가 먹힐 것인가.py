from bisect import bisect_left
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    A = sorted(map(int, input().split()), reverse=True)
    B = sorted(map(int, input().split()))
    cnt = 0
    for x in A: cnt += bisect_left(B, x)
    print(cnt)