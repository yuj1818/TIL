from queue import PriorityQueue
from sys import stdin
input = stdin.readline
N = int(input())
nums = PriorityQueue(maxsize=N)
for _ in range(N):
    num = int(input())
    if not num:
        if nums.qsize():
            print(nums.get())
        else:
            print(0)
    else:
        nums.put(num)