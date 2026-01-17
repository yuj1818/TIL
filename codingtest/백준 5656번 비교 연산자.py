import sys
input = sys.stdin.readline
tc = 1
while 1:
    a, op, b = input().rstrip().split()
    if op == 'E': break
    print(f"Case {tc}: {'true' if eval(a+op+b) else 'false'}")
    tc += 1