import sys
input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    com = set()
    for _ in range(n):
        name, c = input().split()
        if c == 'enter': com.add(name)
        else: com.remove(name)
    sys.stdout.write('\n'.join(sorted(com, reverse=True)))

main()