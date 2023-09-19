T = int(input())

def dfs(s, n, cnt):
	global min_cnt
	if n >= N - 1:
		min_cnt = min(min_cnt, cnt)
		return
	if cnt > min_cnt:
		return
	for i, capacity in stations[s + 1:n + 1]:
		dfs(i, i + capacity, cnt + 1)

for tc in range(1, T + 1):
	info = list(map(int, input().split()))
	N = info[0]
	stations = list(enumerate(info[1:]))
	min_cnt = float('inf')
	dfs(stations[0][0], stations[0][1], 0)
	print(f'#{tc} {min_cnt}')