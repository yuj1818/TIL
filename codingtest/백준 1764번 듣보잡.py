from sys import stdin
input = stdin.readline
N, M = map(int, input().split())
not_seen_heard = sorted(list(set([input().strip('\n') for _ in range(N)]) & set([input().strip('\n') for _ in range(M)])))
print(len(not_seen_heard))
for name in not_seen_heard:
    print(name)