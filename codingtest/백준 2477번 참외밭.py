#!/usr/bin/env python
# coding: utf-8

# In[11]:


K = int(input())
distances = []
ways = []
for _ in range(6):
    way, distance = map(int, input().split())
    distances.append(distance)
    ways.append(way)

w_idx, h_idx = [i for i in range(6) if ways.count(ways[i]) == 1]
small_h = abs(distances[(w_idx + 1) % 6] - distances[w_idx - 1])
small_w = abs(distances[(h_idx + 1) % 6] - distances[h_idx - 1])
area = distances[w_idx] * distances[h_idx] - small_w * small_h
answer = area * K
print(answer)

