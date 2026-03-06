import sys

input = sys.stdin.readline
s = input().rstrip()
cnt = [[0] * 26]
for i, c in enumerate(s):
    cnt.append(cnt[-1][:])
    cnt[i + 1][ord(c) - 97] += 1
for _ in range(int(input())):
    c, *p = input().rstrip().split()
    l, r = map(int, p)
    print(cnt[r + 1][ord(c) - 97] - cnt[l][ord(c) - 97])
