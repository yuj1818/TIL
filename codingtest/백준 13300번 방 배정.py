#!/usr/bin/env python
# coding: utf-8

# In[1]:


N, K = map(int, input().split())

students = {
    0: {},
    1: {}
}

room = 0

for _ in range(N):
    S, grade = map(int, input().split())
    students[S][grade] = students[S].get(grade, 0) + 1
    
for s_key in students.keys():
    for g_key in students[s_key].keys():
        if students[s_key][g_key] % K == 0:
            room += students[s_key][g_key] // K
        else:
            room += students[s_key][g_key] // K + 1
            
print(room)            

