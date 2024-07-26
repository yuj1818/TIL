def solution(sticker):
    N = len(sticker)
    
    if N == 1:
        return sticker[0]
    
    dp1 = [0] * N
    dp2 = [0] * N
    
    for i in range(N - 1):
        dp1[i] = max(sticker[i] + dp1[i - 2], dp1[i - 1])
    
    for j in range(1, N):
        dp2[j] = max(sticker[j] + dp2[j - 2], dp2[j - 1])

    return max(dp1[-2], dp2[-1])