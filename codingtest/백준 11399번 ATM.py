n = int(input())
people = list(map(int, input().split()))
people.sort()

ans = 0
t = 0

for person in people:
    ans += person + t
    t += person

print(ans)