import sys
a, b = zip(*sorted([(i, int(sys.stdin.readline())) for i in range(1,9)], key=lambda x: -x[1])[:5])
print(sum(b))
print(*sorted(a))