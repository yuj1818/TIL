#!/usr/bin/env python
# coding: utf-8

# In[ ]:


bingo_board = [list(map(int, input().split())) for _ in range(5)]

called_nums = []

for _ in range(5):
    called_nums += list(map(int, input().split()))

# 0 ~ 4: row check, 5 ~ 9: col check, 10 ~ 11: cross check
marked = [0] * 12

bingo = 0
cnt = 0
num = 0

for called_num in called_nums:
    found_sig = 0
    cnt += 1
    for i in range(5):
        for j in range(5):
            num = bingo_board[i][j]
            if called_num == bingo_board[i][j]:
                if i == j:
                    marked[10] += 1
                if i + j == 4:
                    marked[11] += 1
                marked[i] += 1
                marked[j + 5] += 1
                found_sig = 1
                break
        if found_sig == 1:
            break
    bingo = marked.count(5)
    if bingo >= 3:
        break

print(cnt)

