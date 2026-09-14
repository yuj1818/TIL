def solution(n, m, section):
    answer = 0
    painted = [0] * (n + 1)
    for x in section:
        if painted[x]:
            continue
        answer += 1
        for i in range(x, min(n + 1, x + m)):
            painted[i] = 1
    return answer
