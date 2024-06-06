from collections import deque
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    a, b = map(int, input().split())
    q = deque([(a, '')])
    nums = {a: 1}

    def add(num, c, pre):
        if not nums.get(num):
            q.append((num, pre + c))
            nums[num] = 1

    while q:
        n, command = q.popleft()

        if n == b:
            print(command)
            break

        d = (n * 2) % 10000
        s = n - 1 if n > 0 else 9999
        l = (n % 1000) * 10 + n // 1000
        r = (n % 10) * 1000 + n // 10

        for num, c in [(d, 'D'), (s, 'S'), (l, 'L'), (r, 'R')]:
            add(num, c, command)