def solution(begin, target, words):
    def dfs(begin, cnt, visitied):
        nonlocal answer
        if begin == target:
            answer = min(cnt, answer)
            return
        for i in range(len(words)):
            if not visited[i] and check(words[i], begin) == length - 1:
                visited[i] = 1
                dfs(words[i], cnt + 1, visited)
                visited[i] = 0
        return
    
    length = len(target)
    answer = len(words) + 1
    visited = [0] * len(words)
    
    dfs(begin, 0, visited)
    
    if answer > len(words):
        return 0
    else:
        return answer

def check(word, target):
    result = 0
    for w, t in zip(word, target):
        if w == t:
            result += 1
    return result
