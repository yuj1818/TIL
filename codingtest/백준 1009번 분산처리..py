import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0: print(10)
    elif a == 1 or a == 5 or a == 6: print(a)
    elif a == 4 or a == 9:
        if b % 2: print(a)
        else: print((a ** 2) % 10)
    else:
        if b % 4: print(a ** (b % 4) % 10)
        else: print(a ** 4 % 10)