import sys
input = sys.stdin.readline
n = int(input())
ans = 0
people = [0] * 2000001
for _ in range(n):
    a, b = map(int, input().split())
    if people[a] == b:
        ans += 1
    people[a] = b
print(ans + sum(people))