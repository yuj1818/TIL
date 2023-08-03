#!/usr/bin/env python
# coding: utf-8

# In[ ]:


C, R = map(int, input().split())
N = int(input())
matrix = [[0 for _ in range(C)] for _ in range(R)]
way_x = [0, 1, 0, -1]   # 하 우 상 좌
way_y = [1, 0, -1, 0]
way = 0

if N > C * R:
    print(0)
else:
    x = 0
    y = 0
    for i in range(1, C * R + 1):
        if i == N:
            print(x + 1, y + 1)
            break

        matrix[y][x] = i

        pre_x = x
        pre_y = y

        x = x + 1 * way_x[way]
        y = y + 1 * way_y[way]

        if x not in range(C) or y not in range(R) or matrix[y][x] != 0:
            way = (way + 1) % 4
            x = pre_x + 1 * way_x[way]
            y = pre_y + 1 * way_y[way]

