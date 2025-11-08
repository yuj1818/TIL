import sys
input = sys.stdin.readline
s = []
for _ in range(int(input())):
    n = input().rstrip()
    if n == '2': print(s.pop() if s else -1)
    elif n == '3': print(len(s))
    elif n == '4': print(0 if s else 1)
    elif n == '5': print(s[-1] if s else -1)
    else:
        n, x = map(int, n.split())
        s.append(x)