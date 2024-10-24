import sys
d = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+':  1.5, 'D0': 1.0, 'F': 0}
tsco = 0
tcred = 0
for _ in range(20):
    _, n, g = sys.stdin.readline().split()
    n = float(n)
    if g=='P': continue
    tsco += n*d[g]
    tcred += n
print(tsco/tcred)