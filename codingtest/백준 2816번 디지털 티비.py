import sys
input = sys.stdin.readline
n = int(input())
ch = [input().rstrip() for _ in range(n)]
idx1, idx2 = ch.index('KBS1'), ch.index('KBS2')
idx2 += 1 if idx2 < idx1 else 0
print('1' * idx1 + '4' * idx1 + '1' * idx2 + '4' * (idx2 - 1))