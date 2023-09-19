T = int(input())

def dfs(prod_n, cost):
	global min_cost
	if prod_n == N:
		min_cost = min(min_cost, cost)
		return
	if cost > min_cost:
		return
	for i in range(N):
		if not visited[i]:
			visited[i] = 1
			dfs(prod_n + 1, cost + V[prod_n][i])
			visited[i] = 0

for tc in range(1, T + 1):
	N = int(input())
	V = [list(map(int, input().split())) for _ in range(N)]
	visited = [0] * N
	min_cost = float('inf')
	dfs(0, 0)
	print(f'#{tc} {min_cost}')