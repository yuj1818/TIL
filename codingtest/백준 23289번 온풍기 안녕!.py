from collections import deque
import sys
input = sys.stdin.readline
dyx = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

def main():
    def heat():
        temp = [[0] * C for _ in range(R)]
        for i, j, d in heater:
            if d == 1: j += 1
            elif d == 2: j -= 1
            elif d == 3: i -= 1
            elif d == 4: i += 1
            q = deque([(i, j, 5)])
            visited = [[0] * C for _ in range(R)]
            visited[i][j] = 1
            while q:
                ci, cj, cp = q.popleft()
                temp[ci][cj] += cp
                if cp == 1: continue
                dy, dx = dyx[d]
                if d < 3:
                    nj = cj + dx
                    if nj < 0 or nj >= C: continue
                    if not visited[ci][nj] and not walls[ci][cj][d]:
                        q.append((ci, nj, cp - 1))
                        visited[ci][nj] = 1
                    for ni, nd in [(ci - 1, 4), (ci + 1, 3)]:
                        if 0 <= ni < R and not visited[ni][nj] and not (walls[ni][cj][d] or walls[ni][cj][nd]):
                            q.append((ni, nj, cp - 1))
                            visited[ni][nj] = 1
                else:
                    ni = ci + dy
                    if ni < 0 or ni >= R: continue
                    if not visited[ni][cj] and not walls[ci][cj][d]:
                        q.append((ni, cj, cp - 1))
                        visited[ni][cj] = 1
                    for nj, nd in [(cj - 1, 1), (cj + 1, 2)]:
                        if 0 <= nj < C and not visited[ni][nj] and not (walls[ci][nj][d] or walls[ci][nj][nd]):
                            q.append((ni, nj, cp - 1))
                            visited[ni][nj] = 1
        return temp

    def update():
        for i in range(R):
            for j in range(C):
                if temp[i][j] != 0: room[i][j] += temp[i][j]

    def control():
        diff = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                for dy, dx, nd in [(0, 1, 1), (1, 0, 4)]:
                    ni, nj = i + dy, j + dx
                    if 0 <= ni < R and 0 <= nj < C and not walls[i][j][nd]:
                        x = abs(room[ni][nj] - room[i][j])
                        if x < 4: continue
                        v = x // 4
                        if room[ni][nj] > room[i][j]:
                            diff[ni][nj] -= v
                            diff[i][j] += v
                        else:
                            diff[ni][nj] += v
                            diff[i][j] -= v
        for i in range(R):
            for j in range(C):
                if diff[i][j] != 0:
                    room[i][j] += diff[i][j]

    def outside():
        for i in range(0, R):
            for j in [0, C - 1]:
                if room[i][j] >= 1: room[i][j] -= 1
        for j in range(1, C - 1):
            for i in [0, R - 1]:
                if room[i][j] >= 1: room[i][j] -= 1

    def inspect():
        for i, j in watch:
            if room[i][j] < K:
                return False
        return True

    R, C, K = map(int, input().split())
    room = [[0] * C for _ in range(R)]
    heater = []
    watch = []
    ans = 0
    for i in range(R):
        row = list(map(int, input().split()))
        for j in range(C):
            if row[j] == 5:
                watch.append((i, j))
            elif row[j] > 0:
                heater.append((i, j, row[j]))
    W = int(input())
    walls = [[[0] * 5 for _ in range(C)] for _ in range(R)]
    for _ in range(W):
        y, x, t = map(int, input().split())
        x -= 1
        y -= 1
        if t == 0:
            walls[y][x][3] = 1
            if y > 0: walls[y - 1][x][4] = 1
        else:
            walls[y][x][1] = 1
            if x < C - 1: walls[y][x + 1][2] = 1

    temp = heat()
    while 1:
        update()
        control()
        outside()
        ans += 1
        if ans == 101: break
        if inspect(): break

    return ans

if __name__ == '__main__':
    print(main())