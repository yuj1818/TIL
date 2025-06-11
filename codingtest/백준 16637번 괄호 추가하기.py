import sys
input = sys.stdin.readline

def dfs(i, v):
    global mv
    if i == n:
        if mv < int(v): mv = int(v)
        return
    if i + 4 <= n:
        dfs(i + 4, str(eval(''.join([v, f[i]] + [str(eval(''.join(f[i + 1:i + 4])))]))))
    if i + 2 <= n:
        dfs(i + 2, str(eval(''.join([v] + f[i:i + 2]))))

def main():
    global n, f, mv
    n = int(input())
    f = list(input().strip())
    mv = float('-inf')
    dfs(1, f[0])
    print(mv)

if __name__ == '__main__': main()