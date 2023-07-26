#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input())
move_list = list(map(int, input().split()))
answer = []
for i in range(n):
    dist = move_list[i]
    if dist == 0:
        answer.append(str(i+1))
    else:
        answer.insert(len(answer) - dist, str(i+1))
print(' '.join(answer))

