def solution(n, stations, w):
    ans = 0
    
    if stations[0] - w > 1:
        ans += -(-(stations[0] - w - 1) // (w * 2 + 1))
        
    if stations[-1] + w < n:
        ans += -(-(n - (stations[-1] + w)) // (w * 2 + 1))
    
    for i in range(len(stations) - 1):
        if stations[i + 1] - stations[i] - (w * 2) - 1 > 0:
            ans += -(-(stations[i + 1] - stations[i] - (w * 2) - 1) // (w * 2 + 1))
        
    return ans