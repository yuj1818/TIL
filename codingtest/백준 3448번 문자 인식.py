import sys
N = int(sys.stdin.readline())
for _ in range(N):
    R, A = 0, 0
    while True:
        line = sys.stdin.readline().rstrip()
        if line == '': break
        for char in line:
            if char == '#': A += 1
            else:
                A += 1
                R += 1
    ratio = round(R / A * 100, 1)
    if str(ratio).split('.')[-1] == '0':
        ratio = int(ratio)
    print(f'Efficiency ratio is {ratio}%.')