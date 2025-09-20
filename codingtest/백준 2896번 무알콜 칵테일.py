import math, sys
input = sys.stdin.readline
q = list(map(int, input().split()))
r = list(map(int, input().split()))
gcd = math.gcd(*r)
r = list(map(lambda x: x // gcd, r))
m = min([q[i] / r[i] for i in range(3)])
print(' '.join([str(q[i] - m * r[i]) for i in range(3)]))