import sys
input = sys.stdin.readline
cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A = [cnt[ord(x) - 65] for x in input().rstrip()]
B = [cnt[ord(x) - 65] for x in input().rstrip()]
n = len(A)
s = []
for i in range(n): s.extend([A[i], B[i]])
l = n * 2
while l > 2:
    ns = []
    for i in range(l - 1): ns.append((s[i] + s[i + 1]) % 10)
    s, l = ns, len(ns)
print(''.join(map(str, s)))