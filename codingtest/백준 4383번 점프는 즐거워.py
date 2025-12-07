import sys
while 1:
    try:
        n, *arr = map(int, sys.stdin.readline().split())
        print('Jolly' if set([abs(arr[i] - arr[i - 1]) for i in range(1, n)]) == set(range(1, n)) else 'Not jolly')
    except: break