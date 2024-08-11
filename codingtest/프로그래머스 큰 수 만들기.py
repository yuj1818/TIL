def solution(number, k):
    number = list(map(int, number))
    ans = []
    
    for n in number:
        if ans:
            while k > 0 and ans and ans[-1] < n:
                ans.pop()
                k -= 1
        ans.append(n)
        
    ans = ans[:-k] if k > 0 else ans
    return ''.join(map(str, ans))