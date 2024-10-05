import sys
input = sys.stdin.readline
tc = int(input())

def solution(n, k, t, m):
    score = [[0] * (k + 1) for _ in range(n + 1)]
    cnt = [0] * (n + 1)
    rec = [0] * (n + 1)
    for idx in range(m):
        i, j, s = map(int, input().split())
        if s > score[i][j]:
            score[i][j] = s
        cnt[i] += 1
        rec[i] = idx
    total = [(sum(score[i]), cnt[i], rec[i], i) for i in range(1, n + 1)]
    total = sorted(total, key=lambda x: (-x[0], x[1], x[2]))
    for i in range(n):
        if total[i][-1] == t:
            print(i + 1)
            return

for _ in range(tc):
    n, k, t, m = map(int, input().split())
    solution(n, k, t, m)