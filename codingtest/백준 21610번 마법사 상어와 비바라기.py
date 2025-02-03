import sys
input = sys.stdin.readline
d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

def main():
    n, m = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)]
    cloud = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]
    for k in range(m):
        w, c = map(int, input().split())
        dy, dx = d[w - 1]
        # 이동 후, 비 1 씩 내리기
        for idx in range(len(cloud)):
            i, j = cloud[idx]
            ni, nj = (i + dy * c) % n, (j + dx * c) % n
            cloud[idx] = (ni, nj)
            A[ni][nj] += 1
        # 물복사 버그
        v = [[0] * n for _ in range(n)]
        for i, j in cloud:
            v[i][j] = 1
            for idx in range(1, 8, 2):
                ni, nj = i + d[idx][0], j + d[idx][1]
                if 0 <= ni < n and 0 <= nj < n and A[ni][nj]:
                   A[i][j] += 1
        # 새로운 구름 생성
        cloud = []
        for i in range(n):
            for j in range(n):
                if A[i][j] < 2 or v[i][j]: continue
                cloud.append((i, j))
                A[i][j] -= 2
    print(sum(map(sum, A)))

main()