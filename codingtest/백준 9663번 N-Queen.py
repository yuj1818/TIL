import sys
n = int(sys.stdin.readline())
ans = 0
pos = [0] * n

def check(x):
    for i in range(x):
        if pos[x] == pos[i] or abs(x - i) == abs(pos[x] - pos[i]):
            return False
    return True

def nqueen(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        pos[x] = i
        if check(x):
            nqueen(x + 1)

nqueen(0)
print(ans)