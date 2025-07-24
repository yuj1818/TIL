import sys
input = sys.stdin.readline
n = int(input())
days = list(map(int, input().split()))
days.sort(reverse=True)
for i in range(n - 1): days[i] -= n - 1 - i
print(n + max(days) + 1)