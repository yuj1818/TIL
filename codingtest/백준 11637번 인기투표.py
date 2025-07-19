import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = [int(input()) for i in range(n)]
    t = sum(a)
    a = sorted(enumerate(a), key=lambda x: -x[1])
    if a[0][1] == a[1][1]: print('no winner')
    else:
        if a[0][1] > t / 2: print(f'majority winner {a[0][0] + 1}')
        else: print(f'minority winner {a[0][0] + 1}')