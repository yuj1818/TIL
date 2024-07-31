from collections import deque
        
def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    s1 = sum(q1)
    s2 = sum(q2)
    cnt = 0
    
    for _ in range(len(queue1) * 3):
        if s1 > s2:
            n = q1.popleft()
            q2.append(n)
            s1 -= n
            s2 += n
        elif s1 < s2:
            n = q2.popleft()
            q1.append(n)
            s1 += n
            s2 -= n
        else:
            break
        cnt += 1
        
    else:
        return -1
    
    return cnt
    