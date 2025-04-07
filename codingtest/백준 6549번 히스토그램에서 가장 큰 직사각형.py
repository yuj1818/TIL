import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def main():
    while 1:
        n, *arr = list(map(int, input().split()))
        if n == 0: break
        s = [(0, arr[0])]
        ans = 0
        for i in range(1, n):
            if s[-1][1] > arr[i]:
                while s and s[-1][1] > arr[i]:
                    idx, h = s.pop()
                    if s: a = (i - s[-1][0] - 1) * h
                    else: a = i * h
                    if ans < a: ans = a
            s.append((i, arr[i]))
        while s:
            idx, h = s.pop()
            if s: a = (n - s[-1][0] - 1) * h
            else: a = n * h
            if ans < a: ans = a
        print(ans)

main()