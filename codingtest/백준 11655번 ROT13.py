import sys
for x in sys.stdin.readline().rstrip():
    if x.isalpha():
        c = 97 if x.islower() else 65
        print(chr(c + (ord(x) + 13 - c) % 26), end='')
    else: print(x, end='')