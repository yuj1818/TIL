import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
words = Counter([i for _ in range(n) if len(i := input()) > m])
ans = sorted(words)
ans = sorted(ans, key=len, reverse=True)
ans = sorted(ans, key=words.get, reverse=True)
sys.stdout.write(''.join(ans))