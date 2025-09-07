import sys
input = sys.stdin.readline
for _ in range(int(input())):
    m, n = input().strip().split()
    if m == '1': print(int(''.join(map(lambda x: format(int(x), '08b'), n.split('.'))), 2))
    else:
        n = format(int(n), '064b')[::-1]
        print('.'.join(map(lambda x: str(int(x, 2)), [n[i:i+8][::-1] for i in range(0, len(n), 8)][::-1])))