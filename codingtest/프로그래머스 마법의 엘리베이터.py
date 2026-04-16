def solution(storey):
    ans = 0
    while storey > 0:
        d, m = divmod(storey, 10)
        if 5 > m or (5 == m and d % 10 < 5):
            ans += m
            storey = d
        else:
            ans += 10 - m
            storey = d + 1

    return ans

print(solution(15555))
# 19
