def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    d = [(0, 1), (1, 0), (-1, -1)]
    didx = 0
    num = 1
    g = sum([x for x in range(1, n + 1)])
    nx, ny = 0, 0
    while num <= g:
        while 0 <= ny < n and 0 <= nx <= ny and not arr[ny][nx]:
            arr[ny][nx] = num
            nx += d[didx % 3][0]
            ny += d[didx % 3][1]
            num += 1
        nx -= d[didx % 3][0]
        ny -= d[didx % 3][1]
        didx += 1
        nx += d[didx % 3][0]
        ny += d[didx % 3][1]
    ans = [item for line in arr for item in line]
    return ans