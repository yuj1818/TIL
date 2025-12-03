import sys
from collections import Counter
a = [int(sys.stdin.readline()) for _ in range(10)]
print(int(sum(a) / 10))
print(sorted(Counter(a).items(), key=lambda x: -x[1])[0][0])