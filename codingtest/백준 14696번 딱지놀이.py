#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())

# 별 > 동그라미 > 네모 > 세모
for r in range(N):
    A = list(map(int, input().split()))
    A.pop(0)
    B = list(map(int, input().split()))
    B.pop(0)

    winner = 'D'
    for shape in range(4, 0, -1):
        if A.count(shape) > B.count(shape):
            winner = 'A'
        elif B.count(shape) > A.count(shape):
            winner = 'B'

        if winner != 'D':
            break

    print(winner)

