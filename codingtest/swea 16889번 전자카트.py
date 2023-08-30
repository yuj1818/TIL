from itertools import permutations
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    min_v = sum(max(row) for row in area)
    for perm in permutations(range(1, N), N - 1):
        sum_v = 0
        start = 0
        for sequence in perm:
            sum_v += area[start][sequence]
            if sum_v >= min_v:
                break
            start = sequence
        sum_v += area[start][0]
        min_v = min(min_v, sum_v)
    print(f'#{tc} {min_v}')