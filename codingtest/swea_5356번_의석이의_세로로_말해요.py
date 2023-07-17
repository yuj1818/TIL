#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import deque

T = int(input())

for testcase in range(1, T+1):
        
    words = []
    
    for i in range(5):
        queue = deque(input())
        words.append(queue)
        
    answer = ""
    
    cnt = 0
    empty = []
    while(len(empty) != 5):
        for i in range(len(words)):
            if len(words[i]) == 0:
                cnt += 1
                if i not in empty:
                    empty.append(i)
            else:
                answer += words[i].popleft()
                
    print(f"#{testcase} {answer}")

