import sys
input = sys.stdin.readline

def solution():
    while True:
        n, m = map(int, input().split())
        if n + m == 0: break
        rank = [0] * 10001
        for _ in range(n):
            for num in map(int, input().split()):
                rank[num] += 1
        cnt = sorted(set(rank))[-2]
        for i in range(1, 10001):
            if rank[i] == cnt:
                print(i, end=' ')
        print()

solution()