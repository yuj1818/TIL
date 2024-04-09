N = int(input())
reqs = list(map(int, input().split()))
budget = int(input())
s = 0
e = max(reqs)

while s <= e:
  m = (s + e) // 2
  total = 0
  for req in reqs:
    if req > m:
      total += m
    else:
      total += req
  if total <= budget:
    s = m + 1
  else:
    e = m - 1

print(e)
