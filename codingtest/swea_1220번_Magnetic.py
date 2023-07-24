#!/usr/bin/env python
# coding: utf-8

# In[1]:


for testcase in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]

    answer = 0

    for i in range(N):
        s = ''
        for t in table:
            if t[i] != 0:
                s += str(t[i])
        if '12' in s:
            answer += s.count('12')

    print(answer)


# In[ ]:


1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2

