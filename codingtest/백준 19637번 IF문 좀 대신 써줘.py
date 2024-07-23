import sys, bisect
input = sys.stdin.readline
n, m = map(int, input().split())
ranks = []
scores = []
for _ in range(n):
    rank, score = input().split()
    ranks.append(rank)
    scores.append(int(score))
for _ in range(m):
    print(ranks[bisect.bisect_left(scores, int(input()))])