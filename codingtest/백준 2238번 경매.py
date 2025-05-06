import sys
input = sys.stdin.readline

def main():
    u, n = map(int, input().split())
    arr = dict()
    for _ in range(n):
        s, p = input().split()
        p = int(p)
        if p in arr: arr[p].append(s)
        else: arr[p] = [s]
    arr = sorted(arr.items(), key=lambda x: (len(x[1]), x[0]))
    c, a = arr[0]
    print(a[0], c)

main()