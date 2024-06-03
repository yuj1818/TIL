import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    k = int(input())
    minH = []
    maxH = []
    nums = defaultdict(int)
    for _ in range(k):
        c, n = input().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(minH, n)
            heapq.heappush(maxH, -n)
            nums[n] += 1
        else:
            if n == 1 and maxH:
                nums[-heapq.heappop(maxH)] -= 1
            elif minH:
                nums[heapq.heappop(minH)] -= 1


        while maxH and nums[-maxH[0]] < 1:
            heapq.heappop(maxH)

        while minH and nums[minH[0]] < 1:
            heapq.heappop(minH)

    print('EMPTY' if not minH else '{} {}'.format(-heapq.heappop(maxH), heapq.heappop(minH)))