from collections import deque
import sys
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    a = deque(map(int, input().split()))
    tmp = deque()
    ans = 0
    while 1:
        ans += 1
        while a and len(tmp) < k:
            x = a.popleft()
            if x == 1: tmp.appendleft(1)
            else: tmp.append(2)
        if tmp[0] == tmp[-1]: tmp.popleft()
        else:
            tmp.popleft()
            tmp.pop()
        if not tmp and not a: break
    print(ans)

main()