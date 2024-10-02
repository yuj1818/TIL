import sys
input = sys.stdin.readline
n, k = map(int, input().split())
pos = input()

def solution(n, k, pos):
    ans, h = 0, 0
    for i, p in enumerate(pos):
        if p == 'P':
            while h < n and (pos[h] != 'H' or h < i - k):
                h += 1
            if h == n:
                return ans
            if i - k <= h <= i + k:
                h += 1
                ans += 1
    return ans

print(solution(n, k, pos))