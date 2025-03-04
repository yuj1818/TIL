import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    n, *scores = list(map(int, input().split()))
    scores.sort()
    diff = [scores[i] - scores[i - 1] for i in range(1, n)]
    print(f'Class {tc}')
    print(f'Max {scores[-1]}, Min {scores[0]}, Largest gap {max(diff)}')