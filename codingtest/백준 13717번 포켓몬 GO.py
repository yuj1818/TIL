import sys
input = sys.stdin.readline
n = int(input())
a = ['', 0]
t = 0
for i in range(n):
    name = input().strip()
    k, m = map(int, input().split())
    c = 0
    while m >= k:
        m -= k - 2
        c += 1
    if a[1] < c: a = [name, c]
    t += c
print(t)
print(a[0])