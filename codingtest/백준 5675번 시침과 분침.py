import sys

while True:
    try:
        print('N' if int(sys.stdin.readline()) % 6 else 'Y')
    except: break