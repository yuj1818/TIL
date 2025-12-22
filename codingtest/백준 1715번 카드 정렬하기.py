from heapq import heappush, heappop
import sys
input = sys.stdin.readline
n = int(input())
deck = []
for _ in range(n): heappush(deck, int(input()))
acc = 0
while len(deck) > 1:
    a, b = heappop(deck), heappop(deck)
    acc += a + b
    heappush(deck, a + b)
print(acc)