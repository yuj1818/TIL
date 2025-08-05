import sys
input = sys.stdin.readline
B, C, D = map(int, input().split())
b = sorted(map(int, input().split()))
c = sorted(map(int, input().split()))
d = sorted(map(int, input().split()))
prev = 0
nxt = 0
for _ in range(min(len(b), len(c), len(d))):
    s = b.pop() + c.pop() + d.pop()
    prev += s
    nxt += int(s * 0.9)
rest = sum(b) + sum(c) + sum(d)
print(prev + rest)
print(nxt + rest)