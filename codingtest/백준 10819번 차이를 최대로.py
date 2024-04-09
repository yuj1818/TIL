N = int(input())
nums = list(map(int, input().split()))

mv = 0

def dfs(s, v):
  global mv

  if sum(visited) == N:
    mv = max(mv, v)
    return

  for j in range(N):
    if not visited[j]:
      visited[j] = 1
      dfs(j, v + abs(nums[s] - nums[j]))
      visited[j] = 0

for i in range(N):
  visited = [0] * N
  visited[i] = 1
  dfs(i, 0)

print(mv)
