import sys

def main():
    s = list(map(int, sys.stdin.readline().strip())) + [-1]
    c = [0, 0]
    x = s[0]
    for i in range(1, len(s)):
        if s[i] != x:
            c[s[i-1]] += 1
        x = s[i]
    print(min(c))

main()