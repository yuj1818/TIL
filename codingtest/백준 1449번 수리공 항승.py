import sys
input = sys.stdin.readline
N, L = map(int, input().split())
pos = sorted(map(int, input().split()))
s, cnt = pos[0], 1
for i in range(1, N):
    if s <= pos[i] < s + L: continue
    else:
        s = pos[i]
        cnt += 1
print(cnt)