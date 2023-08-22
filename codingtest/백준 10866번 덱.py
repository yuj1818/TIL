from sys import stdin
from collections import deque
N = int(input())
d = deque()
for _ in range(N):
    command_line = stdin.readline().split()
    command = command_line[0]
    if 'push' in command:
        n = command_line[1]
        if command == 'push_front':
            d.appendleft(n)
        elif command == 'push_back':
            d.append(n)
    elif command == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif command == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(d))
    elif command == 'empty':
        print(int(not bool(d)))
    elif command == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif command == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)