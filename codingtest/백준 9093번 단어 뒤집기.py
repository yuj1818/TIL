input = open(0).readline
def main():
    for _ in range(int(input())):
        s = [x[::-1] for x in input().strip().split()]
        print(' '.join(s))
main()