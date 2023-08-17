T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    oven = [i for i in range(N)]
    lastIdx = oven[-1]
    while len(oven) > 1:
        d = oven.pop(0)
        cheese[d] //= 2
        if cheese[d] == 0:
            if lastIdx < M - 1:
                lastIdx += 1
                oven.append(lastIdx)
        else:
            oven.append(d)
    answer = oven[0] + 1
    print(f'#{tc} {answer}')
