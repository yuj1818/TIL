import sys
s = int(sys.stdin.readline())
sq = int((s * 2) ** 0.5)
print(sq - 1 if (sq - 1) * sq // 2 <= s < sq * (sq + 1) // 2 else sq)