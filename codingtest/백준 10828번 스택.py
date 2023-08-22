from sys import stdin
N = int(input())
stack = []
for _ in range(N):
    command_line = stdin.readline().split()
    command = command_line[0]
    if command == 'push':
        n = command_line[1]
        stack.append(n)
    elif command == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(int(not bool(stack)))
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
