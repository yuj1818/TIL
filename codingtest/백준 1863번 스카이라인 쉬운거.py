import sys
input = sys.stdin.readline

def main():
    s = [0]
    ans = 0
    for _ in range(int(input())):
        x, y = map(int, input().split())
        while s[-1] > y:
            s.pop()
            ans += 1
        if s[-1] < y: s.append(y)
    print(ans + len(s) - 1)

main()