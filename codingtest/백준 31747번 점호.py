import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    a = deque(map(int, input().split()))
    tmp = [deque() for _ in range(3)]
    ans, cnt, p = 0, k, n
    for _ in range(k):
        x = a.popleft()
        tmp[x].append(1)
    while tmp[1] or tmp[2]:
        if cnt == min(k, p):
            if tmp[1] and tmp[2]:
                tmp[1].popleft()
                tmp[2].popleft()
                cnt -= 2
                p -= 2
            else:
                if tmp[1]: tmp[1].popleft()
                else: tmp[2].popleft()
                cnt -= 1
                p -= 1
            ans += 1
        if a:
            cnt += 1
            tmp[a.popleft()].append(1)
    print(ans)

main()