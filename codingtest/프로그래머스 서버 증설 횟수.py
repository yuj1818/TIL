def solution(players, m, k):
    s = [0] * 24
    cnt = 0
    for i in range(24):
        v = players[i] // m - s[i]
        if v > 0:
            for j in range(k):
                if i + j >= 24:
                    break
                s[i + j] += v
            cnt += v
    print(s)
    return cnt
