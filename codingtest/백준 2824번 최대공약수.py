import math, sys, operator
from itertools import accumulate

input = sys.stdin.readlines()
a = list(accumulate(map(int, input[1].split()), operator.mul))[-1]
b = list(accumulate(map(int, input[-1].split()), operator.mul))[-1]
ans = math.gcd(a, b)
if ans > 999999999:
    ans = str(ans)[-9:]
print(ans)
