import sys
input = sys.stdin.readline
coin = [25, 10, 5, 1]
for _ in range(int(input())):
    c = int(input())
    for x in coin:
        print(c // x, end=' ')
        c %= x
    print()