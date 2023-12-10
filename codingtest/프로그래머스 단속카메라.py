def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    pre = -30001
    
    for s, e in routes:
        if s > pre:
            pre = e
            answer += 1
    return answer