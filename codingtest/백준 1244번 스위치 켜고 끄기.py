#!/usr/bin/env python
# coding: utf-8

# In[5]:


N = int(input())

on_off = list(map(int, input().split()))

student_num = int(input())

for _ in range(student_num):
    g, n = map(int, input().split())

    if g == 1:
        for i in range(1, N // n + 1):
            on_off[n * i - 1] = int(not(on_off[n * i - 1]))
    else:
        on_off[n - 1] = int(not (on_off[n - 1]))
        for i in range(1, min(n - 1, N - n) + 1):
            if on_off[n - 1 - i] == on_off[n - 1 + i]:
                on_off[n - 1 - i] = int(not(on_off[n - 1 - i]))
                on_off[n - 1 + i] = int(not(on_off[n - 1 + i]))
            else:
                break

for i in range(0, N // 20 + 1):
    print(*on_off[i * 20:(i + 1) * 20])

