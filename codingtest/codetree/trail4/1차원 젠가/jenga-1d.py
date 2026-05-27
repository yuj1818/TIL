n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())
for _ in range(e1 - s1 + 1): blocks.pop(s1 - 1)
for _ in range(e2 - s2 + 1): blocks.pop(s2 - 1)
print(len(blocks))
print('\n'.join(map(str, blocks)))
