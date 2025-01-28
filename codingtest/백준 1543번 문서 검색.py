import sys

def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    print(s.count(t))

main()