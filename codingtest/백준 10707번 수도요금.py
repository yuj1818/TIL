import sys
a, b, c, d, p = [int(sys.stdin.readline()) for _ in range(5)]
print(min(a * p, b if p <= c else b + d * (p - c)))