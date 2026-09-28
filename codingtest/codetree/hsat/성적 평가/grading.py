n = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]
scores_p = list(map(sum, zip(*scores)))
for i in range(3):
    res = [0] * n
    s = [(-1, 1001)] + sorted(enumerate(scores[i]), key=lambda x: -x[1])
    for j in range(1, n + 1):
        rank = j
        while s[rank][1] == s[rank - 1][1]: rank -= 1
        res[s[j][0]] = rank
    print(*res)
res = [0] * n
s = [(-1, 3001)] + sorted(enumerate(scores_p), key=lambda x: -x[1])
for i in range(1, n + 1):
    rank = i
    while s[rank][1] == s[rank - 1][1]: rank -= 1
    res[s[i][0]] = rank
print(*res)