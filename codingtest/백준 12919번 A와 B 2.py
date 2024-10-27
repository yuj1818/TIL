import sys
input = sys.stdin.readline

def dfs(t):
    global s
    if len(t) == len(s):
        if t == s:
            print(1)
            sys.exit()
    else:
        if t[-1] == 'A':
            dfs(t[:-1])
        if t[0] == 'B':
            dfs(t[1:][::-1])

if __name__ == '__main__':
    s = input().rstrip()
    dfs(input().rstrip())
    print(0)