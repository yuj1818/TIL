#!/usr/bin/env python
# coding: utf-8

# In[41]:


def solution(N, profit):
    if N == 1:
        return profit[0][0]

    center = N // 2

    cnt = 0
    
    total = 0
    
    plus = 1
    
    for line in profit:
        start = center - cnt
        end = center + cnt + 1
        
        if center + cnt + 1 == N:
            end = None

        total += sum(line[start:end])
        
        if cnt == center:
            plus = -1
            
        cnt += plus
    
    return total

T = int(input())

for testcase in range(1,T+1):
    N = int(input())

    profit = [list(map(int, list(input()))) for i in range(N)]
    answer = solution(N, profit)

    print(f"#{testcase} {answer}")    

