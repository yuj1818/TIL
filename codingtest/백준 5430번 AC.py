from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    if n == 0:
        input()
        nums = deque()
    else:
        nums = deque(input().replace('[', '').replace(']', '').split(','))
    sig = False
    f = True # True: 앞, False: 뒤

    for c in p:
        if c == 'R':
            f = not f
        else:
            if nums:
                if f:
                    nums.popleft()
                else:
                    nums.pop()
            else:
                sig = True
                break

    if sig:
        print('error')
    else:
        if f:
            print('[' + ','.join(nums) + ']')
        else:
            print('[' + ','.join(reversed(nums)) + ']')
