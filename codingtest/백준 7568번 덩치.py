N = int(input())
sizes = [list(map(int, input().split())) for _ in range(N)]
weights, heights = zip(*sizes)
for w, h in sizes:
    cnt = 0
    for nw, nh in sizes:
        if nw > w and nh > h:
            cnt += 1
    print(cnt + 1, end=' ')