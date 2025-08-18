import sys
input = sys.stdin.readline
n, m = map(int, input().split())
scores = list(map(int, input().split()))
res = []
for _ in range(m):
    idx, *ans = input().strip().split()
    res.append((int(idx), sum([scores[i] for i in range(n) if ans[i] == 'O'])))
res.sort(key=lambda x: (-x[1], x[0]))
print(' '.join(map(str, res[0])))