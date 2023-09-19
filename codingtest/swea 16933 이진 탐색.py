T = int(input())

def binary_search(l, r, target):
    global sig
    if l > r:
        return False
    else:
        mid = (l + r) // 2
        if target == A[mid]:
            return True
        elif target > A[mid]:
            if direction[-1] == 'r':
                sig = False
                return
            direction.append('r')
            return binary_search(mid + 1, r, target)
        else:
            if direction[-1] == 'l':
                sig = False
                return
            direction.append('l')
            return binary_search(l, mid - 1, target)


for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A, B = list(map(int, input().split())), list(map(int, input().split()))
    A.sort()
    ans = 0
    for el in B:
        sig = True
        direction = ['']
        if binary_search(0, N - 1, el) and sig:
            ans += 1
    print(f'#{tc} {ans}')