import sys
input = sys.stdin.readline

def main():
    dif = lambda x: x[1] - x[0] if x[1] - x[0] >= 0 else 0
    n, k = map(int, input().split())
    AB = [dif(list(map(int, input().split()))) for _ in range(n)]
    AB.sort()
    print(AB[k - 1])

main()