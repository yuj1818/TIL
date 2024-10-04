from collections import Counter
def solution(topping):
    ans = 0
    o = {k: v for k, v in Counter(topping).items()}
    y = dict()
    while topping:
        t = topping.pop()
        y[t] = y.get(t, 0) + 1
        o[t] -= 1
        
        if o[t] == 0:
            o.pop(t)
            
        if len(y) == len(o):
            ans += 1
    return ans