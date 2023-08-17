for _ in range(1, 11):
    tc = int(input())
    data = list(map(int, input().split()))
    i = 1
    while data[-1] > 0:
        if i > 5:
            i = 1
        d = data.pop(0)
        data.append(d - i if d - i > 0 else 0)
        i += 1
    print(f'#{tc}', *data)