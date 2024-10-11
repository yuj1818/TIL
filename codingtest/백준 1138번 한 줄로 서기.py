n = int(input())
people = list(map(int, input().split()))
ans = []
for i in range(n - 1, -1, -1):
    ans.insert(people[i], i + 1)
print(*ans)