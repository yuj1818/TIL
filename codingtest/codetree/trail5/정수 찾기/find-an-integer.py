n = int(input())
a = set(map(int, input().split()))
m = int(input())
for x in list(map(int, input().split())):
    print(1 if x in a else 0)