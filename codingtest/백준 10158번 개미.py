#!/usr/bin/env python
# coding: utf-8

# In[ ]:


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
x_list = range(w + 1)
y_list = range(h + 1)
x = (p + t) % w
y = (q + t) % h
answer = list()
#                        지그재그 순회   2로 나누었을 때 0이면 순방향
#                                      2로 나누었을 때 1이면 역방향
answer.append(x_list[x + (w - 2 * x) * (((p + t) // w) % 2)])
answer.append(y_list[y + (h - 2 * y) * (((q + t) // h) % 2)])
print(*answer)

