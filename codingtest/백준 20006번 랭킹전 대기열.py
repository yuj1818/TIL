import sys
input = sys.stdin.readline
p, m = map(int, input().split())
rooms = []
for _ in range(p):
    l, n = input().split()
    l = int(l)
    if rooms:
        for i in range(len(rooms)):
            if len(rooms[i]) < m and rooms[i][0][0] - 10 <= l <= rooms[i][0][0] + 10:
                rooms[i].append((l, n))
                break
        else:
            rooms.append([(l, n)])
    else:
        rooms.append([(l, n)])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    for player in sorted(room, key= lambda x: x[1]):
        print(*player)