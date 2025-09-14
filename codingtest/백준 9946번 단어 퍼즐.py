import sys
input = sys.stdin.readline
tc = 1
while 1:
    a, b = input().strip(), input().strip()
    if a == 'END' and b == 'END': break
    sig = 1
    for i in range(97, 123):
        if a.count(chr(i)) != b.count(chr(i)):
            sig = 0
            break
    print(f"Case {tc}: {'same' if sig else 'different'}")
    tc += 1