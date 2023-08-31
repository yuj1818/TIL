T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())))
    capacities = sorted(list(map(int, input().split())))
    ans = 0
    while weights and capacities:
        w = weights.pop()
        if w <= capacities[-1]:
            ans += w
            capacities.pop()
    print(f'#{tc} {ans}')