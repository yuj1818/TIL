import sys
input = sys.stdin.readline
g = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
tc, ts = 0, 0
for _ in range(int(input())):
    _, c, s = input().strip().split()
    tc += int(c)
    ts += g[s] * int(c)
print(f'{round(ts / tc + 10**-10, 2):.2f}')