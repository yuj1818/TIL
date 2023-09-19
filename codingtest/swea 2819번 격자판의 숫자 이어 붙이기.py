T = int(input())
dx = [0, 0, -1, 1]	# 상하좌우
dy = [-1, 1, 0, 0]

def dfs(i, j):
	if len(stack) == 7:
		nums.add(int(''.join(stack)))
		return
	for d in range(4):
		ni = i + dy[d]
		nj = j + dx[d]
		if 0 <= ni < 4 and 0 <= nj < 4:
			stack.append(board[ni][nj])
			dfs(ni, nj)
			stack.pop()

for tc in range(1, T + 1):
	board = [input().split() for _ in range(4)]
	nums = set()
	for i in range(4):
		for j in range(4):
			stack = [board[i][j]]
			dfs(i, j)
	ans = len(nums)
	print(f'#{tc} {ans}')