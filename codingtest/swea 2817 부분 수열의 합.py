T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(1 << N):
        a = []
        for j in range(N):
            if i & (1 << j):
                a.append(A[j])
        if sum(a) == K:
            cnt += 1
    print(f'#{tc} {cnt}')