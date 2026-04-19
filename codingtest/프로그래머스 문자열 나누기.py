def solution(s):
    ans = 0
    s = list(s)
    while s:
        x = s.pop(0)
        cx, co = 1, 0
        while cx != co and s:
            y = s.pop(0)
            if y == x: cx += 1
            else: co += 1
        ans += 1
    if s: ans += 1
    return ans
    
