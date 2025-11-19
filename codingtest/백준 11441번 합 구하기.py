import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
acc = [A[0]]
for i in range(1, n): acc.append(acc[-1] + A[i])
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(acc[e-1] - (acc[s-2] if s - 2 >= 0 else 0))