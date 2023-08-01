#!/usr/bin/env python
# coding: utf-8

# In[ ]:


W, H = map(int, input().split())

N = int(input())

lines = [list(map(int, input().split())) for _ in range(N)]

w_line = [0]
h_line = [0]

for line in lines:
    direction, num = line

    if direction == 0:
        h_line.append(num)
    else:
        w_line.append(num)

w_line.append(W)
h_line.append(H)
w_line.sort()
h_line.sort()

w_list = []
h_list = []

for i in range(1, len(w_line)):
    w_list.append(w_line[i] - w_line[i - 1])

for i in range(1, len(h_line)):
    h_list.append(h_line[i] - h_line[i - 1])

print(max(w_list) * max(h_list))

