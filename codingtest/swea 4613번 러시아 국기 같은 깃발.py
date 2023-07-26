#!/usr/bin/env python
# coding: utf-8

# In[ ]:


T = int(input())

for testcase in range(T):
    N, M = map(int, input().split())
    color_map = [input() for _ in range(N)]

    answer = N * M


    for wc in range(N-2):  # 파랑, 빨강 최소 한 줄씩 남겨두기
        ch_w = 0
        for line in color_map[:wc + 1]:
            ch_w += M - line.count('W')
        for bc in range(wc + 1, N - 1):
            ch_b = 0
            for line in color_map[wc + 1:bc + 1]:
                ch_b += M - line.count('B')
            ch_r = 0
            for line in color_map[bc + 1:]:
                ch_r += M - line.count('R')
            answer = min(answer, ch_w + ch_b + ch_r)

    print(f'#{testcase+1} {answer}')

