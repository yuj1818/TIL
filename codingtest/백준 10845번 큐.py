from sys import stdin
from collections import deque
N = int(input())
q = deque()
for _ in range(N):
    command_line = stdin.readline().split()
    command = command_line[0]
    if command == 'push':
        q.append(command_line[1])
    elif command == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        print(int(not bool(q)))
    elif command == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
