N = int(input())
member = []
for i in range(N):
    age, name = input().split()
    member.append([int(age), name, i])
for a, n, idx in sorted(member, key=lambda x: (x[0], x[2])):
    print(a, n)