import sys
input = sys.stdin.readline
n = int(input())
total_scores = [0] * n

def calc(scores):
    res = [0] * n
    scores = sorted(enumerate(scores), key=lambda x: -x[1])
    rank, pre, same = 0, -1, 1
    for idx, score in scores:
        if pre != score: 
            rank += same
            same = 1
        else: same += 1
        res[idx] = rank
        pre = score
    print(*res)

for _ in range(3):
    scores = list(map(int, input().split()))
    calc(scores)
    for i in range(n):
        total_scores[i] += scores[i]
calc(total_scores)