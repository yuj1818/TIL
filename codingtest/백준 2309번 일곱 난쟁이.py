#!/usr/bin/env python
# coding: utf-8

# In[2]:


from itertools import combinations

heights = [int(input()) for _ in range(9)]

all_comb = list(combinations(heights, 7))

answer = []
for comb in all_comb:
    if sum(comb) == 100:
        answer = comb
        break

for height in sorted(comb):
    print(height)

