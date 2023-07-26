#!/usr/bin/env python
# coding: utf-8

# In[3]:


T = int(input())

for testcase in range(T):
    N = int(input())
    
    num_set = set()
    i = 0
    lamb_num = 0
    while len(num_set) < 10:
        i += 1
        lamb_num = i * N
        num_set.update(list(str(lamb_num)))
        
    print(f'#{testcase+1} {lamb_num}')

