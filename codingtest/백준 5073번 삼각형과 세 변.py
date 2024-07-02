import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    maxV = max(a, b, c)
    if a + b + c - maxV <= maxV:
        print('Invalid')
    else:
        rm = len({a, b, c})
        if rm == 1:
            print('Equilateral')
        elif rm == 2:
            print('Isosceles')
        else:
            print('Scalene')