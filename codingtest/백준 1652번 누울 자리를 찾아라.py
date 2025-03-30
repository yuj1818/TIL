input = open(0).readline
n = int(input())
room = [input().strip() for _ in range(n)]
ans = [0, 0]

def check(room):
    ans = 0
    for t in room:
        for x in t.split('X'):
            if x and len(x) >= 2: ans += 1
    print(ans, end=' ')

check(room)
check([''.join(c) for c in zip(*room)])