import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n - 1, 0, -1):
        if a[i - 1] < a[i]:
            for j in range(n - 1, 0, -1):
                if a[i - 1] < a[j]:
                    a[i - 1], a[j] = a[j], a[i - 1]
                    a[i:] = reversed(a[i:])
                    print(' '.join(map(str, a)))
                    return
    print(-1)

if __name__ == '__main__': main()
