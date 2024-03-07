N, C = map(int, input().split())
msg = list(map(int, input().split()))
cnt = {}
for num in msg:
  cnt[num] = cnt.get(num, 0)
  cnt[num] += 1
cnt = sorted(cnt.items(), key= lambda x:-x[1])
ans = []
for num, c in cnt:
  for _ in range(c):
    ans.append(num)
print(' '.join(map(str, ans)))
