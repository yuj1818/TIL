import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(lambda x: int(x, 2), input().strip().split())
    print(format(a + b, 'b'))