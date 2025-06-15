import sys
input = sys.stdin.readline

def main():
    input()
    code = map(int, input().split())
    s = input().strip()
    a = [0] * 53
    for x in code: a[x] += 1
    for x in s:
        if x == ' ': y = 32
        elif x.islower(): y = 70
        else: y = 64
        a[ord(x) - y] -= 1
    for i in range(53):
        if a[i] < 0: return 'n'
    return 'y'

if __name__ == '__main__': print(main())