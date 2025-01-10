import sys
input = sys.stdin.readline

def check(s, t):
    for i in range(min(len(s), len(t))):
        if s[-i-1:] == t[0:i+1] or s[0:i+1] == t[-i-1:]: return 1
    return 0

def main():
    n = int(input())
    names = [input().strip() for _ in range(n)]
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            ans += check(names[i], names[j])
    print(ans)

if __name__ == '__main__':
    main()