import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    keywords = {input().rstrip() for _ in range(n)}
    ans = []
    for _ in range(m):
        words = set(input().rstrip().split(','))
        keywords -= words
        ans.append(str(len(keywords)))
    print('\n'.join(ans))

if __name__ == "__main__":
    main()