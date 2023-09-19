T = int(input())

def dfs(i, percent):
	global max_v
	if percent < max_v:
		return
	if i == N:
		max_v = percent
	for j in range(N):
		if not visited[j]:
			visited[j] = 1
			dfs(i + 1, percent * P[i][j] * 0.01)
			visited[j] = 0

for tc in range(1, T + 1):
	N = int(input())
	P = [list(map(int, input().split())) for _ in range(N)]
	max_v = 0
	visited = [0] * N
	dfs(0, 1)
	max_v *= 100
	print(f'#{tc} {max_v:.6f}')