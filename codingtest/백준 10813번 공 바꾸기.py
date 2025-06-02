n, m = map(int, input().split())
ball = list(range(n + 1))
for _ in range(m):
    a, b = map(int, input().split())
    ball[a], ball[b] = ball[b], ball[a]
print(' '.join(map(str, ball[1:])))