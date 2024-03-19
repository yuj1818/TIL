N, S = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(1<<N):
  s = []
  for j in range(N):
    if i & (1<<j):
      s.append(a[j])
  if s and sum(s) == S:
    cnt += 1
print(cnt)
