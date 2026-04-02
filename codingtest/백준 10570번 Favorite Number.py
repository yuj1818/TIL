from collections import Counter
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    print(sorted(Counter([int(input()) for _ in range(n)]).items(), key=lambda x: (-x[1], x[0]))[0][0])
