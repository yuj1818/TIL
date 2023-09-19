T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_dif_h = sum(H)
    for i in range(1 << N):
        sum_h = 0
        for j in range(N):
            if i & (1 << j):
                sum_h += H[j]
            if sum_h > min_dif_h:
                break
        if B <= sum_h < min_dif_h:
            min_dif_h = sum_h
    min_dif = min_dif_h - B
    print(f'#{tc} {min_dif}')