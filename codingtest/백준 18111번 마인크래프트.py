from copy import deepcopy
N, M, B = map(int, input().split())
land = []
for _ in range(N):
    land.extend(list(map(int, input().split())))
min_t = 512 * N * M
h = 0
for level in range(min(land), max(land) + 1):
    working_time = 0
    nB = B
    for i in range(N * M):
        if land[i] == level:
            continue
        if land[i] > level:
            working_time += 2 * (land[i] - level)
            nB += land[i] - level
        else:
            nB -= level - land[i]
            working_time += level - land[i]
    if nB >= 0:
        if min_t >= working_time:
            min_t = working_time
            h = level

print(min_t, h)