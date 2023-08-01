#!/usr/bin/env python
# coding: utf-8

# In[3]:


N = int(input())

matrix = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, N + 1):
    x, y, width, height = map(int, input().split())

    for row in range(y, y + height):
        matrix[row][x:x + width] = [i] * width

for i in range(1, N + 1):
    answer = 0
    for row in matrix:
        answer += row.count(i)
    print(answer)

