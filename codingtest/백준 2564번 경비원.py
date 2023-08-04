w, h = map(int, input().split())
n = int(input())
distances = []

for _ in range(n + 1):
    way, pos = map(int, input().split())
    if way == 1:
        distances.append(pos)
    elif way == 2:
        distances.append(w + h + (w - pos))
    elif way == 3:
        distances.append(2 * w + h + (h - pos))
    else:
        distances.append(w + pos)

answer = 0

for distance in distances[:-1]:
    dif = abs(distances[-1] - distance)
    answer += min(dif, 2 * (w + h) - dif)

print(answer)