import sys
input = sys.stdin.readline
f = lambda x: True if x == '1' else False
n = int(input())
cur = list(map(f, input().rstrip()))
goal = list(map(f, input().rstrip()))

def change(state, cnt):
    for i in range(1, n):
        if state[i - 1] == goal[i - 1]: continue
        cnt += 1
        for j in range(i - 1, i + 2):
            if j < n:
                state[j] = not state[j]
    if state == goal: return cnt
    else: return -1

if cur == goal:
    print(0)
else:
    cur_cp = cur.copy()
    off = change(cur, 0)
    if off != -1: print(off)
    else:
        cur_cp[0] = not cur_cp[0]
        cur_cp[1] = not cur_cp[1]
        on = change(cur_cp, 1)
        print(on)