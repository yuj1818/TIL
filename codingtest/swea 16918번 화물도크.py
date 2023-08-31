T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    waiting_lst = [list(map(int, input().split())) for _ in range(N)]
    waiting_lst.sort(key=lambda x: (x[1], x[0]))
    reservation = [waiting_lst[0]]
    for i in range(1, N):
        if waiting_lst[i][0] >= reservation[-1][1]:
            reservation.append(waiting_lst[i])
    ans = len(reservation)
    print(f'#{tc} {ans}')