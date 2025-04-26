import sys
n = int(sys.stdin.readline())
w = list(sys.stdin.readline().strip())
for _ in range(n - 1):
    c = sys.stdin.readline().strip()
    for i in range(len(w)):
        if w[i] == c[i]: continue
        else: w[i] = '?'
print(*w, sep='')