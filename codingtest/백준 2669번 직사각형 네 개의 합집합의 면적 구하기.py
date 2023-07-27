#!/usr/bin/env python
# coding: utf-8

# In[16]:


points = []
for _ in range(4):
    points += list(map(int, input().split()))
    
matrix = [[0] * max(points) for _ in range(max(points))]

for i in range(4):
    if i == 4:
        x1, y1, x2, y2 = points[i * 4: ]
    else:
        x1, y1, x2, y2 = points[i * 4 : (i + 1) * 4]

    for row in range(y1, y2):
        for col in range(x1, x2):
            matrix[row][col] = 1

answer = 0
for cell in matrix:
    answer += cell.count(1)

print(answer)

