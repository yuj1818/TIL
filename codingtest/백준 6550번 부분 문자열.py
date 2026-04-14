import sys

def main(x):
    s, t = map(lambda x: list(x[::-1]), x.rstrip().split())
    while s and t:
        if s[-1] == t[-1]: s.pop()
        t.pop()
    if not s: return 'Yes'
    return 'No'

if __name__ == '__main__':
    for x in sys.stdin.readlines():
        print(main(x))
