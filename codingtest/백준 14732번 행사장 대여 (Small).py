import sys
input = sys.stdin.readline
n = int(input())
area = set()
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            area.add((y, x))
print(len(area))