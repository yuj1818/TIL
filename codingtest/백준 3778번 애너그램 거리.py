import sys
input = sys.stdin.readline
for t in range(1, int(input()) + 1):
    aa = [0] * 26
    for c in input().strip():
        aa[ord(c) - 97] += 1
    for c in input().strip():
        aa[ord(c) - 97] -= 1
    aa = map(abs, aa)
    print(f'Case #{t}: {sum(aa)}')