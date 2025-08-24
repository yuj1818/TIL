import sys
from math import lcm
s, t = [sys.stdin.readline().strip() for _ in range(2)]
ls, lt = len(s), len(t)
v = lcm(ls, lt)
print(1 if v // ls * s == v // lt * t else 0)