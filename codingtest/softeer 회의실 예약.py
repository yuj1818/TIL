import sys
input = sys.stdin.readline
n, m = map(int, input().split())
rooms = dict()
for _ in range(n):
    rooms[input().rstrip()] = [0] * 9
for _ in range(m):
    name, s, e = input().rstrip().split()
    s, e = int(s), int(e)
    for i in range(s, e):
        rooms[name][i - 9] = 1
for idx, el in enumerate(sorted(rooms.items())):
    name, arr = el
    time = []
    i, s, e = 0, 0, 0
    while i < 9:
        if not arr[i]:
            s = i + 9
            e = s + 1
            for j in range(i + 1, 9):
                if not arr[j]:
                    e += 1
                else: 
                    time.append((s, e))
                    break
            else: time.append((s, e))
            i = e - 8
        else: i += 1
    print(f'Room {name}:')
    print(f'{len(time)} available:' if time else 'Not available')
    if time:
        for s, e in time:
            print(f'{s:02d}-{e:02d}')
    print('-----' if idx != n - 1 else '')