#!/usr/bin/env python
# coding: utf-8

# In[12]:


def check_omok(board, N):
    dirX = [1, 0, -1]  # 우하단, 하단, 좌하단
    dirY = [1, 1, 1]

    row = 0
    for line in board:  # 가로 오목 확인
        if 'o' * 5 in line:
            return 'YES'

        for x in range(N):
            if line[x] == 'o':
                for dx, dy in zip(dirX, dirY):
                    stone = 1
                    posX = x + dx
                    posY = row + dy
                    while 0 <= posX < N and 0 <= posY < N and board[posY][posX] == 'o' and stone < 5:
                        posY += dy
                        posX += dx
                        stone += 1
                    if stone == 5:
                        return 'YES'
        row += 1
    return 'NO'


T = int(input())

for testcase in range(T):
    N = int(input())

    board = [input() for i in range(N)]

    print(f'#{testcase+1} {check_omok(board, N)}')

