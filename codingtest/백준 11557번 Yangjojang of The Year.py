import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = {k: int(v) for k, v in [input().rstrip().split() for _ in range(n)]}
    print(sorted(arr.items(), key=lambda x: -x[1])[0][0])
