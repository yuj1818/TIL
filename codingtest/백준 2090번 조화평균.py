from fractions import Fraction
import sys
input = sys.stdin.readline
input()
a = list(map(int, input().split()))
ans = 0
for x in a: ans += Fraction(1, x)
print(f'{ans.denominator}/{ans.numerator}')
