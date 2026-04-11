import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    m, w = a[i]
    if m > n - w:
        print(0)
        sys.exit()
print(1)
print(a[1][1], a[0][0] - a[1][1])
print(a[0][1] - a[2][0], a[2][1] + a[1][1] - a[0][0])
print(a[2][0], 0)
