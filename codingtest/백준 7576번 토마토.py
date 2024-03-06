M, N = map(int, input().split())
box = []
day = 0
total = M * N
now = 0
apple_pos = []
for i in range(N):
  line = list(map(int, input().split()))
  box.append(line)
  for j in range(M):
    if line[j] == 1:
      now += 1
      apple_pos.append((i, j))
    elif line[j] == -1:
      total -= 1

d = [(-1, 0), (0, 1),  (1, 0), (0, -1)]
while apple_pos and now != total:
  day += 1
  new_pos = []
  for y, x in apple_pos:
    for dy, dx in d:
      ny = y + dy
      nx = x + dx

      if 0 <= ny < N and 0 <= nx < M and box[ny][nx] != -1 and not box[ny][nx]:
        new_pos.append((ny, nx))
        box[ny][nx] = 1
        now += 1

        if now == total:
          break
    apple_pos = new_pos

if now != total:
  print(-1)
else:
  print(day)
