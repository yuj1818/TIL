n = int(input())
s = set(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))
for x in a:
    print(1 if x in s else 0, end=' ')