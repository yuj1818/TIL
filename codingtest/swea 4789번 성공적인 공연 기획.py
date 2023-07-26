#!/usr/bin/env python
# coding: utf-8

# In[5]:


T = int(input())

for testcase in range(T):
    applause = input()
    
    standing = 0
    employee = 0
    for i in range(len(applause)):
        if standing < i:
            lack = i - standing
            employee += lack
            standing += lack
        standing += int(applause[i])
    print(f'#{testcase+1} {employee}')

