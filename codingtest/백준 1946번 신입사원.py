T = int(input())

for tc in range(T):
  N = int(input())
  ans = N
  scores = []

  for _ in range(N):
    scores.append(tuple(map(int, input().split())))
  scores.sort(key= lambda x : x[0])
  
  grade = N
  for s1, s2 in scores:
    if s2 > grade:
      ans -= 1
    grade = min(s2, grade)
  
  print(ans)
