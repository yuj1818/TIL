#!/usr/bin/env python
# coding: utf-8

# In[6]:


def check_possible(N, M, K, arrive_time):
    prev = 0
    total = 0

    for i in range(N):
        term = arrive_time[i] - prev
        if total == 0 and term < M:
            return 'Impossible'

        total += term * (K / M)

        if total < 1:
            return 'Impossible'

        total -= 1
        prev = arrive_time[i]
    
    return 'Possible'

T = int(input())

for testcase in range(T):
    N, M, K = map(int, input().split())
    
    arrive_time = list(map(int, input().split()))
    
    arrive_time.sort()

    print(f'#{testcase+1} {check_possible(N, M, K, arrive_time)}')

