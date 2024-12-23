import sys

def main():
    s = sys.stdin.readline().strip()
    b = list(sys.stdin.readline().strip())
    lb = len(b)
    ans = []
    for x in s:
        ans.append(x)
        if x == b[-1] and ans[-lb:] == b:
            del ans[-lb:]
    print(''.join(ans) if ans else 'FRULA')
    
main()