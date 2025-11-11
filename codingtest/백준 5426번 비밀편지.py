import sys
input = sys.stdin.readline
for _ in range(int(input())):
    s = input().rstrip()
    n = int(len(s) ** 0.5)
    arr = []
    for i in range(n):
        arr.append(s[i * n: (i + 1) * n])
    print(''.join(map(lambda x: ''.join(x), list(zip(*arr))[::-1])))