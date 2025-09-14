import sys
input = sys.stdin.readline
tc = 1
while 1:
    a, b = input().strip(), input().strip()
    if a == 'END' and b == 'END': break
    print(f"Case {tc}: {'same' if sorted(a) == sorted(b) else 'different'}")
    tc += 1