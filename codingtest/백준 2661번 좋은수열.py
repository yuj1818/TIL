import sys
input = sys.stdin.readline

def check(num):
    for i in range(1, len(num) // 2 + 1):
        if num[-i:] == num[-i * 2: -i]: return False
    return True

def find(num):
    if len(num) == n:
        print(num)
        sys.exit()

    for i in '123':
        if check(num + i):
            find(num + i)

n = int(input())
find('1')