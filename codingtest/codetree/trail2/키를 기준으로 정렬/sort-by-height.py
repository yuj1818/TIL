n = int(input())
a = [input().split() for _ in range(n)]
a.sort(key=lambda x:x[1])
print('\n'.join([' '.join(x) for x in a]))